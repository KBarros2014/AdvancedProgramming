__author__ = 'Misa'

import cmd
import random
import sys
import pickle


class Controller(cmd.Cmd):
    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = "Enter your command: \n"
        self.game = Game()

    def start_game(self):
        self.game.display_game_status()

    def do_attack(self, line):
        """
        Attack zombies in player's current location
        """
        if self.game.attack():
            print ("\nYou survived the zombie attack")
            self.game.display_game_status()
        else:
            print ("\nFortunately there are no zombies here\n")

    def do_run(self, direction):
        """
        Escape from zombies by running to north, south, east or west. Type run direction
        """
        if self.game.run(direction):
            print ("\nYou ran away from the zombies. You got scratched!")
            self.game.display_game_status()
        else:
            print ("\nYou failed to run\n")

    def do_cower(self, line):
        """
        Hide and heal 3 health points but lose some time.
        """
        if self.game.cower():
            print ("\nYou hid in the corner and rested a while")
            self.game.display_game_status()
        else:
            print ("\nThere are zombies here!\n")

    def do_move(self, direction):
        """
        Move player to north, south, east or west. Type move direction
        """
        if self.game.move(direction):
            print ("\nYou are moving to " + direction)
            self.game.display_game_status()

    def do_get_totem(self, line):
        """
        Retrieve the Zombie Totem(Only possible in Evil Temple)
        """
        if self.game.get_totem():
            print ("\nYou found the Zombie Totem!!")
            self.game.display_game_status()
        else:
            print ("\nThe Zombie Totem will be in the Evil Temple, not here!\n")

    def do_bury_totem(self, line):
        """
        Bury the Zombie Totem(Only possible in Graveyard)
        """
        if self.game.bury_totem():
            print ("\nYou have successfully buried the Zombie Totem!\n")
            sys.exit()
        else:
            print ("\nYou can't do that!\n")

    def do_get_item(self, line):
        """
        Retrieve an item from the player's current location
        """
        if self.game.get_item():
            self.game.display_game_status()
        else:
            print ("\nYou couldn't find anything useful\n")

    def do_save(self, line):
        """
        Save the current game state to Save folder with given name.
        Uses savedata as default file name if no name given.
        """
        if len(line) == 0:
            line = "savedata"
        output = open("Save/" + line, "wb")
        pickle.dump(self.game, output)
        print("Game saved in Save folder: " + line + "\n")
        output.close()

    def do_load(self, line):
        """
        Load the existing saved game state from Save folder
        """
        if len(line) == 0:
            line = "savedata"
        else:
            print ("Invalid file name")
        loaded_game = open("Save/" + line, "rb")
        self.game = pickle.load(loaded_game)
        print("\nGame loaded from Save folder: " + line)
        self.game.display_game_status()

    def do_help(self, line):
        print ("\nhelp help??\n")


class Game():
    def __init__(self):
        self.game_time = 9
        self.count_cards = 0
        self.all_tiles = {
            "Foyer": Tile("Foyer", "Dining Room", "blocked", "blocked", "blocked", 2, "nothing"),
            "Dining Room": Tile("Dining Room", "Patio", "Foyer", "blocked", "Evil Temple", 0, "nothing"),
            "Evil Temple": Tile("Evil Temple", "blocked", "blocked", "Dining Room", "blocked", 0, "nothing"),
            "Patio": Tile("Patio", "Yard", "Dining Room", "blocked", "blocked", 0, "nothing"),
            "Yard": Tile("Yard", "blocked", "Patio", "blocked", "Graveyard", 0, "nothing"),
            "Graveyard": Tile("Graveyard", "blocked", "blocked", "blocked", "Yard", 0, "nothing")
            }
        self.all_items = {"Board with Nails": 1, "Machete": 2, "Grisly Femur": 1, "Golf Club": 1, "Chainsaw": 3}
        self.player_location = self.all_tiles.get("Foyer")
        self.player_health = 6
        self.player_attack = 1
        self.player_item = "nothing"
        self.has_zombie_totem = False
        self.devcard = DevCard()

    def get_item(self):
        if self.player_location.item is not "nothing":
            self.player_item = self.player_location.item
            item_strength = self.all_items.get(self.player_item)
            self.player_attack += item_strength
            print ("\nYou found a " + self.player_item)
            self.player_location.item = "nothing"
            self.update_game_time()
            return True
        else:
            return False

    def withdraw_card(self):
        random_card = self.devcard.pick_card()

        if random_card[0] == 0:
            self.player_location.item = random_card[1]
        elif random_card[0] == 1:
            self.player_location.zombies = random_card[1]
        else:
            print ("\n" + random_card[1])

        self.update_game_time()
        self.check_game_end_condition()

    def display_game_status(self):
        current_room = self.player_location.name
        north_room = self.all_tiles.get(current_room).direction.get("North")
        south_room = self.all_tiles.get(current_room).direction.get("South")
        east_room = self.all_tiles.get(current_room).direction.get("East")
        west_room = self.all_tiles.get(current_room).direction.get("West")

        print ("\n========================\nYou are in the %s \nThe time is %ipm \n"
               "\nYour Health is %s \nYour Attack is %i \n\nYou have %s with you \n"
               "There is a %s on the ground \nThere are %i zombies \n\n---Connections from this room---\n"
               "North Room is %s \nSouth Room is %s \nEast Room is %s \nWest Room is %s \n"
               % (current_room, self.game_time, self.player_health, self.player_attack,
                  self.player_item, self.player_location.item, self.player_location.zombies,
                  north_room, south_room, east_room, west_room))
        if self.has_zombie_totem:
            print ("You have the Zombie Totem and now you need to go to the Graveyard\n========================\n")
        else:
            print ("You need to go to Evil Temple and search for the Zombie Totem\n========================\n")

    def attack(self):
        numbers_of_zombies = self.player_location.zombies
        damage = numbers_of_zombies - self.player_attack
        if damage > 4:
            damage = 4
        if numbers_of_zombies > 0:
            self.player_health -= damage
            self.player_location.zombies = 0
            self.check_game_end_condition()
            return True
        else:
            return False

    def run(self, direction):
        current_room = self.player_location
        zombies_in_room = self.player_location.zombies
        next_room = current_room.direction.get(direction.capitalize())
        if direction != "north" and direction != "east" and direction != "south" and direction != "west":
            print ("\nMove to where? Give direction: north, south, east or west\n")
            return False
        if zombies_in_room > 0 and next_room is not "blocked":
            self.player_health -= 1
            self.player_location = self.all_tiles[next_room]
            self.withdraw_card()
            return True
        else:
            return False

    def cower(self):
        if self.player_location.zombies <= 0:
            self.update_game_time()
            self.player_health += 3
            return True
        else:
            return False

    def move(self, direction):
        current_room = self.player_location
        zombies_in_room = self.player_location.zombies
        next_room = current_room.direction.get(direction.capitalize())
        if direction != "north" and direction != "east" and direction != "south" and direction != "west":
            print ("\nMove to where? Give direction: north, south, east or west\n")
            return False
        if zombies_in_room == 0 and next_room is not "blocked":
            self.player_location = self.all_tiles[next_room]
            self.withdraw_card()
            return True
        else:
            print ("\nYou can't do that!\n")
            return False

    def check_game_end_condition(self):
        if self.player_health <= 0:
            print("\nZombies have eaten your brains. Game over!\n")
            sys.exit()
        elif self.game_time >= 12:
            print("\nYou have run out of time and been overrun by the zombie horde. Game over!\n")
            sys.exit()
        return False

    def get_totem(self):
        if self.player_location.name == "Evil Temple":
            self.has_zombie_totem = True
            return True
        else:
            return False

    def bury_totem(self):
        if self.player_location.name == "Graveyard":
            if self.player_location.zombies == 0:
                if self.has_zombie_totem:
                    return True
        else:
            return False

    def update_game_time(self):
        self.count_cards += 1
        if self.count_cards >= 3:
            self.game_time += 1
            self.count_cards = 0
            print ("\nIt is now %ipm" % self.game_time)
            self.check_game_end_condition()


class Tile():
    def __init__(self, name, north, south, east, west, zombies, item):
        self.name = name
        self.direction = {"North": north, "South": south, "East": east, "West": west}
        self.zombies = zombies
        self.item = item


class DevCard():
    def __init__(self):
        self.items = ["Board with nails", "Machete", "Grisly Femur", "Golf Club", "Chainsaw"]
        self.numbers_of_zombies = [6, 4, 4, 4, 6, 5, 4, 3, 5, 4, 4]
        self.messages = ["You try hard not to wet yourself", "You sense your impending DOOM",
                         "Something icky in your mouth", "A bat poops in your eye",
                         "Your soul isn't wanted here", "The smell of blood is in the air.",
                         "You hear terrible screams", "Your body shivers involuntarily", "You feel a sparkle of Hope"]

    def pick_card(self):
        random_value = random.randint(0, 2)

        if random_value == 0:
            random_item = random.choice(self.items)
            return random_value, random_item
        elif random_value == 1:
            random_zombies = random.choice(self.numbers_of_zombies)
            return random_value, random_zombies
        else:
            random_message = random.choice(self.messages)
            return random_value, random_message


def main():
    controller = Controller()
    controller.start_game()
    controller.cmdloop()


if __name__ == '__main__':
    main()


