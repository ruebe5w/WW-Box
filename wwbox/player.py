class Player:
    """Represents a Player/a Client"""

    def __init__(self, name: str, id: str):
        self.name = name
        self.id = id
        self.status = 2  # 2=alive, 1=attacked, 0=death
        self.can_vote = True
        self.can_speak = True
        self.effects = {}
        self.roles = []  # Array, just role names

    def add_effect(self, key: str, value):
        """Adds an Effect to a Player"""
        self.effects[key] = value

    def remove_effect(self, key: str):
        """Removes an Effect from a Player"""
        self.effects.pop(key, None)

    def append_to_effect(self, effect, key, value):
        """Append an Key-Value-Pair to an Effect."""
        self.effects[effect].update({key: value})

    def get_effect(self, key: str):
        """Gets the Value of a Players Effect. Return False if Player has no effect with passed key."""
        if self.is_effected(key):
            return self.effects[key]
        else:
            return False

    def is_effected(self, effect):
        """Return bol if Player has effect."""
        return effect in self.effects

    def append_secondary_role(self, role):
        """Appends a secondary Role to Players Roles."""
        if role not in self.roles:
            self.roles.append(role)

    def set_primary_role(self, role):
        """Set Players primary role. Other Roles slip backwards."""
        if role not in self.roles:
            self.roles = [role] + self.roles
        else:
            self.roles.remove(role)
            self.roles = [role] + self.roles

    def del_role(self, role):
        """Deletes a Role from Players-Roles."""
        if role in self.roles:
            self.roles.remove(role)
