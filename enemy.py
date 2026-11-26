from entity import Entity

class Enemy(Entity):
    def __init__(self, item):
        self.item = item

    def Drop_Loot(self):
        return self.item

    def Play_Turn(self, target):
        override_message = super().Play_Turn(target)
        return override_message

    