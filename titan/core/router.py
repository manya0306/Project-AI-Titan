from titan.handlers.search_handler import handle_search
from titan.handlers.open_handler import handle_open
from titan.core.command_registry import COMMANDS
from titan.handlers.close_handler import handle_close

def route_command(intent, command, tokens):

    # -------------------------
    # 1. INTENT LAYER (PRIMARY)
    # -------------------------
    
    if intent == "search":
        return handle_search(command)

    if intent == "open":
        return handle_open(command)
    
    if intent == "close":
        return handle_close(command)

    # -------------------------
    # 2. TIME / DATE INTENTS (if you have them)
    # -------------------------
    if intent == "time":
        return COMMANDS["time"]["action"]()

    if intent == "date":
        return COMMANDS["date"]["action"]()

    # -------------------------
    # 3. COMMAND REGISTRY (FALLBACK)
    # -------------------------
    for trigger, data in COMMANDS.items():

        if trigger in tokens:

            result = data["action"]()

            if data.get("response"):
                return data["response"]

            return result

    # -------------------------
    # 4. NOTHING MATCHED
    # -------------------------
    return None