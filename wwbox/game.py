from wwbox.importation import *
from wwbox.player import Player
import random


class Game:
    """Represents a Game/a Round"""

    def __init__(self, id=0, status=0):
        self.id = id
        self.scenario = Scenario()
        self.status = status
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

    def start(self, scenario_name):
        print('Ein neues Spiel wird gestartet!')
        self.status = 1
        print('Scenario \"' + scenario_name + '\" wird geladen...')
        scenarios = import_scenario()
        self.scenario = scenarios[scenario_name]
        self.__role_assignment()
        self.play_audio(self.scenario.story_audio)

    def __role_assignment(self):
        player_count = len(self.players)
        counts = self.scenario.calculate_role_count(player_count)
        player_id_array = []
        for player_id in self.players:
            player_id_array.append(player_id)
        random.shuffle(player_id_array)
        i = 0
        for key in counts.keys():
            self.roles.update({key: self.scenario.roles[key]})
            player = self.players[player_id_array[i]]
            player.set_primary_role(self.roles[key])
            role_gedöns = ""  # TODO Send Players Role
            self.send_gui(player, role_gedöns)  # TODO

    def send_gui(self, player, gui_commands):
        print()
        # TODO send information to players

    def play_audio(self, audio_file):
        print()
        # TODO play_audio
