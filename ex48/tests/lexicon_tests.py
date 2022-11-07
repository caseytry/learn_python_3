from nose.tools import *
from ex48 import lexicon


def test_directions():
    assert_equal(lexicon.scan("North"), [('direction', 'North')])
    result = lexicon.scan("north south EAST")
    assert_equal(result, [('direction', 'north'),
                        ('direction', 'south'),
                        ('direction', 'EAST')])
    assert_equal(lexicon.scan("down"), [('direction', 'down')])
    result = lexicon.scan("left right left right")
    assert_equal(result, [('direction', 'left'),
                        ('direction', 'right'),
                        ('direction', 'left'),
                        ('direction', 'right')])

def test_verbs():
    assert_equal(lexicon.scan("go"), [('verb', 'go')])
    result = lexicon.scan("go KILL eat heal tear rip")
    assert_equal(result, [('verb', 'go'),
                        ('verb', 'KILL'),
                        ('verb', 'eat'),
                        ('verb', 'heal'),
                        ('verb', 'tear'),
                        ('verb', 'rip')])

def test_stops():
    assert_equal(lexicon.scan("the"), [('stop', 'the')])
    result = lexicon.scan("the IN of")
    assert_equal(result, [('stop', 'the'),
                        ('stop', 'IN'),
                        ('stop', 'of')])

def test_nouns():
    assert_equal(lexicon.scan("bear"), [('noun', 'bear')])
    result = lexicon.scan("BEAR princess planet shIp")
    assert_equal(result, [('noun', 'BEAR'),
                        ('noun', 'princess'),
                        ('noun', 'planet'),
                        ('noun', 'shIp')])

def test_numbers():
    assert_equal(lexicon.scan("1234"), [('number', 1234)])
    result = lexicon.scan("3 91234")
    assert_equal(result, [('number', 3),
                        ('number', 91234)])

def test_errors():
    assert_equal(lexicon.scan("ASDFADFASDF"),
                [('error', 'ASDFADFASDF')])
    result = lexicon.scan("bear IAS princess twelve")
    assert_equal(result, [('noun', 'bear'),
                        ('error', 'IAS'),
                        ('noun', 'princess'),
                        ('error', 'twelve')])