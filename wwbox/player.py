class Player:
    def __init__(self, name: str, id: int):
        self.name = name
        self.id = id
        self.status = 1
        self.can_vote = True
        self.can_speak = True
        self.effects = []

    def add_effect(self, key: str, value):
        self.effects[key] = value

    def get_effects(self, key: str):
        return self.effects[key]

    def is_effected(self, effect):
        return effect in self.effects
