from configparser import ConfigParser


class Scenario:
    def __init__(self, name: str, author: str, description: str, story_audio: str, img: str):
        self.name = name
        self.author = author
        self.description = description
        self.roles = {}
        self.story_audio = story_audio
        self.img = img

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

    def update_role(self, role):
        self.roles.update({role.name: role})

    def remove_role(self, role):
        del self.roles[role.name]
