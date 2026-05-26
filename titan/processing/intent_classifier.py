def classify_intent(command: str):

    command = command.lower()

    if any(word in command for word in ["open", "launch", "start"]):
        return "open_app"

    if "search" in command or "find" in command:
        return "search_web"

    if "time" in command:
        return "get_time"

    if "date" in command:
        return "get_date"

    return "unknown"