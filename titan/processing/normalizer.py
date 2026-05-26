from titan.core.alias_map import ALIAS_MAP


FILLER_WORDS = [
    "can",
    "you",
    "please",
    "i",
    "want",
    "to",
    "the"
]


def normalize_command(command):

    words = command.lower().split()

    cleaned_words = []

    for word in words:

        if word in ALIAS_MAP:
            word = ALIAS_MAP[word]

        if word not in FILLER_WORDS:
            cleaned_words.append(word)

    return " ".join(cleaned_words)