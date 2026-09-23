from Engine.Entities.entity import Entity
import json
import random

class Enemy(Entity):

    def __init__(self):
        with open (f"/mnt/mydrive/PythonProjects/DDTest/Data/Entities/Enemies/zombie.json", "r") as file:
            enemy_data = json.load(file)
        super().__init__(
            name=enemy_data["Name"],
            health=enemy_data["Health"],
            attacks=enemy_data["Attacks"]
        )

    def choose_attack(self):
        return random.choice(list(self.attacks.keys()))
