from nose.tools import *
from ex48 import parser, lexicon

def test_sentence():
    s1 = parser.Sentence(('noun', "cheese"), 
            ('verb', "eats"),
            ('noun', "pigeon"))
    assert s1.verb ==  "eats"
    assert s1.subject == "cheese"
    assert s1.object == "pigeon"


def test_peek():
    word_list = []
    assert None == parser.peek(word_list)

    word_list = lexicon.scan("princess kill bear")
    assert "noun" == parser.peek(word_list)

def test_match():
    word_list = []
    assert None == parser.match(word_list, 'noun')

    word_list = lexicon.scan("bear eat princess")
    assert_equal(('noun', "bear"), parser.match(word_list, 'noun'))
    assert_equal(None, parser.match(word_list, 'noun'))

def test_verb():
    word_list = []
#    assert None == parser.parse_verb(word_list)
    assert_raises(parser.ParserError, parser.parse_verb, word_list)

    word_list = lexicon.scan("the kill bear")
    assert_equal(('verb', "kill"), parser.parse_verb(word_list))