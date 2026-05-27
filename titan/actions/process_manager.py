import psutil

PROCESS_ALIASES = {

    "edge": "msedge",
    "browser": "msedge",

    "chrome": "chrome",

    "calculator": "calc",
    "calc": "calc",

    "vscode": "code",
    "code": "code",

    "discord": "discord",
    "steam": "steam"
}


def close_app(target: str) -> bool:

    target = target.lower().strip()
    target = PROCESS_ALIASES.get(target, target)

    for process in psutil.process_iter(["name"]):

        try:
            process_name = process.info["name"]

            if not process_name:
                continue

            process_name = process_name.lower()

            # Remove .exe
            clean_name = process_name.replace(".exe", "")

            # STRICT MATCH
            if clean_name == target:

                process.terminate()

                return True

        except:
            continue

    return False