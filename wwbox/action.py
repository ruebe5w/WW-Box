from configparser import ConfigParser
from wwbox.game import Game

class Action:
    """Represents a Action"""

    def __init__(self, name: str, id: int, conditions, method, audio=""):
        self.name = name
        self.id = id
        self.conditions = conditions  # dict
        self.method = method
        self.audio = audio

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
