import character


player = character.Character(input("Name your character!\n>>"))
print(f"You named them {player.name}")
print(f"player is a {player} class")

print(f"do you have the key? {player.has_key}")

player.has_key = True

print(f"do you have the key now? {player.has_key}")