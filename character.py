class Character:
    def __init__(self, equipable, equipment):
        self.equipment = equipment
        self.equipable = equipable

    def Equip_Item(self, equipable):
        self.equipment.append(equipable)
        return equipable 
    

    def Unequip_Item(self, equipable):
        if equipable in self.equipment:
            self.equipment.remove(equipable)
        return equipable

    def __str__(self):
        return f"Character with equipment: {', '.join([item.name for item in self.equipment])}, Attack: {self.attack}, Defense: {self.defense}"

    def Project_Damage(self, target):
        damage_dealt = target.copy().Take_damage(self.attack)
        return damage_dealt

    def Play_Turn(self, target):
        override_message = super().Play_Turn(target)
        return override_message
    
        