from configparser import ConfigParser


class Scenario:
    def __init__(self, name: str, author: str, description: str):
        self.name = name
        self.author = author
        self.description = description
        self.roles = {}

    def write_to_file(self):
        """Saves Scenario to config"""
        file = ConfigParser(allow_no_value=True)
        file['GENERAL'] = {'name': self.name, 'author': self.author, 'description': self.description}
        role_name_array = {}
        for role in self.roles:
            role_name_array.update({role})
