
from random import random


class Vague:
    def __init__(self, vague_actuel):
        self.vague_actuel = vague_actuel
        self.enemies = []

    def pick_enemies(self,db):
        self.enemies = []
        vague_data = db.get_vague_data(self.vague_actuel)

        for i in range(3):
            ennemie = random.choice(vague_data.monsters)
            self.enemies.append(ennemie)

        return self.enemies