from titan.utils.tokenizer import tokenize

from titan.core.intent_map import INTENT_MAP


def detect_intent(command):

    command = command.lower()

    # OPEN
    open_keywords = [
        "open",
        "launch",
        "start"
    ]

    # SEARCH
    search_keywords = [
        "search",
        "find",
        "look up"
    ]

    # CLOSE
    close_keywords = [
        "close",
        "kill",
        "terminate",
        "quit"
    ]

    # -------------------------
    # DETECT OPEN
    # -------------------------

    for word in open_keywords:
        if word in command:
            return "open"

    # -------------------------
    # DETECT SEARCH
    # -------------------------

    for word in search_keywords:
        if word in command:
            return "search"

    # -------------------------
    # DETECT CLOSE
    # -------------------------

    for word in close_keywords:
        if word in command:
            return "close"

    # -------------------------
    # FALLBACK
    # -------------------------

    return "unknown"