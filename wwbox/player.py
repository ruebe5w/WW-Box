class Player:
    def __init__(self, name: str, id: int, attributes: []):
        self.name = name
        self.id = id
        self.attributes = attributes

    def set_attribute(self, key: str, value):
        self.attributes[key] = value

    def get_attribute(self, key: str):
        return self.attributes[key]
