import random

class Bag:
    def __init__(self):
        self.gems = []
        self.pulled = []
        self.totals = {}

    def count(self, type):
        if type not in self.totals:
            return 0

        return self.totals[type]

    def add(self, type):
        if type not in self.totals:
            self.totals[type] = 1
            self.gems.append(type)
            return

        self.totals[type] += 1
        self.gems.append(type)

    def pull(self, n):
        i = 0
        tempPulled = []
        while i < n:
            if len(self.gems) > 0:
                temp = self.gems.pop(random.randint(0, len(self.gems) - 1))
                tempPulled.append(tempPulled)
            i += 1
        self.pulled.append(tempPulled)

    def rebag(self, r):
        for gem in self.pulled:
            if r(gem):
                self.add(gem)
        self.pulled = []



