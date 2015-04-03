__author__ = 'siggyzee'

# item and zombies are only present for testing purposes and will be removed in final code

class Tile:
    def __init__(self, name = "", north = "", east = "", south = "", west = "", item = "", zombies = 0):
        self.type = False
        self.name = name
        self.direction = {"North": north, "South": south, "East": east, "West": west}
        self.zombies = zombies
        self.item = item