name = input("What is your name? ")
age = int(input("How old are you? "))

if age < 12:
    print("You are a minor.")
    exit()

print("Welcome", name + "!")

inventory = []


def explore():
    print("You explore the forest and discover a hidden path.")


def add_item():
    item = input("What item do you want to add to your inventory? ")
    inventory.append(item)
    print(item, "has been added to your inventory.")


def show_inventory():
    print("Your inventory:")
    for item in inventory:
        print(item)


while True:
    print()
    print("Main menu:")
    print("explore")
    print("add")
    print("inventory")
    print("lopeta")

    command = input("Choose a command: ")

    if command == "explore":
        explore()

    elif command == "add":
        add_item()

    elif command == "inventory":
        show_inventory()

    elif command == "lopeta":
        print("Goodbye!")
        break

    else:
        print("Unknown command.")