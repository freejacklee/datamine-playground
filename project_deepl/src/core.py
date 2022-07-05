"""
tks to: [DeepL Api 设计中的欺骗战术 - zu1k](https://zu1k.com/posts/thinking/deception-tactics-in-deepl-api-design/)
"""

import json
import os
from typing import Optional

import requests

from algo import handlePayload, initId, initTimestampFromSentences
from const import URL_DEEPL_TRANSLATE, headers, LOG_PATH
from utils import gen_jobs


def callTranslationViaDeepL(to_translate: str, proxy: str = None) -> Optional[dict]:
    """

    :param to_translate: one word, sentence, or paragraph, pay attention to its length, since I noticed there is a limit in deepl's api, which seems to be 5000 words.
    :param proxy: proxy is vital if you have a bunch of text to translate, since we can only solve the problems from the client side, not from the server side
    :return:
    """
    if not to_translate:
        print("DENIED since your input is blank")
        return

    sentences = [i for i in to_translate.split(".") if i]
    timestamp = initTimestampFromSentences(sentences)
    id = initId()
    # print({"timestamp": timestamp, "id": id, "input": sentences})

    payload_json = {
        "jsonrpc": "2.0",
        "method": "LMT_handle_jobs",
        "params": {
            "jobs": gen_jobs(sentences),
            "lang": {
                "preference": {
                    "weight": {},
                    "default": "default"
                },
                "source_lang_computed": "EN",
                "target_lang": "ZH"
            },
            "priority": 1,
            "commonJobParams": {
                "browserType": 1,
                "formality": None
            },
            "timestamp": timestamp
        },
        "id": initId()
    }

    # the payload should be no spaces between keys or values, ref: https://stackoverflow.com/a/16311587/9422455
    payload_dumped = json.dumps(payload_json, separators=(",", ":"))
    payload_to_post = handlePayload(payload_dumped, id)

    sess = requests.Session()
    sess.headers = headers
    # sess.verify = False
    if proxy:
        sess.proxies = {"http": proxy, "https": proxy}

    res = sess.post(URL_DEEPL_TRANSLATE, data=payload_to_post).json()
    if "result" not in res:
        print(f"failed to translate reason: [{res['error']['message']}]")
        err_fn = "error.log"
        err_fp = os.path.join(LOG_PATH, err_fn)
        with open(err_fp, "w") as f:
            json.dump(res, f, ensure_ascii=False, indent=2)
            print(f"the log has been dumped into file://{err_fp}")
        return
    return res
