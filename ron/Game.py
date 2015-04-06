from Tile import *
from DevCard import *
import sys

class Game():
    def __init__(self):
        self.player_health = 6
        self.player_attack = 1
        self.all_tiles = {
            "Foyer": Tile("Foyer","Dining Room", "blocked", "blocked", "blocked", 0, "None"),
            "Dining Room": Tile("Dining Room", "Patio", "Foyer", "blocked", "Evil Temple", 0, "None"),
            "Evil Temple": Tile("Evil Temple", "blocked", "blocked", "Dining Room", "blocked", 0, "None"),
            "Patio": Tile("Patio", "Yard", "Dining Room", "blocked", "blocked", 0, "None"),
            "Yard": Tile("Yard", "blocked", "Patio", "blocked", "Graveyard", 0, "None"),
            "Graveyard": Tile("Graveyard", "blocked", "blocked", "blocked", "Yard", 0, "None")}			
        self.game_time = 9
        self.card_count = 0				
        self.all_items = {"Board with Nails": 1, "Machete": 2, "Grisly Femur": 1, "Golf Club": 1, "Chainsaw": 3}
        self.player_location = self.all_tiles.get("Foyer")       
        self.player_item = "Bare fist"
        self.has_zombie_totem = False
        self.devcard = DevCard()
		
    def get_item(self):
        if self.player_location.item is not "None":          
            print ("\nYou picked up a " + self.player_location.item)
            self.player_item = self.player_location.item
            self.player_attack = 1 + self.all_items[self.player_item]
            self.player_location.item = "None"
            self.update_game_time()
            return True
        else:
            return False

    def withdraw_card(self):
        selected = self.devcard.pick_card()
        if selected[0] == 0:
            self.player_location.item = selected[1]
        elif selected[0] == 1:
            self.player_location.zombies = selected[1]
        else:
            print ("\n" + selected[1])
        self.update_game_time()
        self.check_game_end_condition()

    def display_game_status(self):
        location = self.player_location.name
        north = self.all_tiles.get(location).direction.get("North")
        south = self.all_tiles.get(location).direction.get("South")
        east = self.all_tiles.get(location).direction.get("East")
        west = self.all_tiles.get(location).direction.get("West")

        print ("\n## Starting status message ##\n")
        print ("\nCurrent time:" + str(self.game_time) + "\n")
        print ("Current location: " + location + "\n")
        print ("North: " + north + "\n")
        print ("South: " + south + "\n")
        print ("East: " + east + "\n")
        print ("West: " + west + "\n")
        print ("Room item: " + self.player_location.item + "\n")
        print ("ZOmbies in room: " + str(self.player_location.zombies) + "\n")
        print ("HP: " + str(self.player_health) + "\n")
        print ("Attack: " + str(self.player_attack) + "\n")		
        print ("Weapon: " + self.player_item + "\n")
        print ("Has totem: " + str(self.has_zombie_totem) + "\n")
        print ("\n## End of status message ##\n")

    def attack(self):
        hit = self.player_location.zombies - self.player_attack
        if hit > 4: hit = 4
        if hit < 0: hit = 0
        if self.player_location.zombies > 0:
            self.player_health = self.player_health - hit
            self.player_location.zombies = 0
            self.check_game_end_condition()
            return True
        else:
            return False

    def run(self, direction):     
        if direction != "north" and direction != "east" and direction != "south" and direction != "west":
            print ("\nPlease specify direction\n")
            return False
        next_room = self.player_location.direction[direction.capitalize()]
        if self.player_location.zombies > 0 and next_room is not "blocked":
            self.player_health -= 1
            self.player_location = self.all_tiles[next_room]
            self.withdraw_card()
            return True
        else:
            print ("\nThere are no zombies or direct is blocked\n")
            return False

    def cower(self):
        if self.player_location.zombies <= 0:
            self.update_game_time()
            self.player_health += 3
            return True
        else:
            return False

    def move(self, direction):        
        if direction != "north" and direction != "east" and direction != "south" and direction != "west":
            print ("\nPlease specify direction\n")
            return False
        next_room = self.player_location.direction[direction.capitalize()]	
        if self.player_location.zombies == 0 and next_room is not "blocked":
            self.player_location = self.all_tiles[next_room]
            self.withdraw_card()
            return True
        else:
            print ("\nIt's block or there are zombies here!\n")	
            return False

    def check_game_end_condition(self):
        if self.player_health <= 0:
            print("\nHP 0. You lost!\n")
            sys.exit()
        elif self.game_time >= 12:
            print("\nTimes up. You lost!\n")
            sys.exit()
        return False

    def get_totem(self):
        if self.player_location.name == "Evil Temple":
            self.has_zombie_totem = True
            return True
        else:
            return False

    def bury_totem(self):
        if self.player_location.name == "Graveyard" and self.player_location.zombies == 0 and self.has_zombie_totem:
            return True
        else:
            return False

    def update_game_time(self):
        self.card_count += 1
        if self.card_count >= 4:
            self.game_time += 1
            self.card_count = 0
            self.check_game_end_condition()