from Engine.Entities.entity import Entity
from Engine.Entities.player import Player
from Engine.Entities.enemy import Enemy


class Fight_Scene:

    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy

    def fight(self) -> None:
        while self.player.isalive() and self.enemy.isalive():
            player_attack = self.player.choose_attack()
            self.player.attack(self.enemy, player_attack)

            if self.enemy.isalive():
                enemy_attack = self.enemy.choose_attack()
                self.enemy.attack(self.player, enemy_attack)

        if self.player.isalive():
            print(f"{self.player.name} wins")
        else:
            print(f"{self.enemy.name} wins")

player = Player()
enemy = Enemy()
test = Fight_Scene(player, enemy)

test.fight()

# Fight sequence fight function should take 1 target, being the enemy. The enemy is determined by the map section.
# Map.json -> Value (Enemy): Key (Enemy name, or random enemy, random enemy is handled through random_enemy.py to pick random enemy from that map.)
# Key -> current_enemy variable either above or just in fight_scene class = Key from specified_map_data["Map Enemies"]
# Fight method takes current_enemy variable as an argument so that it basically says player is fighting whatever specified enemy is.
# So calling this would look like player.fight(current_enemy)