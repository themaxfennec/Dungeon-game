import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))
from classes.Mage import mage
from classes.Warrior import warrior
from classes.Monk import monk
from enemys.monsters import Monster

class Effect:
    def __init__(self, name, stacks=1):  
        self.name = name
        self.stacks = stacks

    def apply(self, target):
        if not hasattr(target, 'statuses'):
            target.statuses = {}
        
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
                print(f"{getattr(target, 'name', 'Monster')} takes {dmg} burn damage!")
                self.stacks -= 1
                if self.stacks <= 0:
                    print(f"{getattr(target, 'name', 'Monster')}'s burn effect ends!")
                    del target.statuses[self.name]

        if self.name == "plate":
            defc = self.stacks
            print(f"{target.name} has {defc} plates blocking.")


def process_effects(target):
        if hasattr(target, 'statuses'):
            for effect in list(target.statuses.values()):
                effect.process(target)