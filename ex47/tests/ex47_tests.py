from nose.tools import *
from ex47.game import Room


def test_room():
    gold = Room("GoldRoom",
            """This room has gold in it you can grab. there's a
            door to the north.""")
    assert_equal(gold.name, "GoldRoom")
    assert_equal(gold.paths, {})

def test_room_paths():
    center = Room("Center", "Test room in the center.")
    north = Room("North", "Test Room in the north.")
    south = Room("South", "test room in the south")

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
    assert_equal(west.go('east').go('down').go('up').go('west'), west)
    assert_equal(down.go('up').go('west').go('east'), start)

#my add
    start.add_things({'Bob': 'Male'})
    start.add_things({'Mary': 'Female'})
    #rewriting above to be just one entry, "characters"
    start.add_things({'People': ['Fred', 'Jane', 'Tim']})
    west.add_things({'Trees': 'Object'})
    assert_true(start.see('Bob'))
    assert_in('Fred', start.things['People'][0])
    assert_in('People', start.things)
    assert_in('Fred', start.things['People'])
    assert_not_in('Bob', start.things['People'])
    assert_true(start.see('People'))
    assert_true(start.see('Mary'))
    assert_false(start.see('Trees'))