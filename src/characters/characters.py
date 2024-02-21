

class Character:

    def __init__(self, name = "Nameless", type = "classless", health = 0, items = [], bag = []):
        self.name = name
        self.type = type
        self.health = health
        self.items = items
        self.bag = bag

    def takeTurn(self, map, x, y):
        print("implement takeTurn for all characters")
        pass
