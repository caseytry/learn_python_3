class Character(object):
    def __init__(self, name):
        self.name = name
        self.inventory = {}

    def additem(self, item):
        self.inventory[str(item)]
    
    def deleteitem(self, item):
        del self.inventory[str(item)]

    def displayinventory(self):
        return self.inventory


player = Character(input("Name your character!\n>>"))
print(f"You named them {player.name}")
print(f"player is a {player} class")

print(player.displayinventory)
#weapon = "sword"
player.additem('weapon': "sword")

print(player.inventory)
