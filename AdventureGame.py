def showInstructions():
    print("RPG Game - http://usingpython.com/python-rpg-game/")
    print("=========")
    print("Commands:")
    print("'go [direction]'")
    print("'get [item]'")

def showStatus():
    print("------------------------")
    print("You are in the " + rooms[currentRoom]["name"])
    print("Inventory: " + str(inventory))
    if "item" in rooms[currentRoom]:
        print("You see a " + rooms[currentRoom]["item"])

inventory = []

rooms = {
    1 : {"name" : "Entrance Hall",
         "east" : 2,
         "north": 4},
    2 : {"name" : "Servant's Quarters",
         "west" : 1,
         "north": 3,},
    3 : {"name" : "Sultan's Wardrobe",
         "south": 2,
         "west" : 4},
    4 : {"name" : "Sultan's Bedroom",
         "east" : 3,
         "south": 1,
         "west" : 5},
    5 : {"name" : "Hidden Corridor",
         "east" : 4,
         "west" : 6},
    6 : {"name" : "Treasure Room",
         "east" : 5,
         "item" : "treasure chest"}
    }

currentRoom = 1

showInstructions()

while True:

    showStatus()

    move = input(">").lower().split()

    if move[0] == "go" :
        if move[1] in rooms[currentRoom]:
            currentRoom = rooms[currentRoom][move[1]]
        else:
            print("You can't go that way!")

    if move[0] == "get" :
        if "item" in rooms[currentRoom] and move [1] in rooms[currentRoom]["item"]:
            inventory += [rooms[currentRoom]["item"]]
            print(rooms[currentRoom]["item"] + " got!")
            del rooms[currentRoom]["item"]
        else:
            print("There isn't a " + str(move[1:]) + " in here!")
