__author__ = 'siggyzee'
#from enum import Enum
#
#
#class Direction(Enum):
#    north = 1
#    east = 2
#    south = 3
#    west = 4

#Please edit this if you see it's lacking, or you see a potential improvement - Siggy

class Room:
    def __init__(self, name = "", north = 0, east = 0, south = 0, west = 0):
        self.name = name
        self.north = north
        self.east = east
        self.south = south
        self.west = west
        self.zombies = 0
        self.item = ""


#   Using set and get fucntions is not standard form when programming in python because
#   object varibles are public, see http://stackoverflow.com/questions/2579840/do-you-use-the-get-set-pattern-in-python
#    def returnName(self):
#        return(self.name)


class RoomController:
    def __init__(self):
        self.roomsDict = {}
        foyer = Room("Foyer", 1, 0, 0, 0)
        diningRoom = Room("Dining Room", 1, 1, 1, 0)
        evilTemple = Room("Evil Temple", 0, 0, 0, 1)
        patio = Room("Patio", 1, 0, 1, 0)
        yard = Room("Yard", 0, 0, 1, 1)
        graveYard = Room("Graveyard", 0, 1, 0, 0)
        self.roomsDict[foyer.name] = foyer
        self.roomsDict[diningRoom.name] = diningRoom
        self.roomsDict[evilTemple.name] = evilTemple
        self.roomsDict[patio.name] = patio
        self.roomsDict[yard.name] = yard
        self.roomsDict[graveYard.name] = graveYard

#Example
class main:
    print ("Hi")
    rooms = RoomController()
    print(rooms.roomsDict["Foyer"].name)
    rooms.roomsDict["Evil Temple"].zombies = 42
    print("OMG the Evil Temple has", rooms.roomsDict["Evil Temple"].zombies, "Zombies")

if __name__ == "__main__":
    main
