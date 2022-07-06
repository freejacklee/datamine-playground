from typing import get_args
from core import callTranslationViaDeepL
from const import Langs

if __name__ == '__main__':
    import argparse

    args = argparse.ArgumentParser(
        description="""deepl api (unofficial)
    currently supported:
        - [√] english -> chinese 
        - [x] chinese -> english, it is on the agenda if I have time :)

    examples:
        [attention] you should use QUOTES to wrap all your words to translate
        1. return plain text:
            python main.py "are you ok"

        2. return json (with more info)
            python main.py "are you ok" -f json
        """,
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    args.add_argument("to_translate", help="words to translate")
    args.add_argument("-f", "--format", help="return format, json(full) or plain(direct result)",
                      choices=["json", "plain"], default="plain")
    args.add_argument("--target_lang", help="target lang",
                      default="ZH", choices=Langs)
    args.add_argument("--from_lang", help="from lang",
                      default="EN", choices=Langs)
    args.add_argument(
        "--terminology", help="terminology mapping, any lines like 'KEY\tVAR' or a file", default="")
    args.add_argument(
        "-p", "--proxy", help="add proxy, which is very important for continuously usage")
    parser = args.parse_args()

    assert parser.from_lang in Langs, f"from_lang {parser.from_lang} not supported, valid are: {Langs}"
    assert parser.target_lang in Langs, f"to_lang {parser.target_lang} not supported, valid are: {Langs}"

    # 如果为空，则保持默认；如果有"\t"说明是文本内容，则直接读取
    if not parser.terminology or "\t" in parser.terminology or "\\t" in parser.terminology:
        terminology = parser.terminology
    # 如果没有"\t"，则说明是文本，则读取
    else:
        with open(parser.terminology) as f:
            terminology = f.read().strip()
    # 统一
    terminology = terminology.replace("\\t", "\t")

    result = callTranslationViaDeepL(
        parser.to_translate,
        target_lang=parser.target_lang,
        from_lang=parser.from_lang,
        terminology=terminology
    )
    if not result:
        print("ABORT!")
        exit(-1)

    if parser.format == "json":
        output = result
    else:
        output = ""
        for translation in result["result"]["translations"]:
            for beam in translation["beams"]:
                for sentence in beam["sentences"]:
                    output += sentence["text"]

    print(output)
