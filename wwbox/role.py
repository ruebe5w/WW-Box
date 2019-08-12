from configparser import ConfigParser


class Role:
    """The Parent Role Object"""

    def __init__(self, name: str, gender: str, toa: int, team: str, night_actions, day_actions, on_attack_actions,
                 death_actions,
                 img: str,
                 scenario: str):
        self.name = name
        self.gender = gender
        self.toa = toa  # time of awakening 0:0R, 1:1R, 2:PR,3:KR,4:AR
        self.team = team
        self.night_actions = night_actions  # dict
        self.day_actions = day_actions  # dict
        self.on_attack_actions = on_attack_actions  # dict
        self.death_actions = death_actions  # dict
        self.scenario = scenario
        self.img = img
        self.write_to_file()

    def write_to_file(self):
        """Writes a Role to a Config-File"""
        file = ConfigParser(allow_no_value=True)
        file['GENERAL'] = {'name': self.name, 'gender': self.gender, 'toa': self.toa, 'team': self.team,
                           'img': self.img,
                           'scenario': self.scenario}
        night_acts = {}
        day_acts = {}
        on_attack_acts = {}
        death_acts = {}

        for action in self.night_actions:
            night_acts.update({action})
        for action in self.day_actions:
            day_acts.update({action})
        for action in self.on_attack_actions:
            on_attack_acts.update({action})
        for action in self.death_actions:
            death_acts.update({action})
        file['NIGHT_ACTIONS'] = night_acts
        file['DAY_ACTIONS'] = day_acts
        file['ON_ATTACK_ACTIONS'] = on_attack_acts
        file['DEATH_ACTIONS'] = death_acts

        file_name = self.name + '.ini'
        print('Write to \"' + file_name + '\"')

        with open(file_name, 'w') as f:
            file.write(f)

    def wake_up(self):
        """Triggers the Night-Actions of the Role."""
        print()
        # TODO role wake_up
