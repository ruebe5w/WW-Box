from wwbox.importation import *
from wwbox.player import Player
import random
from wwbox.tools import *
from wwbox.scenario import Scenario
import time
import operator


class Game:
    """Represents a Game/a Round"""

    def __init__(self, id=0, status=0):
        self.id = id
        # declare self.scenario
        self.status = status
        self.players = {}
        self.roles = {}
        self.actions = {}
        self.order = {}

    def new_player(self, name: str, id: str):
        """Adds a new player Object to Game"""
        self.players[id] = Player(name, id)

    def get_player_by_id(self, id):
        """Get Player Object from ID"""
        return self.players[id]

    def get_players_by_role(self, role):
        player_id_array = []
        for player_key in self.players.keys():
            if role in self.players[player_key].roles:
                player_id_array.append(player_key)

    def get_player_by_effect(self, effect):
        player_id_array = []
        for player_key in self.players.keys():
            if self.players[player_key].is_effected(effect):
                player_id_array.append(player_key)

    def get_player_by_team(self, team):
        player_id_array = []
        for player_key in self.players.keys():
            if team == self.players[player_key].team:
                player_id_array.append(player_key)

    def get_player_by_status(self, status):
        player_id_array = []
        for player_key in self.players.keys():
            if status == self.players[player_key].status:
                player_id_array.append(player_key)

    def add_role(self, name: str, gender: str, toa: int, team: str, night_actions, day_actions, on_attack_actions,
                 death_actions,
                 img: str,
                 scenario: str):
        """Adds a role Object to Game"""
        self.roles[name] = Role(name, gender, toa, team, night_actions, day_actions, on_attack_actions, death_actions,
                                img, scenario)

    def get_role(self, id):
        """Get Role Object from ID"""
        return self.roles[id]

    def import_roles(self):
        self.roles.update(import_roles())

    def start(self, scenario_name):
        """Starts a Game"""
        print('Ein neues Spiel wird gestartet!')
        self.status = 1
        print('Scenario \"' + scenario_name + '\" wird geladen...')
        scenarios = import_scenario()
        self.scenario = scenarios[scenario_name]
        self._role_assignment()
        self.generate_order()
        play_audio(self.scenario.audios['story_audio'])
        self.game_routine()

    def game_routine(self):

        def night():
            nonlocal first_night
            if first_night:
                print()
                _night_wakeup(1)
                first_night = False
            _night_wakeup(2)
            _night_wakeup(3)
            _night_wakeup(4)

        def _night_wakeup(cat):
            for role in self.order[cat]:
                role.wake_up()

        def day():

            play_audio(self.scenario.audios['town_awake'])

            set_announce_deaths()
            # Diskussion

            for key in self.players.keys():
                if self.players[key].status != 0:
                    set_gui(self.players[key].id, base='poll', txt1={'text': 'Wen möchtet ihr umbringen?'},
                            lvPoll={'list': self.get_player_names()})
            play_audio(self.scenario.audios['discuss_start'])
            time.sleep(self.scenario.discussion_time / 2)
            play_audio(self.scenario.audios['discuss_half_time'])
            time.sleep(self.scenario.discussion_time / 2)
            play_audio(self.scenario.audios['discuss_end'])

            # Abstimmung auswerten
            self.players[self.evaluate_voting()].status = 1

            set_announce_deaths()

            play_audio(self.scenario.audios['town_sleep'])

        def set_announce_deaths():
            for player in self.players:
                if player.status == 1:
                    for role_name in player.roles:
                        for action_name in self.roles[role_name].on_attack_actions:
                            self.actions[action_name].run(player)
                    if player.status == 1:
                        # play_audio(self.scenario.audios['player_death'])
                        self.direct_kill(player.id)

                    else:
                        player.status = 2

        first_night = True
        # 0R (Bürgermeister)
        play_audio(self.scenario.audios['town_sleep'])
        night()
        while not self._is_won():
            day()
            night()
        set_announce_deaths()

        # Gewinner verkünden
        # Neustarten

    def _is_won(self):
        team_array = []
        for player_key in self.players.keys():
            if self.players[player_key].status > 0:
                team_array.append(self.players[player_key].team)
        if len(team_array) == 1:
            return True
        else:
            return False

        bol = False
        return bol

    def evaluate_voting(self):
        poll_dict = {}
        for ip in instance_dict.keys():
            if 'poll' in instance_dict[ip]:
                if instance_dict[ip]['poll'] in poll_dict:
                    old = poll_dict[instance_dict[ip]['poll']]
                    poll_dict.update({instance_dict[ip]['poll']: old + 1})
                else:
                    poll_dict.update({instance_dict[ip]['poll']: 1})
        # Count votes:
        return max(poll_dict.keys(), key=lambda k: poll_dict[k])  # TODO max vote

    def get_player_names(self):
        player_names = {}
        for key in self.players.keys():
            player_names.update({key: self.players[key].name})
        return player_names

    def direct_kill(self, player_id):
        player = self.roles[player_id]
        for role_name in player.roles:
            for action_name in self.roles[role_name].death_actions:
                self.actions[action_name].run(player)
        player.status = 0
        player.can_speak = False
        player.can_vote = False

    def _role_assignment(self):
        print('Rollen werden zugeteilt...')
        player_count = len(self.players)
        counts = self.scenario.calculate_role_count(player_count)
        player_id_array = []
        for player_id in self.players:
            player_id_array.append(player_id)
        random.shuffle(player_id_array)
        i = 0
        print(counts)
        for key in counts.keys():
            self.roles.update({key: self.scenario.roles[key]})
            player = self.players[player_id_array[i]]
            player.set_primary_role(self.roles[key])
            text = "Herzlich Willkommen in " + self.scenario.name + '! Du bist in diesem Spiel\n' + player.roles[1].name
            img = player.roles[1].name + '.png'
            set_gui(player.id, base='info', txt1=text, imgPicture=img)
            print(instance_dict)
            i += 1

    def generate_order(self):

        """Generates the order of toa"""

        order = {'0R': {}, '1R': {}, 'PR': {}, 'KR': {}, 'AR': {}}
        role_counts = self.scenario.calculate_role_count(len(self.players))

        def if_role_in_cat(role, role_cat):
            if role.toa == role_cat:
                order[role_cat].update({role.name: role_counts[role.name]})

        for role in self.roles:
            if_role_in_cat(role, '0R')
            if_role_in_cat(role, '1R')
            if_role_in_cat(role, 'PR')
            if_role_in_cat(role, 'KR')
            if_role_in_cat(role, 'AR')
        self.order = order

    def command_switch(self, command: str, *args):

        if command == 'ps' or command == 'playsound':
            play_audio(args[0])
        if command == 'dk':
            self.direct_kill(args[0])
        if command == 'ae':
            self.players[args[0]].add_effect(args[1], args[2])
        if command == 'rme':
            self.players[args[0]].remove_effect(args[1])
        if command == 'ate':
            self.players[args[0]].append_to_effect(args[1], args[2], args[3])
        if command == 'si':
            if 2 in args:
                send_info(args[0], args[1], args[2])
            else:
                send_info(args[0], args[1])
