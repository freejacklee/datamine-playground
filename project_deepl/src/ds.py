from typing import Literal, TypedDict, List


class SentenceItem(TypedDict):
    text: str
    id: int
    prefix: str


class JobItem(TypedDict):
    kind: str
    sentences: List[SentenceItem]
    raw_en_context_before: List[str]
    raw_en_context_after: List[str]
    preferred_num_beams: int


class PayloadParam(TypedDict):
            jobs: List[JobItem]
            lang: dict  # todo
            priority: int #有时是1，有时是-1
            commonJobParams: dict # todo
            timestamp: int

class Payload(TypedDict):
        jsonrpc: str  # version
        method: str # our api: "LMT_handle_jobs",
        params:PayloadParam
        id: int