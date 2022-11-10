print("""You enter a dark room with two doors.
do you go through door #1, door #2, or door #3?""")

door = input("> ")

if door == "1":
    print("There's a giant bear here eating a cheese cake.")
    print("What do you do?")
    print("1. Take the cake.")
    print("2. Scream at the bear.")

    bear = input("> ")

    if bear == "1":
        print("The bear eats your face off. Good job!")
    elif bear == 2:
        print("The bear eats your legs off. Good job!")
    else:
        print(f"Well, doing {bear} is probably better.")
        print("Bear runs away.")

elif door == "2":
    print("You stare into the endless abyss at Cthulu's retina.")
    print("1. Blueberries.")
    print("2. Yellow jacket clothespins")
    print("3. Understanding revolvers yelling melodies.")

    insanity = input("> ")

    if insanity == "1" or insanity == "2":
        print("Your body survives powered by a mind of yellow.")
        print("Good job!")
    else:
        print("The insanity rots your eyes into a pool of muck.")
        print("Good job!")

elif door == "3":
    print("You find yourself at the base of a tree that has an owl in it.")
    print("What would you like to do?")
    print("1. Chop the tree down")
    print("2. Rest beneath the tree")

    tree_choice = input("> ")

    if tree_choice == "1":
        print("As you try to chop the tree down, you remember you dont have an axe.")
        print("You begin hitting the tree with your fist instead. It HURTS, but you do make progress!")
        print("When the tree is finally felled, and your hand is broken, the Owl turns to you.")
        print("It calmly says 'That was quite rude breaking my house man..' and flies away.")
    
    elif tree_choice == "2":
        print("You lay beneath the tree, counting leaves until you drift to sleep.")
        print("The Owl flies down, covers you in a blanket, then flies away again.")
    
    else:
        print(f"Doing {tree_choice} is an option too I suppose. Good luck with that!")
else:
    print("You stumble around and fall on a knife and die. Good job!")
