__author__ = 'siggyzee'
import cmd
import pickle
import getopt
import sys
import argparse

from siggy.game import *


class controller(cmd.Cmd):
    def __init__(self):
        cmd.Cmd.__init__(self)
        self.intro = 'Welcome to Zimp 0.1 \n'
        self.prompt = 'Enter your command: \n'
        self.game = Game()

    def start_game(self):
        self.game.display_game_status()

    def do_move(self, direction):
        print('move', direction)
        result = self.game.move_player(direction)
        if (not result):
            print('You can’t move in that direction or when there are' +
                  ' zombies in the room.')
        else:
            print('You move ' + direction + '.')
            self.game.display_game_status()

    def do_run(self, direction):
        print('run ', direction)
        result = self.game.run(direction)
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
            print('You cower when there is zombies in the room.')
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
            print('You picked up the Zombie totem')
            self.game.display_game_status()

    def do_bury_totem(self, line):
        print('bury totem')
        result = self.game.bury_totem()
        if (not result):
            print('You can only bury the totem in the Graveyard when ' +
                  ' there are no Zombies.')
        else:
            print('Something is BOKE this should never EVER happen WTF' +
                  ' have you done!!!!')

    def do_help(self, line):
        print('Zimp - Help')
        print('')
        print('help			    - Display this help file.')
        print('move <Direction>	- Move player <Direction>. <Direction> ' +
              '= North, East, South, West')
        print('run <Direction> 	- Escape zombies by running <Direction>' +
              '. <Direction> = North, East, South, West')
        print('attack			    - Attack zombies in current room.')
        print('cower		  	    - Hide in current room and not ' +
              'move this turn.')
        print('get_item		    - Retrieve weapon from current room.')
        print('get_totem		    - Retrieve totem (Only possible' +
              ' in Evil Temple).')
        print('bury_totem		    - Bury totem (Only possible in ' +
              'graveyard).')
        print('save <path>		    - Save current game to <path>.')
        print('load <path>		    - Save current game to <path>.')
        print('quit			    - Quit game.')
        print('')

    def do_save(self, save_string):
        if (save_string) == '':
            print('You must enter a file name and/or path ' +
                  'to save too relative to the current directory.')
            print('Eg. ./save/myGameData.dat')
        else:
            try:

                # TODO code for figuring out and creating new directories to go here

                output_file = open(save_string, 'wb')
                pickle.dump(self.game, output_file)
                print('File saved to ' + save_string)
                output_file.close()
            except FileNotFoundError as err:
                print(err)
                print("You entered an invalid file string.")

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


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--new', help='Begin a new game',
                        action='store_true')
    parser.add_argument('-l', '--load', help='Load a saved game' +
                                             ' from <path>')
    args = parser.parse_args()
    if args.new:
        cmd_temp = controller()
        cmd_temp.start_game()
        cmd_temp.cmdloop()
    if args.load != "":
        cmd_temp = controller()
        cmd_temp.do_load(args.load)
        cmd_temp.cmdloop()


if __name__ == '__main__':
    main()
