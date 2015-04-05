class Tile:
    def __init__(self, name="Foyer"):
        self.name = name
        self.item = ''
        self.zombies = 0
        self.west = ""
        self.next_tile = ""
        self.east = ""
        self.item =""
    def find_next(self):
        pass

    def get_tile(self):
        return self.name

    def print_message(self):
        print("Your are in {}".format(self.name))


def main():
        pass


if __name__ == '__main__':
    Foyer = Tile()
    Dining_room = Tile("Dining rooom",)
    Foyer.print_message()

