
class Entity:
    def __init__(self, name: str, health: int, attacks: dict):
        self.name = name
        self.health = health
        self.attacks = attacks

    def isalive(self):
        return self.health >= 0

    def attack(self, target) -> None:
        damage = self.attack[1]
        target.health -= damage

