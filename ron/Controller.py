import cmd
import sys
import pickle
from Game import *

class Controller(cmd.Cmd):
    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = "Enter your command: \n"
        self.game = Game()

    def start_game(self):
        self.game.display_game_status()

    def do_attack(self, line):
        if self.game.attack():
            print ("\nYou killed the zombies")
            self.game.display_game_status()
        else:
            print ("\nNo zombie to attack\n")

    def do_run(self, direction):
        if self.game.run(direction):
            print ("\nYou ran away from the zombies. You lost 1 HP!")
            self.game.display_game_status()


    def do_cower(self, line):
        if self.game.cower():
            print ("\nYou rested for a while")
            self.game.display_game_status()
        else:
            print ("\nYou must kill the zombies first\n")

    def do_move(self, direction):
        if self.game.move(direction):
            print ("\nYou are moving to " + direction)
            self.game.display_game_status()	

    def do_get_totem(self, line):
        if self.game.get_totem():
            print ("\nYou found the totem!")
            self.game.display_game_status()
        else:
            print ("\nNo totem in this zoom.\n")

    def do_bury_totem(self, line):
        if self.game.bury_totem():
            print ("\nTotem buried. You win the game!\n")
            sys.exit()
        else:
            print ("\nYou can't do that!\n")

    def do_get_item(self, line):
        if self.game.get_item():
            self.game.display_game_status()
        else:
            print ("\nNo item to get.\n")

    def do_save(self, line):
        if len(line) == 0:
            print("You must type a file name")
        else:
            file = open("saves/" + line + ".data", "wb")
            pickle.dump(self.game, file)
            file.close()
            print("File saved\n")

    def do_load(self, line):
        try:
            file = open("saves/" + line + ".data", "rb")
            self.game = pickle.load(file)
            file.close()
            print("File loaded\n")
            self.game.display_game_status()
        except (IOError, pickle.UnpicklingError):
            print('Error! no such file or invalid save file')

    def do_quit(self, line):
        print("\n----------")
        print("Game ended")
        print("----------")
        return 1

    def do_help(self, line):
        print ("move <Direction>	- Move player <Direction> \
                run <Direction> 	- Escape zombies by running <Direction> \
                attack			    - Attack zombies in current room \
                cower			    - Hide in current room and not move this turn \
                get_item		    - Retrieve weapon from current room \
                get_totem		    - Retrieve totem (Only in Evil Temple) \
                bury_totem		    - Bury totem (Only in graveyard) \
                save			    - Save current game to <path> \
                load                - Load the saved game <path> \
                quit			    - Quit game \
                help			    - Display this help file")