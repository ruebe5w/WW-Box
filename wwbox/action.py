from configparser import ConfigParser
from wwbox.game import Game

class Action:
    """Represents a Action"""

    def __init__(self, id: int, conditions, commands):
        self.id = id
        self.conditions = conditions  # dict
        self.commands = commands
        self.self_players = [] # Array mit den Spielern die die Action executen

    def write_to_file(self):
        """Writes a Action to a Config-File"""
        file = ConfigParser()
        file['GENERAL'] = {'name': self.name, 'id': self.id, 'audio': self.audio}
        condition_arr = {}

        # for key in self.conditions.keys():
        #    name = self.conditions[key]['name']
        #    condition_arr.update({key: self.conditions[key]})

        condition_arr = self.conditions

        file['CONDITIONS'] = condition_arr
        file['METHOD'] = str(self.method)
        file_name = '../actions' + self.name + '.ini'
        print('Write to \"' + file_name + '\"')

        with open(file_name, 'w') as f:
            file.write(f)

    def testConditions(self,conditions):
        for c in conditions:
            if self.testCondition(c) == False:
                return False

        return True

    def testCondition(self,condition):
        v1 = self.getValue(condition[0])
        v2 = self.getValue(condition[2])
        if condition[1] == "=":
            return v1 == v2
        if condition[1] == "has":
            return v2 in v1

    def getValue(self,valueKey):
        type = valueKey["type"]
        if type == "e":
            return self.getEffect(valueKey["data"])
        if type == "p":
            return self.getPlayer(valueKey["data"])
        if type == "s":
            return valueKey["data"]
        if type == "b":
            return bool(valueKey["data"])
        if type == "i":
            return int(valueKey["data"])

    def getEffect(self,effectKey):
        player = self.getPlayer(effectKey["player"])
        effectName = effectKey["effectname"]
        return game.get_player(player).effects[effectName]

    def getPlayer(self,playerKey):
        getter = playerKey["getter"]
        if "data" in playerKey:
            data = playerKey["data"]
        oo = False
        if "onlyone" in playerKey:
            oo = playerKey["onlyone"]

        if getter == "self":
            return self.self_players
        if getter == "saved":
            return game.saved_players
        if getter == "all":
            return range(0,len(game.players))
        if getter == "poll":
            return game.get_player_by_poll(self.getPlayer(data["targets"]), self.getPlayer(data["players"]), self.getValue(data["txt"]))
        if getter == "effect":
            if data["operator"] == "exists":
                return game.get_players_by_effect(data["effectname"])
            if data["operator"] == "has":
                return game.get_players_by_effect_has(data["effectname"], getValue(data["value"]))
            if data["operator"] == "equals":
                return game.get_players_by_effect_equals(data["effectname"], getValue(data["value"]))
        if getter == "team":
            return game.get_player_by_team(data)
        if getter == "role":
            return game.get_player_bx_role(data)
        if getter == "status":
            return game.get_player_by_status(data)
        return 0

    def executeCommands(self,commands):
        for c in commands:
            self.executeCommand(c)

    def executeCommand(self,command):
        id = command["id"]
        attributes = []
        for v in command["attributes"]:
            attributes.append(self.getValue(v))
        game.command_switch(id, attributes)

    def executeAction(self,self_players):
        self.self_players = self_players
        if self.testCondition(self.conditions):
            self.executeCommands(self.commands)
