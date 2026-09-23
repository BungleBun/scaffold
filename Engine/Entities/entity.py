
class Entity:
    def __init__(self, name: str, health: int, attacks: dict):
        self.name = name
        self.health = health
        self.attacks = attacks

    def isalive(self):
        return self.health > 0

    def attack(self, target, attack_name:str) -> None:
        attack_data = self.attacks[attack_name]
        damage = attack_data["Damage"]
        target.health -= damage

        print(f"{self.name} deals {damage} damage to {target.name}")
