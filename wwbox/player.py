class Player:
    def __init__(self, name: str, id: int):
        self.name = name
        self.id = id
        self.status = 1
        self.can_vote = True
        self.can_speak = True
        self.effects = []
        self.roles = []

    def add_effect(self, key: str, value):
        self.effects[key] = value

    def get_effects(self, key: str):
        return self.effects[key]

    def is_effected(self, effect):
        return effect in self.effects

    def append_secondary_role(self, role):
        if role not in self.roles:
            self.roles.append(role)

    def set_primary_role(self, role):
        if role not in self.roles:
            self.roles = [role] + self.roles
        else:
            self.roles.remove(role)
            self.roles = [role] + self.roles

    def del_role(self, role):
        if role in self.roles:
            self.roles.remove(role)
