#stat block for mage
import random

class mage:
    def __init__(self):
        self.hp = 45
        self.attack = random.randint(1, 15)
        self.defc=random.randint(5,8)
        self.action= 3


        #skill you can get