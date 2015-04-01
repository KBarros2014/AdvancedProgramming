__author__ = 'Misa'

import cmd
import random
import sys


class Controller(cmd.Cmd):
    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = "Enter your command: \n"
        self.game = Game()

    def start_game(self):
        self.game.display_game_status()
        pass

    def end_game(self):
        self.postloop()
        pass

    def do_attack(self, line):
        if self.game.attack():
            print ("\nYou survived the zombie attack")
            self.game.display_game_status()
        else:
            print ("\nFortunately there are no zombies here\n")

    def do_run(self, direction):
        if self.game.run(direction):
            print ("\nYou ran away from the zombies. You got scratched!")
            self.game.display_game_status()
        else:
            print ("\nThere seen to be no zombies. Calm yourself\n")

    def do_cower(self, line):
        if self.game.cower():
            print ("\nYou hid in the corner and rested a while")
            self.game.display_game_status()
        else:
            print ("\nThere are zombies here!\n")

    def do_move(self, direction):
        validate = self.game.check_direction(direction)
        if validate:
            if self.game.move(direction):
                print ("\nYou are moving to " + self.game.player_location.name)
                self.game.display_game_status()
        else:
            print ("\nYou can't do that!\n")

    def do_get_totem(self, line):
        if self.game.get_totem():
            print ("You found the Zombie Totem!!")
            self.game.display_game_status()
        else:
            print ("\nThe Zombie Totem will be in the Evil Temple, not here!\n")

    def do_bury_totem(self, line):
        if self.game.bury_totem():
            print ("\nYou have successfully buried the Zombie Totem!\n")
            sys.exit()
        else:
            print ("\nYou can't do that!\n")

    def do_get_item(self, line):
        if self.game.get_item():
            self.game.display_game_status()
        else:
            print ("\nYou couldn't find anything useful\n")

    def do_save(self, line):
        pass

    def do_load(self, line):
        pass


class Game():
    def __init__(self):
        self.game_time = 9
        self.count_cards = 0
        self.all_tiles = {
            "Foyer": Tile("Foyer", "Dining Room", "Blocked", "Blocked", "Blocked", 6, "Board with Nails"),
            "Dining Room": Tile("Dining Room", "Patio", "Foyer", "Blocked", "Evil Temple", 0, "nothing"),
            "Evil Temple": Tile("Evil Temple", "Blocked", "Blocked", "Dining Room", "Blocked", 0, "nothing"),
            "Patio": Tile("Patio", "Yard", "Dining Room", "Blocked", "Blocked", 0, "nothing"),
            "Yard": Tile("Yard", "Blocked", "Patio", "Blocked", "Graveyard", 0, "nothing"),
            "Graveyard": Tile("Graveyard", "Blocked", "Blocked", "Blocked", "Yard", 0, "nothing")
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
            print ("\nYou found a " + self.player_location.item)
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
        if current_room.zombies > 0:
            current_room.zombies = 0
            self.player_health -= 1
            self.move(direction)
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

    def check_direction(self, direction):
        current_room = self.player_location
        connection = {
            "north": self.all_tiles.get(current_room.name).direction.get("North"),
            "south": self.all_tiles.get(current_room.name).direction.get("South"),
            "east": self.all_tiles.get(current_room.name).direction.get("East"),
            "west": self.all_tiles.get(current_room.name).direction.get("West")
            }
        next_room = connection.get(direction)
        if next_room is "Blocked":
            return False
        else:
            return True

    def move(self, direction):
        current_room = self.player_location
        if current_room.zombies == 0:
            connection = {
                "north": self.all_tiles.get(current_room.name).direction.get("North"),
                "south": self.all_tiles.get(current_room.name).direction.get("South"),
                "east": self.all_tiles.get(current_room.name).direction.get("East"),
                "west": self.all_tiles.get(current_room.name).direction.get("West")
                }
            next_room = connection.get(direction)
            self.player_location = self.all_tiles[next_room]
            self.withdraw_card()
            return True
        else:
            print ("\nThere are zombies in the room!\n")
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
        if self.player_location == "Graveyard":
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

    def save(self):
        pass

    def load(self):
        pass


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


