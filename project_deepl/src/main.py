from core import callTranslationViaDeepL

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
    args.add_argument("-p", "--proxy", help="add proxy, which is very important for continuously usage")
    parser = args.parse_args()

    result = callTranslationViaDeepL(parser.to_translate)
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
