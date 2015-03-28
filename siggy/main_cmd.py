__author__ = 'siggyzee'
import cmd
from siggy.game import *

class main_cmd(cmd.Cmd):
    intro = 'Welcome to Zimp 0.1, please type new for a new game'

    def new_game(self):
        print("hi")
        self.game = Game("Foyer", 8)

    def do_move(self, direction):
        print("move", direction)
        self.game.move_player(direction)

    def do_run(self, direction):
        print("run ", direction)

    def do_attack(self, line):
        print("attack")

    def do_cower(self, line):
        print("cower")

    def do_get_item(self, line):
        print("get item")

    def do_get_totem(self, line):
        print("get totem")

    def do_bury_totem(self, line):
        print("bury totem")

    def do_help(self, line):
        print("Zimp - Help")
        print("")
        print("help			    - Display this help file.")
        print("move <Direction>	- Move player <Direction>.")
        print("run <Direction> 	- Escape zombies by running <Direction>.")
        print("attack			    - Attack zombies in current room.")
        print("cower		  	    - Hide in current room and not move this turn.")
        print("get_item		    - Retrieve weapon from current room.")
        print("get_totem		    - Retrieve totem (Only possible in Evil Temple).")
        print("bury_totem		    - Bury totem (Only possible in graveyard).")
        print("save			    - Save current game to <path>.")
        print("quit			    - Quit game.")
        print("")

    def do_quit(self, line):
        return True


if __name__ == "__main__":
    cmd_temp = main_cmd()
    cmd_temp.new_game()
    cmd_temp.cmdloop()