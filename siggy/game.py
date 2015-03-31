__author__ = 'siggyzee'
from enum import Enum

from siggy.tile import Tile
from siggy.devcard import Devcard
import sys

#from siggy.player import Player


class Game:

    map = {}
    items = {}
    game_time = 8
    devcard_controller = None
    player = None
    player_location = 'Foyer'
    health = 6
    attack_strength = 1
    has_zombie_totem = False
    item = ""
    card_count = 0

    def __init__(self):

        # Load rooms
        foyer = Tile('Foyer', 'Dining Room', 'blocked', 'blocked', 'blocked')
        dining_room = Tile('Dining Room', 'Patio', 'Evil Temple', 'Foyer', 'blocked')
        evil_temple = Tile('Evil Temple', 'blocked', 'blocked', 'blocked', 'Dining Room')
        patio = Tile('Patio', 'Yard', 'blocked', 'Dining Room', 'blocked', '', 2)
        yard = Tile('Yard', 'blocked', 'blocked', 'Patio', 'Graveyard', 'Board with Nails', 3)
        grave_yard = Tile('Graveyard', 'blocked', 'Yard', 'blocked', 'blocked', '', 1)
        self.map[foyer.name] = foyer
        self.map[dining_room.name] = dining_room
        self.map[evil_temple.name] = evil_temple
        self.map[patio.name] = patio
        self.map[yard.name] = yard
        self.map[grave_yard.name] = grave_yard

        # Load items
        self.items['Board with Nails'] = 1
        self.items['Grisly Femur'] = 1
        self.items['Golf Club'] = 1
        self.items['Chainsaw'] = 3
        self.items['Machete'] = 2


        # load Devcard_controller
        devcard_controller = Devcard


        # display initial game state
        self.display_game_state()


    # returns message if given
    def withdraw_devcard(self):
        cardInfo = self.devcard_controller.pickCard()
        if cardInfo[0] == 0:
            self.map[self.player_location].item = cardInfo[1]
        if cardInfo[0] == 1:
            self.map[self.player_location].zombies = cardInfo[1]
        if cardInfo[0] == 2:
            return print(cardInfo[1])
        self.update_game_time()
        self.check_game_end_condition()


    # display_game_state
    #
    # print out the current game state as per specification in google doc file
    # https://docs.google.com/document/d/1a9QeibvSWzbfF02yLp4au0XBqy3PZAAp66WyF5A4Nt0/edit
    #
    def display_game_state(self):

        # print locaiton and time information
        print("Location " + self.player_location + ", Time " + str(self.game_time) + ".00pm")

        # print item information
        if (self.map[self.player_location].item == ""):
            print("There is no item on the floor")
        else:
            print("There is a " + self.map[self.player_location].item + " on the floor")

        # number of zombies in the room
        print("There is " + str(self.map[self.player_location].zombies) + " zombies in the room")

        # movement options
        print("North there is " + self.map[self.player_location].north + ", East there is " +
              self.map[self.player_location].east + ", South there is " +
              self.map[self.player_location].south + ", West there is " +
              self.map[self.player_location].west)

        # print health and attack strength
        print("Your health is " + str(self.health) + ", Your attack is " + str(self.attack_strength))

        # print current item
        if (self.item == ""):
            print("Your not holding an item")
        else:
            print("Your holding a " + self.item)

        # print the zombie totem
        if (self.has_zombie_totem == False):
            print("Your don't have the Zombie Totem")
        else:
            print("Your have the Zombie Totem")



    # move_player(String direction)
    #   takes movement direction as a string of either (north; east; south; west)
    #
    #   returns False is movement not possible
    #   returns True is movement is successful
    #
    def move_player(self, direction):
        if (self.map[self.player_location].zombies > 0):
            print("You can't move normally while zombies are present.")
            return False
        if (direction == 'north'):
            if (self.map[self.player_location].north != 'blocked'):
                self.player_location = self.map[self.player_location].north
            else: return False
        if (direction == 'east'):
            if (self.map[self.player_location].east != 'blocked'):
                self.player_location = self.map[self.player_location].east
            else: return False
        if (direction == 'south'):
            if (self.map[self.player_location].south != 'blocked'):
                self.player_location = self.map[self.player_location].south
            else: return False
        if (direction == 'west'):
            if (self.map[self.player_location].west != 'blocked'):
                self.player_location = self.map[self.player_location].west
            else: return False
        # if player moved update game state
        self.display_game_state()
        return True


    # get_item()
    #   pickup and item from the floor in a tile
    #
    #   returns False when there is no item
    #   returns True if items has been pickedup
    #
    def get_item(self):
        # check an item is present
        if (self.map[self.player_location].item == ""):
            return False
        # set new item
        self.item = self.map[self.player_location].item
        # set new attack strength
        self.attack_strength = 1 + self.items[self.item]
        self.map[self.player_location].item = ""
        self.display_game_state()
        return True


    # attack()
    #   attach zombies currently in the room
    #
    #   returns False when there is no item
    #   returns True if items has been pickedup
    #
    def attack(self):
        # calculate health lost
        health_lost = self.map[self.player_location].zombies - self.attack_strength
        # cap health lost to 4 points
        if (health_lost > 4): health_lost = 4
        # update health
        self.health = self.health - health_lost
        # update zombies in room
        self.map[self.player_location].zombies = 0

        self.check_game_end_condition()
        self.display_game_state()


    # check_game_end_condition()
    #   see if game is lost or won
    #
    #   prints message and ends game if game is either won or lost
    #   returns True if game is continuing
    #   returns False (this should never happen)
    #
    def check_game_end_condition(self):
        # check still alive
        if self.health <= 0:
            print("Zombies have eaten your brains - Game Over.")
            sys.exit()
        if self.game_time == 12:
            print("You have been over run by the zombie horde - Game Over")
            sys.exit()
        return True


    # update_game_time()
    #
    #
    def update_game_time(self):
        # update card stack and time
        self.card_count += 1
        if (self.card_count >= 8):
            self.game_time += 1
            self.card_count = 1









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
