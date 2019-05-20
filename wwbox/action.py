from wwbox.player import Player


class Action:
    """Represents a Action"""

    def __init__(self, name: str, id: int, kind: str, conditions, target: Player):
        self.name = name
        self.id = id
        self.kind = kind
        self.conditions = conditions  # dict
        self.target = target
