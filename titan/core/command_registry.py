from titan.actions.system_actions import get_time, get_date


COMMANDS = {

    "time": {
        "action": get_time,
        "response": None
    },

    "date": {
        "action": get_date,
        "response": None
    }
}