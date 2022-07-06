"""
tks to: [DeepL Api 设计中的欺骗战术 - zu1k](https://zu1k.com/posts/thinking/deception-tactics-in-deepl-api-design/)
"""

from ast import Dict
import json
import os
from typing import Literal, Mapping, Optional, Tuple

import requests

from algo import handlePayload, initId, initTimestampFromSentences
from const import URL_DEEPL_TRANSLATE, headers, LOG_PATH, LangsSupportTerminology
from utils import gen_jobs, eprint
from ds import Payload


def callTranslationViaDeepL(
    to_translate: str,
    target_lang="CH",
    from_lang="EN",
    proxy: Optional[str] = None,
    terminology: str = "",
) -> Optional[dict]:
    """

    :param to_translate: one word, sentence, or paragraph, pay attention to its length, since I noticed there is a limit in deepl's api, which seems to be 5000 words.
    :param proxy: proxy is vital if you have a bunch of text to translate, since we can only solve the problems from the client side, not from the server side
    :return:
    """
    if not to_translate:
        eprint("DENIED since your input is blank")
        return

    # print({"terminology": terminology})
    terminologyDict: Mapping[str, str] = dict(
        i.split("\t") for i in terminology.splitlines() if i)
    # pre process sentences
    if terminologyDict and (from_lang not in LangsSupportTerminology or target_lang not in LangsSupportTerminology):
        for k, v in terminologyDict.items():
            to_translate = to_translate.replace(k, v)

    sentences = [i + '.' for i in to_translate.split(".") if i]
    timestamp = initTimestampFromSentences(sentences)
    id = initId()
    # print({"timestamp": timestamp, "id": id, "input": sentences})

    payload_json: Payload = {
        "jsonrpc": "2.0",
        "method": "LMT_handle_jobs",
        "params": {
            "jobs": gen_jobs(sentences),
            "lang": {
                "preference": {
                    "weight": {},
                    "default": "default"
                },
                # todo: 在deepl中，源语言既可以由用户指定，也可以计算得知，因此要写两套api
                "source_lang_computed": from_lang,
                "target_lang": target_lang
            },
            "priority": -1,  # 有时是1，有时是-1
            "commonJobParams": {
                "browserType": 1,
                # only specific languages can be used
                # "termbase": {"dictionary": "loop closing\t回环检测\nmonocular\t单目\nstereo\t双目"}
            },
            "timestamp": timestamp
        },
        "id": initId()
    }

    if terminology and from_lang in LangsSupportTerminology and target_lang in LangsSupportTerminology:
        termbase = {"dictionary": terminology.strip()}
        payload_json["params"]["commonJobParams"]["termbase"] = termbase
    # else: payload_json["params"]["commonJobParams"]["terminology"] = None

    # the payload should be no spaces between keys or values, ref: https://stackoverflow.com/a/16311587/9422455
    payload_dumped = json.dumps(payload_json, separators=(",", ":"))
    payload_to_post = handlePayload(payload_dumped, id)
    # print({"payload_to_post": payload_to_post})

    sess = requests.Session()
    sess.headers = headers
    # sess.verify = False
    if proxy:
        sess.proxies = {"http": proxy, "https": proxy}

    res = sess.post(URL_DEEPL_TRANSLATE, data=payload_to_post).json()
    if "result" not in res:
        eprint(
            f"failed to translate reason: [{res['error']['message']}]")
        err_fn = "error.log"
        err_fp = os.path.join(LOG_PATH, err_fn)
        with open(err_fp, "w") as f:
            json.dump(res, f, ensure_ascii=False, indent=2)
            eprint(
                f"the log has been dumped into file://{err_fp}")
        return
    return res
