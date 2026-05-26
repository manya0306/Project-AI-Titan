from titan.utils.tokenizer import tokenize

from titan.core.intent_map import INTENT_MAP


def detect_intent(command: str):

    command = command.lower()

    if "open" in command:
        return "open"

    if "search" in command or "google" in command:
        return "search"

    if "time" in command or "what is the time" in command:
        return "time"

    if "date" in command:
        return "date"

    return "unknown"