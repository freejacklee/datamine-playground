from curses.ascii import US
from typing import Mapping, Union
import os
from requests.structures import CaseInsensitiveDict


"""
path
"""

SRC_PATH = os.path.dirname(__file__)
PROJECT_PATH = os.path.dirname(SRC_PATH)
LOG_PATH = os.path.join(PROJECT_PATH, "logs")

"""
request
"""
URL_DEEPL_TRANSLATE = 'https://www2.deepl.com/jsonrpc?method=LMT_handle_jobs'

USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"

headers_: Mapping[str, str] = {
    # cookie is not necessary, and put ua here is out of habit
    "User-Agent": USER_AGENT,
    "Content-Type": "application/json"
}

headers = CaseInsensitiveDict()
headers["User-Agent"] = headers_["User-Agent"]
headers["Content-Type"] = headers_["Content-Type"]


"""
validation
"""
LangsSupportTerminology = [
    "EN",
    "JA",
    "DE",
    "FR"
]

Langs = LangsSupportTerminology + [
    "ZH",
]