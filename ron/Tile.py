class Tile():
    def __init__(self, name, north, south, east, west, zombies, item):
        self.name = name
        self.direction = {"North": north, "South": south, "East": east, "West": west}
        self.zombies = zombies
        self.item = item