__author__ = 'siggyzee'
from enum import Enum

from siggy.tile import Tile
from siggy.devcard import Devcard
from siggy.player import Player



class Direction(Enum):
    north = 1
    east = 2
    south = 3
    west = 4


class Game:

    map = {}
    game_time = 8
    devcard_controller = None
    player = None
    player_location = None

    def __init__(self, tile, time):

        # Load rooms
        self.roomsDict = {}
        foyer = Tile("foyer", 1, 0, 0, 0)
        dining_room = Tile("dining_room", 1, 1, 1, 0)
        evil_temple = Tile("evil_temple", 0, 0, 0, 1)
        patio = Tile("patio", 1, 0, 1, 0)
        yard = Tile("yard", 0, 0, 1, 1)
        grave_yard = Tile("grave_yard", 0, 1, 0, 0)
        self.map[foyer.name] = foyer
        self.map[dining_room.name] = dining_room
        self.map[evil_temple.name] = evil_temple
        self.map[patio.name] = patio
        self.map[yard.name] = yard
        self.map[grave_yard.name] = grave_yard

        # load Devcard_controller
        devcard_controller = Devcard

        # load player
        self.player = Player()

        # set current room
        self.player_location = tile

        # set current time
        self.game_time = time

    # returns message if given
    def withdraw_devcard(self):
        cardInfo = self.devcard_controller.pickCard()
        if cardInfo[1] == 0:
            self.map[self.player_location].item = cardInfo[2]
        if cardInfo[1] == 1:
            self.map[self.player_location].zombies = cardInfo[2]
        if cardInfo[1] == 2:
            return cardInfo[3]


def main():
    game = Game("foyer", 8)


if __name__ == "__main__":
    main()
