# Exercise 47: Automated Testing

Having to type commands into your game over and over to make sure it's working is annoying. Wouldn't it be better to write little pieces of code that test your code? Then when you make a change, or add a new thing to your program, you just "run your tests" and the tests make sure things are still working. These automated tests won't catch all your bugs, but they will cut down on the time you spend repeatedly typing and running your code.

Every exercise after this one will not have a What You Should See section, but instead will have a What You Should Test section. You will be writing automated tests for all of your code starting now, and this will hopefully make you an even better programmer.

I won't try to explain why you should write automated tests. I will only say that you are trying to be a programmer, and programmers automate boring and tedious tasks. Testing a piece of software is definitely boring and tedious, so you might as well write a little bit of code to do it for you.

That should be all the explanation you need because your reason for writing unit tests is to make your brain stronger. You have gone through this book writing code to do things. Now you are going to take the next leap and write code that knows about other code you have written. This process of writing a test that runs some code you have written forces you to understand clearly what you have just written. It solidifies in your brain exactly what it does and why it works and gives you a new level of attention to detail.
Writing a Test Case

We're going to take a very simple piece of code and write one simple test. We're going to base this little test on a new project from your project skeleton.

First, make a ex47 project from your project skeleton. Here are the steps you would take. I'm going to give these instructions in English rather than show you how to type them so that you have to figure it out.

    Copy skeleton to ex47.
    Rename everything with NAME to ex47.
    Change the word NAME in all the files to ex47.
    Finally, remove all the *.pyc files to make sure you're clean.

Refer back to Exercise 46 if you get stuck, and if you can't do this easily then maybe practice it a few times.

## Note

Remember that you run the command nosetests to run the tests. You can run them with python3.6 ex47_tests.py, but it won't work as easily, and you'll have to do it for each test file.

Next, create a simple file ex47/game.py where you can put the code to test. This will be a very silly little class that we want to test with this code in it:

```python
class Room(object):

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.paths = {}

    def go(self, direction):
        return self.paths.get(direction, None)

    def add_paths(self, paths):
        self.paths.update(paths)
```

Once you have that file, change the unit test skeleton to this:

```python
from nose.tools import *
from ex47.game import Room


def test_room():
    gold = Room("GoldRoom",
                """This room has gold in it you can grab. There's a
                door to the north.""")
    assert_equal(gold.name, "GoldRoom")
    assert_equal(gold.paths, {})

def test_room_paths():
    center = Room("Center", "Test room in the center.")
    north = Room("North", "Test room in the north.")
    south = Room("South", "Test room in the south.")

    center.add_paths({'north': north, 'south': south})
    assert_equal(center.go('north'), north)
    assert_equal(center.go('south'), south)

def test_map():
    start = Room("Start", "You can go west and down a hole.")
    west = Room("Trees", "There are trees here, you can go east.")
    down = Room("Dungeon", "It's dark down here, you can go up.")

    start.add_paths({'west': west, 'down': down})
    west.add_paths({'east': start})
    down.add_paths({'up': start})

    assert_equal(start.go('west'), west)
    assert_equal(start.go('west').go('east'), start)
    assert_equal(start.go('down').go('up'), start)
```

This file imports the Room class you made in the ex47.game module so that you can do tests on it. There is then a set of tests that are functions starting with test_. Inside each test case there's a bit of code that makes a room or a set of rooms, and then makes sure the rooms work the way you expect them to work. It tests out the basic room features, then the paths, then tries out a whole map.

The important functions here are assert_equal, which makes sure that variables you have set or paths you have built in a Room are actually what you think they are. If you get the wrong result, then nosetests will print out an error message so you can go figure it out.
Testing Guidelines

Follow this general loose set of guidelines when making your tests:

    Test files go in tests/ and are named BLAH_tests.py, otherwise nosetests won't run them. This also keeps your tests from clashing with your other code.
    Write one test file for each module you make.
    Keep your test cases (functions) short, but do not worry if they are a bit messy. Test cases are usually kind of messy.
    Even though test cases are messy, try to keep them clean and remove any repetitive code you can. Create helper functions that get rid of duplicate code. You will thank me later when you make a change and then have to change your tests. Duplicated code will make changing your tests more difficult.
    Finally, do not get too attached to your tests. Sometimes, the best way to redesign something is to just delete it and start over.

## What You Should See

```shell
$ nosetests
...
----------------------------------------------------------------------
Ran 3 tests in 0.008s

OK
```

That's what you should see if everything is working right. Try causing an error to see what that looks like and then fix it.

##Study Drills

    Go read about nosetests more, and also read about alternatives.
    Learn about Python's "doc tests," and see if you like them better.
    Make your room more advanced, and then use it to rebuild your game yet again, but this time unit test as you go.

