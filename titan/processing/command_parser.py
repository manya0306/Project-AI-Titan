import re

def extract_open_target(command):

    command = command.lower()

    # remove trigger words cleanly
    command = re.sub(r"\b(open|launch|start|close|kill|terminate|quit)\b", "", command)

    # normalize ALL whitespace
    command = " ".join(command.split())

    return command


def extract_search_query(command):

    trigger_words = [
        "search",
        "find",
        "look up"
    ]

    for trigger in trigger_words:

        if trigger in command:

            return command.replace(trigger, "").strip()

    return None