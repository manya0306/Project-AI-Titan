class TitanMemory:

    def __init__(self):
        self.last_app = None
        self.last_query = None
        self.last_intent = None
        self.last_entity = None

    def update(self, intent=None, app=None, query=None, entity=None):

        if intent:
            self.last_intent = intent

        if app:
            self.last_app = app

        if query:
            self.last_query = query

        if entity:
            self.last_entity = entity