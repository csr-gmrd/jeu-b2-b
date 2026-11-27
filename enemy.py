import random

from entity import Entity
from db_init import ItemList

class Enemy(Entity):
    def __init__(self, dropables):
        self.dropables = dropables

    def Drop_Loot(self):
        dropped_items = []
        for item in self.dropables:
            if item.is_looted(item.droprate):
                dropped_items.append(item)
        return dropped_items

    def is_looted(self, droprate):
        chiffre = random.randint(1, 100)
        if chiffre < droprate:
            return True
        else:
            return False

    def Play_Turn(self, target):
        override_message = super().Play_Turn(target)
        return override_message

    