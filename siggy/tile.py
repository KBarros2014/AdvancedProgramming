__author__ = 'siggyzee'

# item and zombies are only present for testing purposes and will be removed in final code

class Tile:
    def __init__(self, name = "", north = "", east = "", south = "", west = "", item = "", zombies = 0):
        self.type = False
        self.name = name
        self.north = north
        self.east = east
        self.south = south
        self.west = west
        self.zombies = zombies
        self.item = item