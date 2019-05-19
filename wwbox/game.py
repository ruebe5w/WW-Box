from wwbox.player import Player
from wwbox.baserole import BaseRole


class Game:
    def __init__(self, id=0):
        self.id = id
        self.players = []
        self.roles = []

    def new_player(self, name: str, id: int):
        self.players[id] = Player(name, id)

    def get_player(self, id):
        return self.players[id]

    def add_role(self, name: str,  gender: str, actions: [], img: str):
        self.roles[name] = BaseRole(name, gender, actions, img)

    def get_role(self, id):
        return self.roles[id]
