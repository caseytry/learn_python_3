### only being used as i try to figure out
#how to import better. if can mash into one file and works, not totally blocked.
class Character(object):
    def __init__(self, name):
        self.name = name
        self.has_key = False

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        #print out last scene
        current_scene.enter()

class Scene(object):

    def enter(self):
        print("This scene not configured yet.")
        print("Subclass it and implement enter().")
        exit(1)

class FirstRoom(Scene):

    def enter(self):
        print("we are in the first room!")
        print(f"{player.name} key statuts is {player.has_key}")
        return exit


class Map(object):

    scenes = {
        'firstroom': FirstRoom()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

player = Character(input("Name your character!\n>>"))
print(f"You named them {player.name}")
print(f"player is a {player} class")

print(f"do you have the key? {player.has_key}")

player.has_key = True

print(f"do you have the key now? {player.has_key}")

a_map = Map('firstroom')
a_game= Engine(a_map)
a_game.play()