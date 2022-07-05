"""
tks to: [DeepL Api 设计中的欺骗战术 - zu1k](https://zu1k.com/posts/thinking/deception-tactics-in-deepl-api-design/)
"""

import json
import random
import time
from typing import Optional

import requests

timestamp = time.time()

url = 'https://www2.deepl.com/jsonrpc?method=LMT_handle_jobs'

headers = {
    # cookie is not necessary, and put ua here is out of habit
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
    "Content-Type": "application/json"
}


def callTranslationViaDeepL(to_translate: str) -> Optional[dict]:
    """

    :param to_translate:
    :return:
        sample return when to_translate == "are you ok" @ 2022/07/05:
        {'jsonrpc': '2.0', 'id': 69910001, 'result': {'translations': [{'beams': [{'sentences': [{'text': '你还好吗？', 'ids': [0]}], 'num_symbols': 6}, {'sentences': [{'text': '你还好吗', 'ids': [0]}], 'num_symbols': 5}, {'': [{'text': '你还好吗?', 'ids': [0]}], 'num_symbols': 6}, {'sentences': [{'text': '你没事吧？', 'ids': [0]}], 'num_symbols': 6}], 'quality': 'normal'}], 'target_lang': 'ZH', 'source_lang': 'EN', 'source_lang_is_confalse, 'detectedLanguages': {'EN': 0.063362, 'DE': 0.002077, 'FR': 0.025998, 'ES': 0.011035, 'PT': 0.005216, 'IT': 0.0055969999999999995, 'NL': 0.021662, 'PL': 0.007718, 'RU': 0.0019399999999999999, 'ZH': 0.0033729999999999997, 'JA': 0.0005009999999999999, 'BG': 0.0008179999999999999, 'CS': 0.051376, 'DA': 0.004497999999999999, 'EL': 0.001078, 'ET': 0.013248, 'FI': 0.0014759999999999999, 'HU': 0.0014269999999999999, 'LT': 0.004829, 'LV': 0.002709, 'RO': 0.00481, 'SK': 0.006817999999999999, 'SL': 0.001738, 'SV': 0.011986, 'TR': 0.058573999999999994, 'ID': 0.010589999999999999, 'unsupported': 0.675547}}}
    """
    if not to_translate:
        print("DENIED since your input is blank")
        return

    def initId():
        """
        ref:
            https://static.deepl.com/js/utils.chunk.$5d3184.js:formatted:1508
        :return:
        """
        return int(1e4 * round(1e4 * random.random())) + 1

    def handlePayload(e: str, t: int):
        """
        ref:
            https://static.deepl.com/js/translator_late.min.$e1ac03.js:formatted:15229
        code:
            f_str: function(e, t) {
                return e.replace('hod":"', (t + 3) % 13 == 0 || (t + 5) % 29 == 0 ? 'hod" : "' : 'hod": "')
            }
        :param e:
        :param t:
        :return:
        """
        return e.replace('hod":"', 'hod" : "' if (t + 3) % 13 == 0 or (t + 5) % 29 == 0 else 'hod": "')

    id = initId()

    payload = {"jsonrpc": "2.0", "method": "LMT_handle_jobs", "params": {"jobs": [
        {"kind": "default", "sentences": [{"text": to_translate, "id": 0, "prefix": ""}],
         "raw_en_context_before": [], "raw_en_context_after": [], "preferred_num_beams": 4, "quality": "fast"}],
        "lang": {
            "preference": {
                "weight": {"DE": 0.1818, "EN": 13.50072, "ES": 0.25707, "FR": 0.30468, "IT": 0.28796, "JA": 0.10335,
                           "NL": 0.28976, "PL": 0.28227, "PT": 0.13819, "RU": 0.1102, "ZH": 0.22576, "BG": 0.07641,
                           "CS": 0.43894, "DA": 0.13387, "EL": 0.07787, "ET": 0.16358, "FI": 0.31664, "HU": 0.09349,
                           "LT": 0.08603, "LV": 0.06412, "RO": 0.12765, "SK": 0.11411, "SL": 0.10327, "SV": 0.24992,
                           "TR": 0.95955, "ID": 0.15974}, "default": "default"}, "source_lang_user_selected": "EN",
            "target_lang": "ZH"}, "priority": -1, "commonJobParams": {"browserType": 1, "formality": None},
        "timestamp": int(timestamp * 1000)}, "id": id}

    payload = handlePayload(json.dumps(payload), id)

    res = requests.post(url, headers=headers, data=payload)
    return res.json()


if __name__ == '__main__':
    import argparse

    args = argparse.ArgumentParser(
        description="""deepl api (unofficial)
    currently supported:
        - [√] english -> chinese 
        - [x] chinese -> english, it is on the agenda if I have time :)
        
    examples:
        [attention] you should use QUOTES to wrap all your words to translate
        1. return plain text:
            python main.py "are you ok"
            
        2. return json (with more info)
            python main.py "are you ok" -f json
        """,
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    args.add_argument("to_translate", help="words to translate")
    args.add_argument("-f", "--format", help="return format, json(full) or plain(direct result)",
                      choices=["json", "plain"], default="plain")
    parser = args.parse_args()

    result = callTranslationViaDeepL(parser.to_translate)
    if not result:
        print("ABORT since there is no return!")
        exit(-1)

    if parser.format == "json":
        output = result
    else:
        output = result["result"]["translations"][0]["beams"][0]["sentences"][0]["text"]

    print(output)
