__author__ = 'siggyzee'


class Player:
    health = 6
    player_location = 'foyer'
    attack_strength = 1
    has_zombie_totem = False
    item = ""
    map = None

    def __init__(self, map):
        # set local varible refering to games map of tiles
        self.map = map


    def cower(self):
        print("cower")

    def attack(self):
        print("attack")

    def run(self, direction):
        print("run")

    def move(self, direction):
        print("move " + direction)
        if (direction == 'north'):
            if (self.map[self.player_location].north != 'nothing'):
                self.player_location = self.map[self.player_location].north
        if (direction == 'east'):
            if (self.map[self.player_location].east != 'nothing'):
                self.player_location = self.map[self.player_location].east
        if (direction == 'south'):
            if (self.map[self.player_location].south != 'nothing'):
                self.player_location = self.map[self.player_location].south
        if (direction == 'west'):
            if (self.map[self.player_location].west != 'nothing'):
                self.player_location = self.map[self.player_location].west


