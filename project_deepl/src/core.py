"""
tks to: [DeepL Api 设计中的欺骗战术 - zu1k](https://zu1k.com/posts/thinking/deception-tactics-in-deepl-api-design/)

multi sentences payload:

{
        "jsonrpc": "2.0",
        "method": "LMT_handle_jobs",
        "params": {
            "jobs": [
                {
                    "kind": "default",
                    "sentences": [{
                        "text": "The Robust Visual Inertial Odometry (ROVIO) algorithm [69] is another ﬁlter-based method that uses the EKF approach, and similar to other ﬁlter-based methods, it uses the IMU data to state propagation, and the camera data to ﬁlter update.",
                        "id": 0,
                        "prefix": ""
                    }],
                    "raw_en_context_before": [],
                    "raw_en_context_after": [
                        "However, besides per- forming the feature extraction, ROVIO executes the extraction of multi-level patches around the features, as illustrated by Figure 15."],
                    "preferred_num_beams": 1
                }, {
                    "kind": "default",
                    "sentences": [{
                        "text": "However, besides per- forming the feature extraction, ROVIO executes the extraction of multi-level patches around the features, as illustrated by Figure 15.",
                        "id": 1,
                        "prefix": ""
                    }],
                    "raw_en_context_before": [
                        "The Robust Visual Inertial Odometry (ROVIO) algorithm [69] is another ﬁlter-based method that uses the EKF approach, and similar to other ﬁlter-based methods, it uses the IMU data to state propagation, and the camera data to ﬁlter update."],
                    "raw_en_context_after": [
                        "The patches are used by the prediction and update step to obtain the innovation term, i.payload_dumped., the calculation of the error between the frame and the projection of the multi-level patch into the frame."],
                    "preferred_num_beams": 1
                }, {
                    "kind": "default",
                    "sentences": [{
                        "text": "The patches are used by the prediction and update step to obtain the innovation term, i.payload_dumped., the calculation of the error between the frame and the projection of the multi-level patch into the frame.",
                        "id": 2,
                        "prefix": ""
                    }],
                    "raw_en_context_before": [
                        "The Robust Visual Inertial Odometry (ROVIO) algorithm [69] is another ﬁlter-based method that uses the EKF approach, and similar to other ﬁlter-based methods, it uses the IMU data to state propagation, and the camera data to ﬁlter update.",
                        "However, besides per- forming the feature extraction, ROVIO executes the extraction of multi-level patches around the features, as illustrated by Figure 15."],
                    "raw_en_context_after": [
                        "The ROVIO algorithm achieves good accuracy and robustness under a low resource utilization [18,65], being suitable for embedded implementations [65]."],
                    "preferred_num_beams": 1
                }, {
                    "kind": "default",
                    "sentences": [{
                        "text": "The ROVIO algorithm achieves good accuracy and robustness under a low resource utilization [18,65], being suitable for embedded implementations [65].",
                        "id": 3,
                        "prefix": ""
                    }],
                    "raw_en_context_before": [
                        "The Robust Visual Inertial Odometry (ROVIO) algorithm [69] is another ﬁlter-based method that uses the EKF approach, and similar to other ﬁlter-based methods, it uses the IMU data to state propagation, and the camera data to ﬁlter update.",
                        "However, besides per- forming the feature extraction, ROVIO executes the extraction of multi-level patches around the features, as illustrated by Figure 15.",
                        "The patches are used by the prediction and update step to obtain the innovation term, i.payload_dumped., the calculation of the error between the frame and the projection of the multi-level patch into the frame."],
                    "raw_en_context_after": [
                        "However, the algorithm proved to be more sensitive to per-frame processing time [65] and less accurate than other algorithms, such as VI-DSO [70]."],
                    "preferred_num_beams": 1
                }, {
                    "kind": "default",
                    "sentences": [{
                        "text": "However, the algorithm proved to be more sensitive to per-frame processing time [65] and less accurate than other algorithms, such as VI-DSO [70].",
                        "id": 4,
                        "prefix": ""
                    }],
                    "raw_en_context_before": [
                        "The Robust Visual Inertial Odometry (ROVIO) algorithm [69] is another ﬁlter-based method that uses the EKF approach, and similar to other ﬁlter-based methods, it uses the IMU data to state propagation, and the camera data to ﬁlter update.",
                        "However, besides per- forming the feature extraction, ROVIO executes the extraction of multi-level patches around the features, as illustrated by Figure 15.",
                        "The patches are used by the prediction and update step to obtain the innovation term, i.payload_dumped., the calculation of the error between the frame and the projection of the multi-level patch into the frame.",
                        "The ROVIO algorithm achieves good accuracy and robustness under a low resource utilization [18,65], being suitable for embedded implementations [65]."],
                    "raw_en_context_after": ["o"],
                    "preferred_num_beams": 1
                }, {
                    "kind": "default",
                    "sentences": [{
                        "text": "o",
                        "id": 5,
                        "prefix": ""
                    }],
                    "raw_en_context_before": [
                        "The Robust Visual Inertial Odometry (ROVIO) algorithm [69] is another ﬁlter-based method that uses the EKF approach, and similar to other ﬁlter-based methods, it uses the IMU data to state propagation, and the camera data to ﬁlter update.",
                        "However, besides per- forming the feature extraction, ROVIO executes the extraction of multi-level patches around the features, as illustrated by Figure 15.",
                        "The patches are used by the prediction and update step to obtain the innovation term, i.payload_dumped., the calculation of the error between the frame and the projection of the multi-level patch into the frame.",
                        "The ROVIO algorithm achieves good accuracy and robustness under a low resource utilization [18,65], being suitable for embedded implementations [65].",
                        "However, the algorithm proved to be more sensitive to per-frame processing time [65] and less accurate than other algorithms, such as VI-DSO [70]."],
                    "raw_en_context_after": [],
                    "preferred_num_beams": 1
                }],
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
            "timestamp": 1657014549082
        },
        "id": 59710004
    }
"""

import json
import os
import time
from typing import Optional, List

import requests

from algo import handlePayload, initId
from const import URL_DEEPL_TRANSLATE, headers, LOG_PATH
from utils import gen_jobs


def callTranslationViaDeepL(to_translate: str, proxy: str = None) -> Optional[dict]:
    """

    :param to_translate:
    :return:
        sample return when to_translate == "are you ok" @ 2022/07/05:
        {'jsonrpc': '2.0', 'id': 69910001, 'result': {'translations': [{'beams': [{'sentences': [{'text': '你还好吗？', 'ids': [0]}], 'num_symbols': 6}, {'sentences': [{'text': '你还好吗', 'ids': [0]}], 'num_symbols': 5}, {'': [{'text': '你还好吗?', 'ids': [0]}], 'num_symbols': 6}, {'sentences': [{'text': '你没事吧？', 'ids': [0]}], 'num_symbols': 6}], 'quality': 'normal'}], 'target_lang': 'ZH', 'source_lang': 'EN', 'source_lang_is_confalse, 'detectedLanguages': {'EN': 0.063362, 'DE': 0.002077, 'FR': 0.025998, 'ES': 0.011035, 'PT': 0.005216, 'IT': 0.0055969999999999995, 'NL': 0.021662, 'PL': 0.007718, 'RU': 0.0019399999999999999, 'ZH': 0.0033729999999999997, 'JA': 0.0005009999999999999, 'BG': 0.0008179999999999999, 'CS': 0.051376, 'DA': 0.004497999999999999, 'EL': 0.001078, 'ET': 0.013248, 'FI': 0.0014759999999999999, 'HU': 0.0014269999999999999, 'LT': 0.004829, 'LV': 0.002709, 'RO': 0.00481, 'SK': 0.006817999999999999, 'SL': 0.001738, 'SV': 0.011986, 'TR': 0.058573999999999994, 'ID': 0.010589999999999999, 'unsupported': 0.675547}}}
    """
    if not to_translate:
        print("DENIED since your input is blank")
        return

    sentences = [i for i in to_translate.split(".") if i]

    def initTimestampFromSentences(sentences: List[str]):
        r = int(time.time() * 1000)
        n = 1
        for sentence in sentences:
            for char in sentence:
                if char == 'i':
                    n += 1
        timestamp = r + (n - r % n)
        return timestamp

    timestamp = initTimestampFromSentences(sentences)
    id = initId()
    # print({"timestamp": timestamp, "id": id})

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
