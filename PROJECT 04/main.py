from item import Item
from room import Room
from player import Player

name = input("What is your name? ")
age = int(input("How old are you? ")
          )
if age < 12:
    print("you are a minor. ")
    exit()

# Create Items
sword = Item("Sword", 2.5)
apple = Item("Apple", 0.2)
key = Item("key", 0.1)

# Create rooms
forest = Room("Forest", sword)
cave = Room("Cave", key)
village = Room("Village", apple)

# Create player
player = Player(name, forest)

print("Welcome", player.name + "!")

while True:
    print()
    print("Main menu:")
    print("explore")
    print("move")
    print("collect")
    print("inventory")
    print("lopeta")

    command = input("Choose a command: ")

    if command == "explore":
        print("You are in", player.location.name)

        if player.location.item is not None: 
            print("You see:", player.location.item.name)
        else:
            print("There is nothing to collect here.")

    elif command == "move":  
        print("Available rooms:")
        print("forest")
        print("cave")
        print("village")

        destination = input("Where do you want to go? ")

        if destination == "forest":
            player.move(forest)

        elif destination == "cave":
            player.move(cave)

        elif destination == "village":
            player.move(village)

        else:
            print("Unknown destination.")

    elif command == "collect":
        player.collect_item()

    elif command == "inventory":
        print("Your inventory:")

        if len(player.items) == 0:
            print("Your inventory is empty.")
        else:
            for item in player.items:
                print(item.name, "-", item.weight, "kg")

    elif command == "lopeta":
        print("Goodbye!")
        break

    else:
        print("Unknown command.")

