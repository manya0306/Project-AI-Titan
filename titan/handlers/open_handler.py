from titan.processing.command_parser import extract_open_target

from titan.core.app_map import APP_MAPPINGS

from titan.actions.system_actions import open_target

from titan.utils.fuzzy_matcher import get_best_match


def handle_open(command):

    target = extract_open_target(command).strip()

    # 1. FIRST: exact match
    if target in APP_MAPPINGS:
        success = open_target(APP_MAPPINGS[target])
        if success:
            return f"Opening {target}"

    # 2. SECOND: fuzzy correction BEFORE execution
    suggestion = get_best_match(target)

    if suggestion and suggestion != target:

        # auto-correct instead of asking only
        if suggestion in APP_MAPPINGS:

            success = open_target(APP_MAPPINGS[suggestion])

            if success:
                return f"Did you mean '{suggestion}'? Opening it."

        return {"suggestion": f"open {suggestion}"}

    # 3. THIRD: direct attempt (optional fallback)
    success = open_target(target)

    if success:
        return f"Opening {target}"

    return f"I don't know how to open {target} yet."