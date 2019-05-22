from wwbox.player import Player
from wwbox.role import Role
from wwbox.importation import import_roles


class Game:
    """Represents a Game/a Round"""

    def __init__(self, id=0):
        self.id = id
        self.players = {}
        self.roles = {}
        self.actions = {}

    def new_player(self, name: str, id: int):
        """Adds a new player Object to Game"""
        self.players[id] = Player(name, id)

    def get_player(self, id):
        """Get Player Object from ID"""
        return self.players[id]

    def add_role(self, name: str, gender: str, toa: int, night_actions, day_actions, death_actions, img: str,
                 scenario: str):
        """Adds a role Object to Game"""
        self.roles[name] = Role(name, gender, toa, night_actions, day_actions, death_actions, img, scenario)

    def get_role(self, id):
        """Get Role Object from ID"""
        return self.roles[id]

    def import_roles(self):
        self.roles.update(import_roles())
