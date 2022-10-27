class Room(object):

    def __init__(self, name, description):
        self.name = name
        self.description =  description
        self.paths = {}
        self.things = {}

    def go(self, direction):
        return self.paths.get(direction, None)
    
    def add_paths(self, paths):
        self.paths.update(paths)

    def see(self, thing, type):
        return self.things.get(thing, type)

    def add_things(self, things):
        self.things.update(things)