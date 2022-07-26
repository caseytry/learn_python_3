import character
import engine

class Scene(object):

    def enter(self):
        print("This scene not configured yet.")
        print("Subclass it and implement enter().")
        exit(1)

class FirstRoom(Scene):

    def enter(self):
        print("We are in the first room")
        print("You awake in a room with only one exit. It's mostly empty, but maybe could find something of use if you search? What would you like to do?")
        action = input ("> ")
        if action == "exit room":
            print("you try to go to the second room")
            return 'secondroom'

        if action == "search":
            print("""
            You try to find any hints as to what this place is.
            While it is clearly not lived in, you dont feel totally unsafe.
            there must be a way out however..
            """)
            return 'firstroom'

        else:
            #have print out valid actions?
            print("invalid action")
            return 'firstroom'

class LockedDoorRoom(Scene):

    def enter(self):
        print("have we made it to the second room")
        print("""
        In this room, aside from the door you just came through, there are two others.
        One of them has a deadbolt lock which is preventing you from getting through.
        The other is open, but can't quite tell whats in side without going in yourself.
        What do you do?
        """)

        action = input ("> ")
        if action == "search":
            print("""
            You search the room. 
            The locked door does have traces of light underneath it. Maybe its the way out?
            The lock itself could be opened if you have a key.
            """)
            return "secondroom"

        if action == "open locked door":
            if player.has_key == False:
                print("You try to force the door open, but it won't budge.")
                return 'secondroom'

            if player.has_key == True:
                print("You insert the key, the deadbolt moves and it is no longer locked!")
                return 'escape'

        if action == "go to first room":
            print ("You head back to the first room")
            return 'firstroom'

        if action == "go to unlocked room":
            print("You go into the unlocked room")
            return 'unlockedroom'

class ThirdRoom(Scene):

    def enter(self):

        print("You go into the third room. This room seems very similar to the others, though one corner is dark.")
        print("What would you like to do?")

        action = input("> ")

        if action == "leave":
            print("You leave this room and head back to the locked room")
            return 'secondroom'

        if action == "search":
            print("""
            You try to search the dark section of the room. Initially, you just walk around with
            your arms outstretched to see if you hit something. 

            You don't grab anything, but your foot does kick something small.
            Cautiously, you bend down and feel around by your feet until you feel it!
            Its a key!
            You take the key and put it in your pocket.
            """)
            player.has_key = True 
            return 'secondroom'

class Escaped(Scene):
    
    def enter(self):
        print("You go through the door that has been locked and have escaped! How long were we in there?!")
        print("Congratulations!")
        exit()

class Map(object):

    scenes = {
        'creation': PlayerCreationRoom(),
        'firstroom': FirstRoom(),
        'secondroom': LockedDoorRoom(),
        'unlockedroom': ThirdRoom(),
        'escape': Escaped()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('firstroom')
a_game= engine.Engine(a_map)
player = character.Character(input("Name your character!\n>>"))
a_game.play()