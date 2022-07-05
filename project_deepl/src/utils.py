from typing import List

from ds import JobItem


def gen_jobs(sentences: List[str]) -> List[JobItem]:
    jobs = []
    sentences_before = []
    for sentence_i, sentence_text in enumerate(sentences):
        job_item: JobItem = {
            "kind": "default",
            "sentences": [{
                "text": sentence_text,
                "id": sentence_i,
                "prefix": ""
            }],
            "raw_en_context_before": sentences_before,
            "raw_en_context_after": [] if sentence_i == len(sentences) - 1 else [sentences[sentence_i + 1]],
            "preferred_num_beams": 1
        }
        jobs.append(job_item)
    return jobs
