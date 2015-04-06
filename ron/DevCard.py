import random

class DevCard():
    def __init__(self):
        self.items = ["Board with nails", "Machete", "Grisly Femur", "Golf Club", "Chainsaw"]
        self.numbers_of_zombies = [6, 4, 4, 4, 6, 5, 4, 3, 5, 4, 4]
        self.messages = ["You try hard not to wet yourself",
                         "You sense your impending DOOM",
                         "Something icky in your mouth",
                         "A bat poops in your eye",
                         "Your soul isn't wanted here",
                         "The smell of blood is in the air.",
                         "You hear terrible screams",
                         "Your body shivers involuntarily",
                         "You feel a sparkle of Hope"]

    def pick_card(self):
        random_value = random.randint(0, 2)
        if random_value == 0:
            random_item = random.choice(self.items)
            return random_value, random_item
        elif random_value == 1:
            random_zombies = random.choice(self.numbers_of_zombies)
            return random_value, random_zombies
        else:
            random_message = random.choice(self.messages)
            return random_value, random_message
