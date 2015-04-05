from zimp.devcard import DevCard
from zimp.tile import Tile
import random

class Game:
    def __init__(self, message, ):
        self.game_time = 9
        self.card_count = 0
        self.player_health = 6
        self.player_attack = 1
        self.player_item = "Nothing"
        self.has_zombie_totem = False
        self.devCard = DevCard()
        self.all_tiles = {
            "Foyer":
                Tile("Foyer",
                     "Dining Room", "blocked", "blocked", "blocked",
                     0, "nothing"),
            "Dining Room":
                Tile("Dining Room",
                     "Patio", "Foyer", "blocked", "Evil Temple",
                     0, "nothing"),
            "Evil Temple":
                Tile("Evil Temple",
                     "blocked", "blocked", "Dining Room", "blocked",
                     0, "nothing"),
            "Patio":
                Tile("Patio",
                     "Yard", "Dining Room", "blocked", "blocked",
                     0, "nothing"),
            "Yard":
                Tile("Yard",
                     "blocked", "Patio", "blocked", "Graveyard",
                     0, "nothing"),
              "Graveyard":
                Tile("Graveyard",
                     "blocked", "blocked", "blocked", "Yard",
                     0, "nothing")}
        self.all_items = {"Board with Nails": 1,
                          "Machete": 2,
                          "Grisly Femur": 1,
                          "Golf Club": 1,
                          "Chainsaw": 3}
        self.player_location = self.all_tiles.get_tile()


    def withdraw_devCard(self):
        random_card = self.devcard.pick_card()
        if random_card[0] == 0:
            self.player_location.item = random_card[1]
        elif random_card[0] == 1:
            self.player_location.zombies = random_card[1]
        else:
            print("\n" + random_card[1])

            self.update_game_time()
            self.check_game_end_condition()


    def display_game_state(self):
        pass

    def move_player(self, direction):
        if self.player_location

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

    def attack(self):
        pass

    def check_game_end_condition(self):
        pass

    def update_game_time(self):
        pass

    def run(self, direction):
        pass

    def cower(self):
        pass

    def get_totem(self):
        pass

    def bury_totem(self):
        pass

