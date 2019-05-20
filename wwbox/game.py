from wwbox.player import Player
from wwbox.baserole import BaseRole


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

    def add_role(self, name: str, gender: str, night_actions, day_actions, death_actions, img: str):
        """Adds a role Object to Game"""
        self.roles[name] = BaseRole(name, gender, night_actions, day_actions, death_actions, img)

    def get_role(self, id):
        """Get Role Object from ID"""
        return self.roles[id]