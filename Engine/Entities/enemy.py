from entity import Entity
import json

class Enemy(Entity):

    def __init__(self):
        super().__init__(
            name="jajs",
            health=38,
            attacks={"Boom": 20}
        )

enemy = Enemy()
print(enemy.name)