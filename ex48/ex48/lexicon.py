directions = ["north", "south", "east", "west","up","down","left","right"]
verbs = ["go", "kill", "eat", "heal", "tear", "rip"]
stops = ["the", "in", "of"]
nouns = ["bear", "princess", "planet", "ship"]

def scan(input):
    words = input.split()
    word_type = ''
    sentence = []

    for word in words:
        if word.lower() in directions:
            word_type = 'direction'
        elif word.lower() in verbs:
            word_type = 'verb'
        elif word.lower() in stops:
            word_type = 'stop'
        elif word.lower() in nouns:
            word_type = 'noun'
        elif word.isdigit():
            word_type = 'number'
            word = int(word)
        else:
            word_type = 'error'
        
        sentence.append((word_type, word))

    return sentence

# I used this prior to using .isdigit
#original code was:
#         elif convert_number(word):
#           word_type = 'number'
#            word = convert_number(word)
#def convert_number(word):
#    try:
#        return int(word)
#    except ValueError:
#        return None    