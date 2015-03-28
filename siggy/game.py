__author__ = 'siggyzee'

from siggy.tile import Tile
from siggy.devcard import Devcard
from siggy.player import Player




class Game:

    map = {}
    game_time = 8
    devcard_controller = None
    player = None

    def __init__(self, tile, time):

        # Load rooms
        self.roomsDict = {}
        foyer = Tile("Foyer", 1, 0, 0, 0)
        diningRoom = Tile("Dining Room", 1, 1, 1, 0)
        evilTemple = Tile("Evil Temple", 0, 0, 0, 1)
        patio = Tile("Patio", 1, 0, 1, 0)
        yard = Tile("Yard", 0, 0, 1, 1)
        graveYard = Tile("Graveyard", 0, 1, 0, 0)
        self.map[foyer.name] = foyer
        self.map[diningRoom.name] = diningRoom
        self.map[evilTemple.name] = evilTemple
        self.map[patio.name] = patio
        self.map[yard.name] = yard
        self.map[graveYard.name] = graveYard

        # Load Devcard_controller
        devcard_controller = Devcard

        #Load player
        self.player = Player()

        # set current room
        self.location = tile

        # set current time
        self.game_time = time



def main():
    game = Game("Foyer", 8)


if __name__ == "__main__":
    main()
