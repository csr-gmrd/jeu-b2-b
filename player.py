class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.team = []
        self.inventory = []

    def CreateTeam(self, characters):
        self.team = characters

    def PickCharacter(self, index):
        if 0 <= index < len(self.team):
            return self.team[index]
        else:
            return None

    def IsTeamAlive(self):
        return any(character.Is_alive() for character in self.team)

    def CheckInventory(self):
        return [item.name for item in self.inventory]

    def UseItem(self, item):
        if item in self.inventory:
            item.Use()
            self.inventory.remove(item)