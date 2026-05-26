SYNONYMS = {

    "browser": "edge",
    "google chrome": "edge",
    "code editor": "code",
    "editor": "code",

    "music": "spotify",
    "songs": "spotify",

    "youtube": "youtube",
    "google": "google",

    "calculator": "calculator"
}


def resolve_entity(command: str):

    command = command.lower()

    for key, value in SYNONYMS.items():

        if key in command:
            return command.replace(key, value)

    return command