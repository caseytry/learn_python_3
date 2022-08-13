import character
import engine

class Scene(object):

    def enter(self):
        print("This scene not configured yet.")
        print("Subclass it and implement enter().")
        exit(1)

class FirstRoom(Scene):

    def enter(self):
        print("we are in the first room!")
        print(f"{player.name} key statuts is {player.has_key}")
        return 'secondroom'

class SecondRoom(Scene):

    def enter(self):
        print("have we made it to the second  room")
        return exit


class Map(object):

    scenes = {
        'firstroom': FirstRoom(),
        'secondroom': SecondRoom()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

player = character.Character(input("Name your character!\n>>"))
print(f"You named them {player.name}")
print(f"player is a {player} class")

print(f"do you have the key? {player.has_key}")

player.has_key = True

print(f"do you have the key now? {player.has_key}")

a_map = Map('firstroom')
a_game= engine.Engine(a_map)
a_game.play()