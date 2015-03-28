__author__ = 'siggyzee'
from enum import Enum

from siggy.tile import Tile
from siggy.devcard import Devcard
from siggy.player import Player


class Game:

    map = {}
    game_time = 8
    devcard_controller = None
    player = None
    player_location = None

    def __init__(self, tile, time):

        # Load rooms
        self.roomsDict = {}
        self.roomsDict = {}
        foyer = Tile('foyer', 'dining_room', 'nothing', 'nothing', 'nothing')
        dining_room = Tile('dining_room', 'patio', 'evil_temple', 'foyer', 'nothing')
        evil_temple = Tile('evil_temple', 'nothing', 'nothing', 'nothing', 'dining_room')
        patio = Tile('patio', 'dining_room', 'nothing', 'yard', 'nothing')
        yard = Tile('yard', 'nothing', 'nothing', 'patio', 'grave_yard')
        grave_yard = Tile('grave_yard', 'nothing', 'yard', 'nothing', 'nothing')
        self.map[foyer.name] = foyer
        self.map[dining_room.name] = dining_room
        self.map[evil_temple.name] = evil_temple
        self.map[patio.name] = patio
        self.map[yard.name] = yard
        self.map[grave_yard.name] = grave_yard

        # load Devcard_controller
        devcard_controller = Devcard

        # load player
        self.player = Player(self.map)

        # set current room
        self.player_location = tile

        # set current time
        self.game_time = time

        # display initial game state
        self.display_game_state()

    # returns message if given
    def withdraw_devcard(self):
        cardInfo = self.devcard_controller.pickCard()
        self.game_time = cardInfo[0]
        if cardInfo[1] == 0:
            self.map[self.player_location].item = cardInfo[2]
        if cardInfo[1] == 1:
            self.map[self.player_location].zombies = cardInfo[2]
        if cardInfo[1] == 2:
            return cardInfo[3]

    # print out the current game state
    def display_game_state(self):
        # print locaiton and time information
        print("Location " + self.player.player_location + ", Time " + str(self.game_time) + ".00pm")
        # print item information
        if (self.map[self.player.player_location].item == ""):
            print("There is no item on the floor")
        else:
            print("There is a " + self.map[self.player.player_location].item + "on the floor")
        # number of zombies in the room
        print("There is " + str(self.map[self.player.player_location].zombies) + " zombies in the room")
        # movement options
        print("North there is " + self.map[self.player.player_location].north + ", East there is " + self.map[self.player.player_location].east + ", South there is " + self.map[self.player.player_location].south + ", West there is " + self.map[self.player.player_location].west)
        # print health and attack strength
        print("Your health is " + str(self.player.health) + ", Your attack is " + str(self.player.attack_strength))
        # print current item
        if (self.player.item == ""):
            print("Your not holding an item")
        else:
            print("Your holding a " + self.player.item)
        # print the zombie totem
        if (self.player.has_zombie_totem == False):
            print("Your don't have the Zombie Totem")
        else:
            print("Your have the Zombie Totem")

    def move_player(self, direction):
        self.player.move(direction)
        # self.withdraw_devcard()
        self.display_game_state()




def main():
    game = Game("foyer", 8)

    #print("Hi")
    #game.display_game_state()
    #game.move_player('north')
    #game.display_game_state()
    #game.move_player('east')
    #game.display_game_state()
    #game.move_player('west')
    #game.display_game_state()
    #game.move_player('north')
    #game.display_game_state()

if __name__ == "__main__":
    main()
