from affichage import Affichage
from vu import vue_selection_equipe

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.team = []
        self.inventory = []

    def CreateTeam(self, characters):
        self.team = []
        characters = characters.copy()
        for _ in range(3):
            character = self.PickCharacter(characters)
            self.team.append(character)
            characters.remove(character)


    def PickCharacter(self, list_of_characters):
        selected_character_index = Affichage.display_vue(vue_selection_equipe( self.team, list_of_characters))
        character = list_of_characters[selected_character_index]
        return character
    
    def IsTeamAlive(self):
        return any(character.Is_alive() for character in self.team)
    

    def CheckInventory(self):
        return [item.name for item in self.inventory]

    def UseItem(self, item):
        if item in self.inventory:
            target = self.PickCharacter(self.team)
            if target is None:
                return 
            if item.item_type == "consumable":
                item.Use(target)
                self.inventory.remove(item)
            else:
                if not target.Is_Slot_Available(item.item_type):
                    old = target.Get_Equipment(item.item_type)
                    target.Unequip_Item(old)
                    self.inventory.append(old)
                target.Equip_Item(item)
            self.inventory.remove(item)
                

        