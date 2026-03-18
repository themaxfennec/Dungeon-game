#warrior stat block
import random

class warrior:
    def __init__(self):
        self.hp = 60
        self.attack = random.randint(1, 20)
        self.defc=random.randint(5,15)
        self.action= 4
        self.statuses = {}
        self.skill={}
    
    #change this in to a relic
    def parry(self, enemy, dmg_hero, hero):
        if dmg_hero==0:
            parry_cha=random.randint(1,20)
            if parry_cha>=10:
                enemy.hp-=hero.attack
                print(f"YOU PARRIED DEALING {hero.attack}!!! Monster HP: {max(0, enemy.hp)}")
                return enemy.hp
            #some enrage that does something other then more dmg or block
                
    
    #skill you can get