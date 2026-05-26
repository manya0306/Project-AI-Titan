from difflib import get_close_matches

from titan.core.app_map import APP_MAPPINGS
from titan.core.command_registry import COMMANDS


def get_best_match(word):

    known_words = list(APP_MAPPINGS.keys()) + list(COMMANDS.keys())

    matches = get_close_matches(
        word,
        known_words,
        n=1,
        cutoff=0.6
    )

    if matches:
        return matches[0]

    return None