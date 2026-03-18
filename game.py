import random

from classes.Warrior import warrior
from classes.Mage import mage
from classes.Monk import monk
from effects.stats import Effect, process_effects

#test monster
class mon:
    def __init__(self):
        self.hp = random.randint(30, 40)
        self.attack = random.randint(3, 5)

floor = 1

class_sec=True

#makes classes work for combat
global classes

#class select
while class_sec== True:
    classes=input("Pick your class: warrior, mage, theif, monk!!(enter quit to quit)").lower()

    if classes=="warrior":
        hero=warrior()
    elif classes=="mage":
        hero=mage()
    elif classes=="monk":
        hero=monk()
    #elif classes=="theif":
        #hero=theif()
    elif classes=="quit":
        break
    else:
        print("That is not a class. Please select a class")
        continue
    class_sec=False
#need to add the other classes

while True:
    user_input = input("\nType 'go' to move to the next floor or 'quit' to exit: ").lower()
    
    if user_input == 'quit':
        break
    if user_input == 'go':
        print(f"-----Floor {floor}------")

        #monster
        enemy = mon()
        print(f"!-- A monster with {enemy.hp} HP comes out! --!")
        
        
        # combat
        while enemy.hp > 0 and hero.hp > 0:
            m_hit = enemy.attack + random.randint(3, 7)
            print(f"The monster is attacking for {m_hit}.")
            print(f"Your Hp {hero.hp}.")
            action=hero.action

            #reset defense 
            defc=0

            #player actions
            while action>0 and enemy.hp>0:
                process_effects(hero, timing="start")
                #makes it so the action system works
                print(f"\nActions remaining: {action}")
                print(f"\nBlock: {defc}")
                cmd = input("Choose action (atk/def/skill): ").lower()

                #attack
                if cmd == 'atk':
                    hit = hero.attack + random.randint(1, 5)
                    enemy.hp -= hit
                    print(f"You hit for {hit}! Monster HP: {max(0, enemy.hp)}")

                #defence
                elif cmd == 'def':
                    defc= 1+random.randint(3,10)+defc

                elif cmd == 'skill':
                    print("\n--- Available Skills (Type 'back' to return) ---")
                    print(hero.skill['skills'])

                    choice = input("Use skill, 'info [name]', or 'back': ").lower()

                    if choice=='back':
                        print("Returning to Main")
                        continue
                
                else:
                    print("That is not an action.")
                    continue
                
                action-=1
                process_effects(hero, timing="end")


                
    
            #monster hits back if it's still alive and heathy
            if enemy.hp > 0:
                process_effects(hero, timing="start")
                dmg_hero=max(0,m_hit-defc)
                hero.hp = hero.hp-dmg_hero
                print(f"Monster hits you for {m_hit} you block {defc}! Your HP: {hero.hp}")
                process_effects(hero, timing="end")
            

            #to make the parry work for the warrior
            if classes=='warrior':
                hero.parry(enemy, dmg_hero, hero)

        #after
        if hero.hp <= 0:
            print("You died! Game Over.")
            class_sec=True
            break
        else:
            print("Monster defeated! You move deeper into the dungeon.")
            floor += 1