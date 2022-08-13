import character
import engine

class Scene(object):

    def enter(self):
        print("This scene not configured yet.")
        print("Subclass it and implement enter().")
        exit(1)

class PlayerCreationRoom(Scene):

    def enter(self):
        print("Welcome to my game! First step, name your character.")
        player = character.Character(input("Name your character!\n>>"))
        print(f"You named them {player.name}. Good Luck!")

        return 'firstroom'



class FirstRoom(Scene):

    def enter(self):
        print("we are in the first room")
        print("you awake in a room with only one exit. what would you like to do?")
        action = input ("> ")
        if action == "exit room":
            print("you try to go to the second room")
            return 'secondroom'

        if action == "search":
            print("""You try to find any hints as to what this place is.
            While it is clearly not lived in, you dont feel totally unsafe.
            there must be a way out however..
            """)
            return 'firstroom'

        else:
            print("invalid action")
            return 'firstroom'

class SecondRoom(Scene):

    def enter(self):
        print("have we made it to the second  room")
        return exit


class Map(object):

    scenes = {
        'creation': PlayerCreationRoom(),
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


#print(f"player is a {player} class")
#print(f"do you have the key? {player.has_key}")
#player.has_key = True
#print(f"do you have the key now? {player.has_key}")

a_map = Map('creation')
a_game= engine.Engine(a_map)
a_game.play()