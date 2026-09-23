from Engine.Entities.entity import Entity
import json


class Player(Entity):

    def __init__(self):
        with open(f"/mnt/mydrive/PythonProjects/DDTest/Data/Entities/Player/player.json", "r") as file:
            player_data = json.load(file)
        super().__init__(
            name=player_data["Name"],
            health=player_data["Health"],
            attacks=player_data["Attacks"]
        )

    def choose_attack(self):

        attack_names = list(self.attacks.keys())

        for number, attack_name in enumerate(attack_names, start=1):
            print(f"{number}. {attack_name}")

        while True:
            choice = input(">>>")

            if choice.isdigit():
                choice = int(choice)

                if 1 <= choice <= len(attack_names):
                    return attack_names[choice - 1]

            print("Invalid choice. Try again.")