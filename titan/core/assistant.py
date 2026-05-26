from titan.processing.normalizer import normalize_command
from titan.processing.intent_detector import detect_intent

from titan.utils.tokenizer import tokenize
from titan.utils.fuzzy_matcher import get_best_match

from titan.core.router import route_command
from titan.core.memory import TitanMemory

from titan.core.llm import ask_llm


class TitanAssistant:

    def __init__(self):
        self.pending_command = None
        self.memory = TitanMemory()

    # -------------------------
    # MEMORY RESOLUTION LAYER
    # -------------------------
    def resolve_memory_reference(self, command):

        command = command.lower()

        words = command.split()

        # case: "it", "that", "this"
        if command in ["it", "that", "this"]:

            if self.memory.last_app:
                return f"open {self.memory.last_app}"

            if self.memory.last_query:
                return f"search {self.memory.last_query}"

        # case: "open it", "launch it"
        if len(words) == 2 and words[1] in ["it", "that", "this"]:

            if self.memory.last_app:
                return f"{words[0]} {self.memory.last_app}"

        return command

    # -------------------------
    # MAIN PROCESS PIPELINE
    # -------------------------
    def process_command(self, command):

        # 1. NORMALIZATION
        command = normalize_command(command)

        # 2. MEMORY RESOLUTION (IMPORTANT FIX)
        command = self.resolve_memory_reference(command)

        # 3. TOKENIZATION
        tokens = tokenize(command)

        # 4. EXIT CONDITION
        if command == "exit":
            return "Shutting down Titan"

        # -------------------------
        # 5. CONFIRMATION SYSTEM
        # -------------------------
        if self.pending_command:

            if command in ["yes", "yeah", "y"]:
                corrected_command = self.pending_command
                self.pending_command = None
                return self.process_command(corrected_command)

            elif command in ["no", "nope", "n"]:
                self.pending_command = None
                return "Okay."

        # -------------------------
        # 6. INTENT DETECTION
        # -------------------------
        intent = detect_intent(command)

        # -------------------------
        # 7. ROUTER EXECUTION
        # -------------------------
        result = route_command(intent, command, tokens)

        if result:

            # suggestion handling from router
            if isinstance(result, dict) and "suggestion" in result:

                suggested_command = result["suggestion"]
                self.pending_command = suggested_command

                return f"Did you mean '{suggested_command}'?"

            # update memory based on intent
            if intent == "open":
                self.memory.last_app = command.replace("open", "").strip()

            elif intent == "search":
                self.memory.last_query = command.replace("search", "").strip()

            self.memory.last_intent = intent

            return result

        # -------------------------
        # 8. FUZZY FALLBACK
        # -------------------------
        for token in tokens:

            suggestion = get_best_match(token)

            if suggestion:

                self.pending_command = suggestion
                return f"Did you mean '{suggestion}'?"

        # -------------------------
        # 9. LLM FALLBACK (BRAIN LAYER)
        # -------------------------
        return ask_llm(command)