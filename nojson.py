import random

class Character:
    def __init__(self, name: str, health: int, damage: int):
        self.name = name
        self.health = health
        self.damage = damage

    def isalive(self):
        return self.health > 0

    def attack(self, target) -> None:
        target.health -= self.damage


player = Character("Bob", 100, 20)
enemy = Character("Zombie", 50, 10)

while player.isalive() and enemy.isalive():
    player.attack(enemy)
    enemy.attack(player)

    print(f"Health of {player.name}: {player.health}")
    print(f"Health of {enemy.name}: {enemy.health}")
    input()


