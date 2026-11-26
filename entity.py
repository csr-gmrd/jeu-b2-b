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

    def Take_damage(self, damage):
        damage_taken = max(damage - self.defense, 0)
        self.hp -= damage_taken
        if self.hp < 0:
            self.hp = 0
        return damage_taken

    def Heal(self, amount):
        self.hp += amount
        if self.hp > self.maxHp:
            self.hp = self.maxHp
        return self.hp

    def Attack(self, target):
        damage_dealt = target.Take_damage(self.attack)
        return damage_dealt

    def Play_Turn(self, target):
        if self.Is_alive():
            damage_dealt = self.Attack(target)
            return f"{self.name} attacks {target.name} for {damage_dealt} damage."
        else:
            return f"{self.name} is defeated and cannot attack."

    