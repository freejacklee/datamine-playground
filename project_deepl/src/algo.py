import random


def handlePayload(payload_dumped: str, id: int):
    """
    ref:
        https://static.deepl.com/js/translator_late.min.$e1ac03.js:formatted:15229
    code:
        f_str: function(e, t) {
            return e.replace('hod":"', (t + 3) % 13 == 0 || (t + 5) % 29 == 0 ? 'hod" : "' : 'hod": "')
        }
    :param payload_dumped:
    :param id:
    :return:
    """
    return payload_dumped.replace('hod":"', 'hod" : "' if (id + 3) % 13 == 0 or (id + 5) % 29 == 0 else 'hod": "')


def initId():
    """
    ref:
        https://static.deepl.com/js/utils.chunk.$5d3184.js:formatted:1508
    :return:
    """
    return int(1e4 * round(1e4 * random.random())) + 1