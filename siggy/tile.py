__author__ = 'siggyzee'
__name__ = "tile"
__package__ = "gimp_game"
class Tile:
    def __init__(self, name = "", north = 0, east = 0, south = 0, west = 0):
        self.type = False
        self.name = name
        self.north = north
        self.east = east
        self.south = south
        self.west = west
        self.zombies = 0
        self.item = ""