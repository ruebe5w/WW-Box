from configparser import ConfigParser


class BaseRole:
    """The Parent Role Object"""

    def __init__(self, name: str, gender: str, night_actions, day_actions, death_actions, img: str, scenario: str):
        self.name = name
        self.gender = gender
        self.night_actions = night_actions  # dict
        self.day_actions = day_actions  # dict
        self.death_actions = death_actions  # dict
        self.scenario = scenario

        self.img = img

    def write_to_file(self):
        """Writes a Role to a Config-File"""
        file = ConfigParser()
        file['GENERAL'] = {'name': self.name, 'gender': self.gender, 'img': self.img, 'scenario': self.scenario}
        night_acts = {}
        day_acts = {}
        death_acts = {}

        for action in self.night_actions:
            name = self.night_actions[action]['name']
            night_acts.update({action: name})
        for action in self.day_actions:
            name = self.day_actions[action]['name']
            day_acts.update({action: name})
        for action in self.death_actions:
            name = self.death_actions[action]['name']
            death_acts.update({action: name})

        file['NIGHT_ACTIONS'] = night_acts
        file['DAY_ACTIONS'] = day_acts
        file['DEATH_ACTIONS'] = death_acts

        file_name = self.name + '.ini'
        print('Write to \"' + file_name + '\"')

        with open(file_name, 'w') as f:
            file.write(f)
