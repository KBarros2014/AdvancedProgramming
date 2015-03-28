__author__ = 'Misa'

import cmd

INDOOR = True
OUTDOOR = False


class Tile():
    def __init__(self, name, room_type, north, south, east, west):
        self.name = name
        self.room_type = room_type
        self.directions = {"North": north, "South": south, "East": east, "West": west}


class DevCard():
    def __init__(self, item, number_of_zombies, message):
        self.item = item
        self.number_of_zombies = number_of_zombies
        self.message = message


class Game():
    def __init__(self, time, map_coordination, player_location):
        self.time = time
        self.map_coordination = map_coordination
        self.player_location = player_location
        self.player = Player(6, 1, False, None)

    def reset_game(self):
        pass

    def withdraw_card(self):
        pass

    def add_item(self):
        pass

    def add_tile(self):
        pass

    def display_game_status(self):
        current_room = self.map_coordination.index(self.player_location)
        north_room = self.map_coordination[current_room].directions["North"]
        south_room = self.map_coordination[current_room].directions["South"]
        east_room = self.map_coordination[current_room].directions["East"]
        west_room = self.map_coordination[current_room].directions["West"]

        print "Current location: %s \nCurrent time: %ipm \nPlayer Health: %s \nPlayer Attack: %i " \
              "\nConnections from this room\nNorth Room: %s \nSouth Room: %s \nEast Room: %s \nWest Room: %s \n" \
              % (self.player_location.name, self.time, self.player.health, self.player.attack, north_room, south_room, east_room, west_room)

    def check_game_end_condition(self):
        """
        code for true(when Player has Totem and buried the Totem in Graveyard
        code for true(when Player's health became 0)
        code for true(when the time became 12 o'clock)
        """
        return False

    def get_tile_by_name(self, room_name):
        for tile in self.map_coordination:
            if tile.name == room_name:
                return tile

    def move_north(self):
        current_room = self.map_coordination.index(self.player_location)
        north_room = self.map_coordination[current_room].directions["North"]
        print "Moving player to north"
        self.player_location = self.get_tile_by_name(north_room)
        print "Now Player is at: " + self.player_location.name


class Player():
    def __init__(self, health, attack, has_zombie_totem, item):
        self.health = health
        self.attack = attack
        self.has_zombie_totem = has_zombie_totem
        self.item = item


class Controller(cmd.Cmd):
    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = "Player input"

    def do_north(self, arg):
        Game.move_north()


def main():
    map_coordination = []
    map_coordination.append(Tile("Foyer", INDOOR, "Dining Room", "Blocked", "Blocked", "Blocked"))
    map_coordination.append(Tile("Dining Room", INDOOR, "Patio", "Foyer", "Blocked", "Evil Temple"))
    map_coordination.append(Tile("Evil Temple", INDOOR, "Blocked", "Blocked", "Dining Room", "Blocked"))
    map_coordination.append(Tile("Patio", OUTDOOR, "Yard", "Dining Room", "Blocked", "Blocked"))

    game = Game(9, map_coordination, map_coordination[0])
    controller = Controller()
    if game.check_game_end_condition() == False:
        print "Zombie in my pocket \n"
        game.display_game_status()

        game.move_north()
        #controller.do_north()

main()

