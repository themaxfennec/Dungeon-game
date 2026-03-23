import random

class Monster:
    def __init__(self):
        self.name = "Monster"
        self.hp = random.randint(30, 40)
        self.attack = random.randint(3, 5)
        self.statuses = {}

