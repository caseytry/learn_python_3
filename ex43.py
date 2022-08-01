from sys import exit
from random import randint
from textwrap import dedent

#test commit
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

class Player(object):

    def __init__(self, health):
        self.health = health 


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
            shoot
            dodge
            tell a joke
            """))
        print(f"health is {health}")
        action = input("> ")

        if action == "shoot":
            print(dedent("""
                we'll do this in a sec
                """))
            health -= 1
            return 'death'

        elif action == "dodge":
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
        print(dedent("""
            we get into armory and doing stuff
            need to get bomb
            keypad lock 
            get it wrong 10 times we ded
            3 digit code
            """))
        code = f"{randint(1,9)}{randint(1,9)}{randint(1,9)}"
        guess = input("[keypad]> ")
        guesses = 0

        while guess != code and guesses <9:
            print("BZZZZEDD!")
            guesses += 1
            guess = input("[keypad]> ")
            #for when want to have code to debug for now.
            print(f"btw code is {code}")
        if guess == code:
            print(dedent("""
                we did it and its open
                go back to bridge to place it
                """))
            return 'the_bridge'
        else:
            print(dedent("""
                lock buzzes last time and then you die
                rip
                """))
            return 'death'

    

class TheBridge(Scene):

    def enter(self):
        print(dedent("""
            getting onto the bridge
            more aliums
            havent seen you, what to do
            """))

        action = input("> ")

        if action == "throw the bomb":
            print(dedent("""
                in panic you toss it
                but one of them gets ya
                maybe will still win?
                """))
            return 'death'

        elif action == "slowly place the bomb":
                print(dedent("""
                    place it carefully
                    they dont notice

                    go back through corridor
                    get to the escape pod!
                    """))
                return 'escape_pod'
        else:
                print("invalid action")
                return "the_bridge"

class EscapePod(Scene):

    def enter(self):
        print(dedent("""
            running through time to pick a pod
            5 total, which one do you take?
            """))
        
        good_pod = randint(1,5)
        guess = input("[pod #]> ")

        if int(guess) != good_pod:
            print(dedent(f"""
                you jumped into pod {guess}
                but it was bad crushing you :( 
                sorry friend
                """))
            return 'death'
        else:
            print(dedent(f"""
                jumped into pod {guess} and its still good!
                you leave the ship and dont end up dead!
                """))

            return 'finished'

            

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
a_character = Player(10)
health = a_character
a_game = Engine(a_map)
a_game.play()
