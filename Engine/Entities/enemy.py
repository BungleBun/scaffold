from entity import Entity
import json

class Enemy(Entity):

    def __init__(self):
        with open (f"/mnt/mydrive/PythonProjects/DDTest/Data/Entities/Enemies/zombie.json", "r") as file:
            enemy_data = json.load(file)
        super().__init__(
            name=enemy_data["Name"],
            health=enemy_data["Health"],
            attacks=enemy_data["Attacks"]
        )

enemy = Enemy()
print(enemy.name)