import os

SRC_PATH = os.path.dirname(__file__)
PROJECT_PATH = os.path.dirname(SRC_PATH)
LOG_PATH = os.path.join(PROJECT_PATH, "logs")

URL_DEEPL_TRANSLATE = 'https://www2.deepl.com/jsonrpc?method=LMT_handle_jobs'

USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"

headers = {
    # cookie is not necessary, and put ua here is out of habit
    "User-Agent": USER_AGENT,
    "Content-Type": "application/json"
}
