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
    print(callTranslationViaDeepL("are you ok?"))
