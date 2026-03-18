#stat block for monk
import random

class monk:
    def __init__(self):
        self.hp = 50
        self.attack = random.randint(5, 25)
        self.defc=4
        self.action= 4
        self.statuses = {}
        self.skill={}

    #starting relic heat system(stances) forms through skills

    #burning rage: deal more dmg but if they are to hot they take dmg
    #cooling down/heating up/nutrel: hit more times in a range
    #ice bearer: more block and take more dmg if to cold