from configparser import ConfigParser


class Scenario:
    def __init__(self, name: str, author: str, description: str, story_audio: str, img: str):
        self.name = name
        self.author = author
        self.description = description
        self.roles = {}
        self.story_audio = story_audio
        self.img = img
        self.role_weighting = {}

    def write_to_file(self):
        """Saves Scenario to config"""
        file = ConfigParser(allow_no_value=True)
        file['GENERAL'] = {'name': self.name, 'author': self.author, 'description': self.description,
                           'story_audio': self.story_audio, 'img': self.img}
        role_name_array = {}
        for role in self.roles:
            role_name_array.update({role})
        file['ROLES'] = role_name_array

        file_name = self.name + '.ini'
        print('Write to \"' + file_name + '\"')

        with open(file_name, 'w') as f:
            file.write(f)

    def update_role(self, role, weighting):
        self.roles.update({role.name: role})
        self.role_weighting.update({role.name: weighting})

    def remove_role(self, role_name):
        del self.roles[role_name]
        del self.role_weighting[role_name]

    def calculate_role_count(self, player_count):
        counts = {}
        for role in self.roles.keys():
            print()
            # TODO Rollenanzahl berechnen
            # z.B. {'role_name': 5}
        return counts
