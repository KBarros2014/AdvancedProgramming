__author__ = 'siggyzee'


class Tile:
    def __init__(self, name="", north="", east="", south="", west=""):
        self.type = False
        self.name = name
        self.direction = {"North": north, "South": south,
                          "East": east, "West": west}
        self.item = ''
        self.zombies = 0
