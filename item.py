from db_init import ItemList

class Item:
    def __init__(self, name, effect, droprate, rarity, item_type):
        self.name = name
        self.effect = effect
        self.droprate = droprate
        self.rarity = rarity
        self.item_type = item_type

    dictionary = {item.name: item for item in ItemList}