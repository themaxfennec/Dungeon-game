#stat block for mage
import random

class mage:
    def __init__(self):
        self.hp = 45
        self.attack = random.randint(1, 15)
        self.defc=random.randint(5,8)
        self.action= 3
        self.statuses = {}
        self.skill={'skills':'fireshot', 'skill_attribute':'fire','min_dmg':5,'max_dmg':7,'burn':2, 'skill_dis': 'shoots a bolt of fire dealing 5 to 7 dmg and inflicts 2 burn.'}
    #starting relic
    #acid, lighting, fire, ice, and earth

    #9 combinds to do things

    #acid + lighting= if blocking or dbuff without atk takes dmg
    #acid + fire = expload(more dmg)
    #ice + earth= takes more dmg for next x atks
    #lighting + fire = pirs
    #acid + ice = thorns (they will be buffs for you)
    #acid + earth = strength down
    #lighting + ice = second atk (only once can not add more to do more) 
    #lighting + earth = does nothing
    #fire + ice = inc burn on hit
    #fire + earth = applies burn at the end of enemy turn

    #combinding skills


