__author__ = 'siggyzee'
import sys
import cmd
import pickle
import argparse
import random


class controller(cmd.Cmd):
    def __init__(self):
        cmd.Cmd.__init__(self)
        self.intro = 'Welcome to Zimp \n'
        self.prompt = 'Enter your command: \n'
        self.game = Game()

    def start_game(self):
        self.game.display_game_status()

    def do_move(self, direction):
        print('move', direction)
        result = self.game.move(direction.capitalize())
        if (not result):
            print('You can’t move in that direction or when there are' +
                  ' zombies in the room.')
        else:
            print('You move ' + direction + '.')
            self.game.display_game_status()

    def do_run(self, direction):
        print('run ', direction)
        result = self.game.run(direction.capitalize())
        if (not result):
            print('You can’t run in that direction or when there are no' +
                  ' zombies in the room.')
        else:
            print('You run ' + direction + '.')
            self.game.display_game_status()

    def do_attack(self, line):
        print('attack')
        result = self.game.attack()
        if (not result):
            print('You can\'t attack when there are no zombies.')
        else:
            print('You survived the zombie attack!!')
            self.game.display_game_status()

    def do_cower(self, line):
        print('cower')
        result = self.game.cower()
        if (not result):
            print('You can\'t cower when there is zombies in the room.')
        else:
            print('You cower and regain +3 health.')
            self.game.display_game_status()

    def do_get_item(self, line):
        print('get_item')
        result = self.game.get_item()
        if (not result):
            print('There is no item in the current room.')
        else:
            print('You picked up the item')
            self.game.display_game_status()

    def do_get_totem(self, line):
        print('get totem')
        result = self.game.get_totem()
        if (not result):
            print('You can\'t retrieve the Zombie totem unless you are' +
                  ' in the Evil Temple and there are no Zombies.')
        else:
            print('You picked up the Zombie totem.')
            self.game.display_game_status()

    def do_bury_totem(self, line):
        print('bury totem')
        result = self.game.bury_totem()
        if (not result):
            print('You can only bury the totem in the Graveyard when ' +
                  ' there are no Zombies.')
        else:
            print('You win. The veil of darkness has ' +
                  'lifted, the smell of death leaves!!')
            sys.exit()

    def help_run(self):
        print('run <Direction> 	- Escape zombies by running <Direction>' +
              '. <Direction> = North, East, South, West')

    def help_attack(self):
        print('attack			    - Attack zombies in current room.')

    def help_cower(self):
        print('cower		  	    - Hide in current room and not ' +
              'move this turn.')

    def help_get_item(self):
        print('get_item		    - Retrieve weapon from current room.')

    def help_get_totem(self):
        print('get_totem		    - Retrieve totem (Only' +
              ' in Evil Temple).')

    def help_bury_totem(self):
        print('bury_totem		    - Bury totem (Only in ' +
              'graveyard).')

    def help_save(self):
        print('save <path>		    - Save current game to <path>.')

    def help_load(self):
        print('load <path>		    - ZLoad game from <path>.')

    def help_quit(self):
        print('quit			    - Quit game.')

    def help_move(self):
                print('move <Direction>	- Move player <Direction>. <Direction> ' +
              '= North, East, South, West')


    def do_save(self, save_string):
        try:
            if (save_string == ''):
                save_string = 'mygame'
            output_file = open(save_string, 'wb')
            pickle.dump(self.game, output_file)
            print('Game saved to ' + save_string)
            output_file.close()
        except Exception as err:
            print(err)
            print('You must enter a file name and/or path to' +
                  ' save too relative to the current directory.')
            print('Eg. ./save/myGameData.dat')


    def do_load(self, load_string):
        try:
            input_file = open(load_string, 'rb')
            self.game = pickle.load(input_file)
            print('Loaded game from ' + load_string)
            self.game.display_game_status()
        except (IOError, pickle.UnpicklingError):
            print('There was an error loading your file ' +
                  load_string + ', please check the path' +
                  ' and file format are correct.')
            return False

    def do_quit(self, line):
        return True


class Tile:
    def __init__(self, name="", north="", east="", south="", west=""):
        self.type = False
        self.name = name
        self.direction = {"North": north, "South": south,
                          "East": east, "West": west}
        self.item = 'nothing'
        self.zombies = 0


class Devcard:
    items = ['Board with Nails', 'Machete', 'Grisly Femur',
             'Golf Club', 'Chainsaw']
    numbers_of_zombies = [6, 4, 4, 4, 6, 5, 4, 3, 5, 4, 4]
    messages = ['You try hard not to wet yourself',
                'You sense your impending DOOM',
                'Something icky in your mouth',
                'A bat poops in your eye',
                'Your soul isn\'t wanted here',
                'The smell of blood is in the air.',
                'You hear terrible screams',
                'Your body shivers involuntarily',
                'You feel a sparkle of Hope']

    def pick_card(self):
        # radomly pick and return dev card values
        return_type = random.randint(0, 2)
        # return  an item
        if (return_type == 0):
            return_number = random.randint(0, len(self.items) - 1)
            return (0, self.items[return_number])
        # return a number of zombies
        if (return_type == 1):
            return_number = random.randint(0, len(self.numbers_of_zombies) - 1)
            return (1, self.numbers_of_zombies[return_number])
        # return a message
        if (return_type == 2):
            return_number = random.randint(0, len(self.messages) - 1)
            return (2, self.messages[return_number])


class Game:
    all_tiles = {}
    all_items = {}
    devcard_controller = None

    # player variables
    player_location = None
    player_health = 6
    player_attack = 1
    player_item = ''
    has_zombie_totem = False

    # time handling
    game_time = 8
    card_count = 0

    def __init__(self):
        # Load rooms
        foyer = Tile('Foyer', 'Dining Room', 'blocked', 'blocked', 'blocked')
        dining_room = Tile('Dining Room', 'Patio', 'Evil Temple',
                           'Foyer', 'blocked')
        evil_temple = Tile('Evil Temple', 'blocked', 'blocked',
                           'blocked', 'Dining Room')
        patio = Tile('Patio', 'Yard', 'blocked', 'Dining Room', 'blocked')
        yard = Tile('Yard', 'blocked', 'blocked', 'Patio',
                    'Graveyard')
        grave_yard = Tile('Graveyard', 'blocked', 'Yard', 'blocked', 'blocked')
        self.all_tiles[foyer.name] = foyer
        self.all_tiles[dining_room.name] = dining_room
        self.all_tiles[evil_temple.name] = evil_temple
        self.all_tiles[patio.name] = patio
        self.all_tiles[yard.name] = yard
        self.all_tiles[grave_yard.name] = grave_yard

        # Load items
        self.all_items['Board with Nails'] = 1
        self.all_items['Grisly Femur'] = 1
        self.all_items['Golf Club'] = 1
        self.all_items['Chainsaw'] = 3
        self.all_items['Machete'] = 2

        # load Devcard_controller
        self.devcard_controller = Devcard()

        self.player_location = self.all_tiles['Foyer']

    # returns message if given
    def withdraw_card(self):
        self.update_game_time()
        cardInfo = self.devcard_controller.pick_card()
        if cardInfo[0] == 0:
            self.player_location.item = cardInfo[1]
        if cardInfo[0] == 1:
            self.player_location.zombies = cardInfo[1]
        if cardInfo[0] == 2:
            return print(cardInfo[1])

    def display_game_status(self):
        print('Location %s, Time %d.00pm' % (self.player_location.name, self.game_time))
        print('There is a %s on the floor' % self.player_location.item)
        print('There is %d zombies in the room' % self.player_location.zombies)
        print('North room is %s, East room is %s, South room is %s, West room is %s'
               % (self.player_location.direction['North'], self.player_location.direction['East'],
                  self.player_location.direction['South'], self.player_location.direction['West']))
        print('Your health is %d, Your attack is %d' % (self.player_health,
                                                        self.player_attack))
        if (self.player_item == ''):
            print('Your not holding an item')
        else:
            print('Your holding a %s' % self.player_item)
        if (not self.has_zombie_totem):
            print('Your don\'t have the Zombie Totem')
        else:
            print('Your have the Zombie Totem')
        print('')

    def move(self, direction):
        if (self.player_location.zombies != 0):
            return False
        if (direction not in ('North', 'East', 'South', 'West')):
            return False
        if (self.player_location.direction[direction] != 'blocked'):
            self.player_location = self.all_tiles[
                self.player_location.direction[direction]]
        else:
            return False
        self.withdraw_card()
        return True

    def get_item(self):
        # check an item is present
        if (self.player_location.item == ''):
            return False
        # set new item
        self.player_item = self.player_location.item
        # set new attack strength
        self.player_attack = 1 + self.all_items[self.player_item]
        self.player_location.item = ''
        return True

    def attack(self):
        if (self.player_location.zombies == 0):
            return False
        # calculate health lost
        health_lost = self.player_location.zombies - self.player_attack
        # cap health lost to 4 points
        if (health_lost > 4):
            health_lost = 4
        # update health
        self.player_health = self.player_health - health_lost
        # update zombies in room
        self.player_location.zombies = 0

        self.check_game_end_condition()
        return True

    def check_game_end_condition(self):
        # check still alive
        if self.player_health <= 0:
            print('Zombies have eaten your brains - Game Over.')
            sys.exit()
        if self.game_time == 12:
            print('You have been over run by the zombie horde - Game Over')
            sys.exit()
        return True

    def update_game_time(self):
        # update card stack and time
        self.card_count += 1
        if (self.card_count >= 4):
            self.game_time += 1
            self.card_count = 1
        self.check_game_end_condition()

    def run(self, direction):
        if (self.player_location.zombies == 0):
            return False
        if (direction not in ('North', 'East', 'South', 'West')):
            return False
        if (self.player_location.direction[direction] != 'blocked'):
            self.player_location = self.all_tiles[
                self.player_location.direction[direction]]
        else:
            return False
        self.player_health -= 1
        self.withdraw_card()
        return True

    def cower(self):
        if (self.player_location.zombies != 0):
            return False
        self.player_health += 3
        self.update_game_time()
        return True

    def get_totem(self):
        if (self.player_location.name != 'Evil Temple'):
            return False
        self.has_zombie_totem = True
        return True

    def bury_totem(self):
        if (self.player_location.name != 'Graveyard'):
            return False
        if (self.player_location.zombies != 0):
            return False
        if (self.has_zombie_totem):
            return True
        return False


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--new', help='Begin a new game',
                        action='store_true')
    parser.add_argument('-l', '--load', help='Load a saved game' +
                                             ' from LOAD')
    args = parser.parse_args()
    if args.new:
        cmd_temp = controller()
        cmd_temp.start_game()
        cmd_temp.cmdloop()
    if args.load is not None:
        cmd_temp = controller()
        cmd_temp.do_load(args.load)
        cmd_temp.cmdloop()
    parser.print_help()


if __name__ == '__main__':
    main()
