class Entity:
    def __init__(self, name, hp, maxHp, attack, defense):
        self.name = name
        self.hp = hp
        self.maxHp = maxHp
        self.attack = attack
        self.defense = defense

    def __str__(self):
        return f"Name: {self.name}, HP: {self.hp}/{self.maxHp}, Attack: {self.attack}, Defense: {self.defense}"

    def Is_alive(self): 
        return self.hp > 0
    