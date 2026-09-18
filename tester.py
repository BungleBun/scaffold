import random
import json
from pathlib import Path

enemies_folder = Path("Data/Entities/Enemies")
enemy_files = list(enemies_folder.glob("*.json"))

random_enemy = random.choice(enemy_files)

with open(f"{random_enemy}", "r") as file:
    data = json.load(file)

random_attack = random.choice(data["Attacks"])

print(random_attack)