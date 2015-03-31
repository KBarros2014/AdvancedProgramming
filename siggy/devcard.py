__author__ = 'siggyzee'

from random import randint


class Devcard:
    item = ['Board with Nails', 'Machete', 'Grisly Femur',
            'Golf Club', 'Chainsaw']
    number_of_zombies = [6, 4, 4, 4, 6, 5, 4, 3, 5, 4, 4]
    message = ['You try hard not to wet yourself',
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
            return_number = randint(0, len(self.item) - 1)
            return(0, self.item[return_number])
        # return a number of zombies
        if (return_type == 1):
            return_number = randint(0, len(self.number_of_zombies) - 1)
            return(1, self.number_of_zombies[return_number])
        # return a message
        if (return_type == 2):
            return_number = randint(0, len(self.message) - 1)
            return(2, self.message[return_number])



#class main():
#
#   temp_DevCard = Devcard()
#
#    # Test
#    print(temp_DevCard.pick_card())
#    print(temp_DevCard.pick_card())
#    print(temp_DevCard.pick_card())
#    print(temp_DevCard.pick_card())
#    print(temp_DevCard.pick_card())

#if __name__ == "__main__":
#    main
