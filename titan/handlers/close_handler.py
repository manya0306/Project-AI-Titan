from titan.processing.command_parser import extract_open_target

from titan.actions.process_manager import close_app


def handle_close(command):

    target = extract_open_target(command)

    success = close_app(target)

    if success:
        return f"Closed {target}"

    return f"I couldn't find {target} running."