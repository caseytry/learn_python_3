from sys import exit
from random import randint
from textwrap import dedent

class Scene(object):

    def enter(self):
        print("This scene not configured yet.")
        print("Subclass it and implement enter().")
        exit(1)

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

class Death(Scene):

    quips = [
        "That didnt go so well for you huh..",
        "If only luck had been on your side today.",
        "I..guess...you at least tried?",
        "Have you asked google for help?"

    ]

    def enter(self):
        print(Death.quips[randint(0, len(self.quips)-1)])
        exit(1)

class CentralCorridor(Scene):

    def enter(self):
        print(dedent("""
            Ho boy he typed a lot here and im short cutting so That
            i can try an see if it passes once this is made.
            """))

        action = input("> ")

        if action == "shoot!":
            print(dedent("""
                we'll do this in a sec
                """))
            return 'death'

        elif action == "dodge!":
            print(dedent("""
                We dodging and stuff happens
                """))
            return 'death'

        elif action == "tell a joke":
            print(dedent("""
                well that worked cuz i guess
                """))
            return 'laser_weapon_armory'

        else:
            print("Does not compute!")
            return 'central_corridor'

class LaserWeaponArmory(Scene):

    def enter(self):
        pass

class TheBridge(Scene):

    def enter(self):
        pass

class EscapePod(Scene):

    def enter(self):
        pass

class Finished(Scene):

    def enter(self):
        print("You won! Good jorb.")
        return 'finished'

class Map(object):

    scenes = {
        'central_corridor': CentralCorridor(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'death': Death(),
        'finished': Finished(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
