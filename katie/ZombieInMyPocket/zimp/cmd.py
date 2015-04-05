import pickle

__author__ = 'katie'
import cmd
import sys
from zimp.game import Game

class CMD(cmd.Cmd):
    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = "Enter command: \n"
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
        Type run <direction>
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
            print ("\nThe Zombie Totem will be in the Evil Temple, "
                   "not here!\n")

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
            print("\nYou couldn't find anything useful\n")

    def do_save(self, line):
        """
        Save the current game state to Save folder with given name.
        Uses savedata as default file name if no name given.
        """
        if len(line) == 0:
            line = "Save/savedata"
        output = open(line, "wb")
        pickle.dump(self.game, output)
        print("Game saved : " + line + "\n")
        output.close()

    def do_load(self, line):
        """
        Load the existing saved game state from Save folder
        """
        try:
            if len(line) == 0:
                line = "Save/savedata"
            loaded_game = open(line, "rb")
            self.game = pickle.load(loaded_game)
            print("\nGame loaded : " + line)
            self.game.display_game_status()
        except (IOError, pickle.UnpicklingError):
            print('\nInvalid file name or file missing\n')

    def do_quit(self, line):
        print ("Quitting")
        sys.exit()

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

