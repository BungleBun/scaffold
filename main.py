import random
import json
from pathlib import Path

with open("data.json", "r") as file:
    data = json.load(file)

class Entity:

    NPCTYPE = data["NPC_TYPE"].lower

    def __init__(self, name, hp, attacks):
        self.name = name
        self.hp = hp
        self.attacks = attacks

class Player:
    pass

class Enemy:
    def __init__(self, name, hp, ):
        super().__init__(
            name=data["Name"],
            hp=data["HP"],
            attacks=data["Attacks"]
        )

    def alive(self):
        return self.hp > 0

    def attack(self):
        attack = random.choice(list(data["Attacks"].items()))
        attack_name = attack[0]
        damage = attack[1]

def NPCTYPE():
    npcdata = data["NPC_TYPE"].lower()

    if npcdata == "enemy":
        Enemy()

attack = random.choice(list(data["Attacks"].items()))
print(attack)