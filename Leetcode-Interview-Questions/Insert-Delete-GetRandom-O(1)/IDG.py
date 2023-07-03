import random

class RandomizedSet:
    def __init__(self):
        self.set = set()
        self.arr = []

    def insert(self, val):
        if val in self.set:
            return False

        self.set.add(val)
        self.arr.append(val)
        return True

    def remove(self, val):
        if val not in self.set:
            return False

        self.set.remove(val)
        self.arr.remove(val)

    def getRandom(self):
        return random.choice(self.arr)
