__author__ = 'siggyzee'

from random import randint


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
        return_type = randint(0, 2)
        # return  an item
        if (return_type == 0):
            return_number = randint(0, len(self.items) - 1)
            return(0, self.items[return_number])
        # return a number of zombies
        if (return_type == 1):
            return_number = randint(0, len(self.numbers_of_zombies) - 1)
            return(1, self.numbers_of_zombies[return_number])
        # return a message
        if (return_type == 2):
            return_number = randint(0, len(self.messages) - 1)
            return(2, self.messages[return_number])
