

class Monster:
    def __init__(self, health = 0, x = 0, y = 0):
        self.health = health
        self.x = x
        self.y = y
        print("Implement __init__ for all monsters")

    def takeTurn(self, characters, map, x, y):
        return "Implement takeTurn"

    def takeDamage(self, d):
        self.health -= d
        return self.health > 0

