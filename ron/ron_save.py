__author__ = 'Ron'

import cmd
import sys
import pickle

class Controller(cmd.Cmd):
    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = "Enter your command: \n"
        self.game = Game()

	#From here I extended the code	
		
    def do_save(self, line):
        if len(line) == 0:
            print("\nYou must enter a file name\n")
        else:
            pickle.dump(self.game, open("saves/" + line + ".data", "wb"), pickle.HIGHEST_PROTOCOL)
            print("\nFile saved\n")			

    def do_load(self, line):
        try:
            self.game = pickle.load(open("saves/" + line + ".data", "rb"))
            print("\nFile loaded\n")
        except (IOError, pickle.UnpicklingError):
            print('\nError! no such file or invalid save file\n')
		
    def do_status(self, line):
        self.game.display_game_status()
		
    def do_quit(self, line):
        print("\n----------")
        print("Game ended")
        print("----------")
        return 1
		
    def help_quit(self):
        print("\nQuit the game\n")

    def help_save(self):
        print("\nSerialize the game object into a file with the file name you entered")
        print('Usage: If you entered "save mySave" command it will create or overwrite a mySave.data file inside the saves folder\n')

    def help_load(self):
        print("\nDeserialize and replace the current game object from a saved file\n")
        
    def help_status(self):
        print("\nDisplay the current game status\n")



