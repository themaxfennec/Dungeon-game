import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))
from classes.Mage import mage
from classes.Warrior import warrior
from classes.Monk import monk

class Effect:
    def __init__(self, name, stacks=1, timing="end"):  
        # timing: "start" or "end" of turn
        self.name = name
        self.stacks = stacks
        self.timing = timing

    def apply(self, target):
        """Apply effect immediately if needed"""
        if self.name == "burn":
            print(f"{target.name} is ignited! ({self.stacks} stacks)")
            target.statuses[self.name] = self
        elif self.name == "plate":
            print(f"{target.name} is plated! (+{self.stacks} block)")
            target.statuses[self.name] = self

    def process(self, target):
        if self.name == "burn":
            dmg = self.stacks
            target.hp -= dmg
            print(f"{target.name} takes {dmg} burn damage!")
            self.stacks -= 1
            if self.stacks <= 0:
                print(f"{target.name}'s burn effect ends!")
                del target.statuses[self.name]
        elif self.name == "plate":
            defc = self.stacks
            print(f"{target.name} has {defc} plate blocks remaining.")

def process_effects(character, timing="end"):
    for effect in list(character.statuses.values()):
        if effect.timing == timing:
            effect.process(character)