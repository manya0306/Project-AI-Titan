from titan.processing.command_parser import extract_search_query
from titan.actions.system_actions import google_search


def handle_search(command):

    query = extract_search_query(command)

    google_search(query)

    return f"Searching Google for {query}"