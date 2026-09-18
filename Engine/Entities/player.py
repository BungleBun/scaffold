from entity import Entity
import json


class Player(Entity):

    def __init__(self):
        with open(f"/mnt/mydrive/Python Projects/D&D tester/Data/Entities/Player/player.json", "r") as file:
            player_data = json.load(file)
        super().__init__(
            name=player_data["Name"],
            health=player_data["Health"],
            attacks=player_data["Attacks"]
        )

player = Player()
print()