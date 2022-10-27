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

## Study Drills

    Go read about nosetests more, and also read about alternatives.
    Learn about Python's "doc tests," and see if you like them better.
    Make your room more advanced, and then use it to rebuild your game yet again, but this time unit test as you go.

## My Responses:

Go read about nosetests more, and also read about alternatives.
To start with, the book is showing its age in that nosetests is no longer actively supported, instead a new version, nose2, has been made to continue the ideas nose had for testing.

As I was trying to understand the differences between the tests, a few different frameworks kept coming back and were the main ones I looked into. They are:

unittest/unittest2
nose/nose2
py.test

Nose/nose2 were built to extend unittest/unittest2; so I tried to take a look at unittest first.

Unittest does have one starting advantage compared to the others by being a part of the standard Python library, making it so that you dont need to worry about having an additional dependency that you would need to deal with.

One of the common things that others in the community had noted was that unittest tests were longer to write and harder to read than pytest.  I tried to find a quick way to see these differences without needing to spend too long making a bunch of tests myself.  

The way I initially handled this for the differences in testing between unittest and pytest was with the sites https://www.pythonpool.com/python-unittest-vs-pytest/ and https://blog.daftcode.pl/the-cleaning-hand-of-pytest-28f434f4b684

Testing with unittest, the code you need to make for the tests is overall longer due to needing to create a new class for each test you want to do that inherits from the unittest.TestCase. So in addition to making a new class for each test of each function you want to do, the code to enable the tests themselves also have to pass `self` as a parameter to the function, and the functions then start with `self.assert`, which may be a personal preference on if one thinks this makes reading of the code more complex or less complex.  To me personally, the numerous additions of `self` for unittest makes reading the tests seem like they are a bit more bloated than code that would not need all the `self` calls. This may still be due to being overall newer to coding!


Nose/Nose2
Since Nose extends unittest, it seems like it has simplified some of the efforts you would need to do if you did unittest by not always needing to create a new class that inherits from unittest and then dealing with all of the '`self` references. Since it is not a part of the standard library, you are now involving a dependancy that you wouldn't have to deal with in unittest.  

One negative that Nose has right now is that nose is no longer actively supported anymore, and while Nose2 does exist it actively calls out that pytests has a bigger team and community than nose2 does, so it appears that team is trying to push more people towards alternatives than to use its product unless needed for new projects.
Because of these reasons, and because the book is still going to use Nose as its reference point for right now so I'll get some more exposure to it, I did not continue looking deeper into nose at this time.

Pytest does seem very appealing to me as a framework. One of the things that came up during the research was how Pytest utilizes the default Python assert, instead of needing its own assert methods for trying to test things. This seems very appealing compared to trying to remember/look up all the different assert methods that unittest/nose directly support, since I'd just be using the standard I'd already be using for other parts of python code and not need to context switch.


Learn about Python's "doc tests," and see if you like them better.

I read a bit about this testing strategy, but I do not think I like it overall. It seems very clunky/awkward to use since I'd need to remember to add each line that I was looking to test with the >>> prefix as well as maintaining the proper quotation marks in the right place.  While it sounds like it'd work great for some simple things, I do not think I'd explore this further unless need for it came along.

Make your room more advanced, and then use it to rebuild your game yet again, but this time unit test as you go.
I did this in the code; though I took the 'rebuild your game yet again' to mean the room/game in the tests rather than the game that was made in chapter 45.