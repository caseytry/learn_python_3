class Room(object):

    def __init__(self, name, description):
        self.name = name
        self.description =  description
        self.paths = {}
 #my add
        self.things = {}

    def go(self, direction):
        return self.paths.get(direction, None)
    
    def add_paths(self, paths):
        self.paths.update(paths)

#my add
    def see(self, thing):
#        return self.things[thing]
        return thing in self.things

    def add_things(self, things):
        self.things.update(things)