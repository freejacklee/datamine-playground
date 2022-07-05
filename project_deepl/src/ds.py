from typing import TypedDict, List


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