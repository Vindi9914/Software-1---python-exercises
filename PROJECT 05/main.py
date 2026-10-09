
from player import Player
from room import village, cave, forest, meadow, palace
from item import apple, key, sword, diamond


SAVE_FILE = "savegame.txt"
WINNING_DIAMONDS = 5


# ---------------- FILE HANDLING ----------------

def read_file(filename):
    """Read and return the contents of a text file."""
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        return ""


def save_game(player):
    """Save the player's progress to a text file."""
    with open(SAVE_FILE, "w", encoding="utf-8") as file:
        file.write(f"name={player.name}\n")
        file.write(f"age={player.age}\n")
        file.write(f"location={player.location}\n")
        file.write(f"apples={player.apples}\n")
        file.write(f"keys={player.keys}\n")
        file.write(f"diamonds={player.diamonds}\n")
        file.write(f"has_key={player.has_key}\n")
        file.write(f"has_sword={player.has_sword}\n")
        file.write(f"is_warrior={player.is_warrior}\n")
        file.write(f"forest_completed={player.forest_completed}\n")


def load_game(player_name):
    """Load saved progress if the player's name matches."""
    try:
        with open(SAVE_FILE, "r", encoding="utf-8") as file:
            data = {}

            for line in file:
                if "=" in line:
                    key_name, value = line.strip().split("=", 1)
                    data[key_name] = value

        if data.get("name") != player_name:
            return None

        player = Player(data["name"], int(data["age"]))
        player.location = data.get("location", "Village")
        player.apples = int(data.get("apples", 0))
        player.keys = int(data.get("keys", 0))
        player.diamonds = int(data.get("diamonds", 0))
        player.has_key = data.get("has_key", "False") == "True"
        player.has_sword = data.get("has_sword", "False") == "True"
        player.is_warrior = data.get("is_warrior", "False") == "True"
        player.forest_completed = (
            data.get("forest_completed", "False") == "True"
        )

        return player

    except (FileNotFoundError, ValueError, KeyError):
        return None


# ---------------- INTRODUCTION ----------------

print(read_file("intro.txt"))
print("\n" + "=" * 50)
print(read_file("instructions.txt"))
print("=" * 50)


# ---------------- PLAYER INFORMATION ----------------

name = input("\nEnter your name: ").strip()

saved_player = load_game(name)

if saved_player is not None:
    print("\nA saved game was found for", name + "!")
    print("Location:", saved_player.location)
    print("Apples:", saved_player.apples)
    print("Keys in the Cave:", saved_player.keys)
    print("Diamonds:", saved_player.diamonds)

    continue_game = input(
        "\nDo you want to continue this game? (yes/no): "
    ).strip().lower()

    if continue_game == "yes":
        player = saved_player
        print("\nWelcome back,", player.name + "!")
    else:
        age = int(input("Enter your age: "))

        if age <= 12:
            print("Sorry, this game is for players aged 13 and over.")
            raise SystemExit

        player = Player(name, age)

else:
    age = int(input("Enter your age: "))

    if age <= 12:
        print("Sorry, this game is for players aged 13 and over.")
        raise SystemExit

    player = Player(name, age)


print(f"\nWelcome {player.name}!")
print("Your adventure begins in the Village.")


# ---------------- MAIN GAME LOOP ----------------

while True:

    if player.diamonds >= WINNING_DIAMONDS:
        print("\nCongratulations!")
        print("You collected five diamonds and completed the adventure!")
        save_game(player)
        print("Your game has been saved.")
        break

    # ---------------- VILLAGE ----------------

    if player.location == "Village":
        print("\nYou are in the Village.")
        print("Apples:", player.apples)
        print("Keys available in the Cave:", player.keys)
        print("\n1. Pick apples")
        print("2. Go to the Cave")
        print("3. View player status")
        print("4. Save and Exit")
        print("5. Exit without saving")

        choice = input("Choose an option: ")

        if choice == "1":
            player.apples += 100
            print(f"\nYou collected 100 {apple.name.lower()}s.")
            print("Total apples:", player.apples)

            if player.keys < 5:
                player.keys += 1
                print(
                    f"One {key.name.lower()} is now available in the Cave."
                )
                print("Keys available:", player.keys)
            else:
                print("The Cave already has the maximum of five keys.")

            save_game(player)

        elif choice == "2":
            player.location = "Cave"
            save_game(player)

        elif choice == "3":
            print("\nPLAYER STATUS")
            print("Name:", player.name)
            print("Age:", player.age)
            print("Location:", player.location)
            print("Apples:", player.apples)
            print("Keys in Cave:", player.keys)
            print("Carrying a key:", player.has_key)
            print("Has sword:", player.has_sword)
            print("Diamonds:", player.diamonds)

        elif choice == "4":
            save_game(player)
            print("Game saved. See you next time!")
            break

        elif choice == "5":
            print("Game exited without saving new progress.")
            break

        else:
            print("Invalid choice. Please select a number from the menu.")

    # ---------------- CAVE ----------------

    elif player.location == "Cave":
        print("\nYou are in the Cave.")
        print("Keys available:", player.keys)
        print("Are you carrying a key?", player.has_key)
        print("\n1. Take a key")
        print("2. Choose a route (you must be carrying a key)")
        print("3. Return to Village")
        print("4. Save and Exit")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            if player.has_key:
                print("You are already carrying a key. Choose a route instead.")
            elif player.keys > 0:
                player.keys -= 1
                player.has_key = True
                print("\nYou took a key from the Cave.")
                save_game(player)
            else:
                print("There are no keys in the Cave.")
                print("Return to the Village and collect more apples.")

        elif choice == "2":
            if player.has_key:
                print("\nChoose your route to the Palace:")
                print("1. Forest Path - escape from bears")
                print("2. Meadow Path - escape from snakes")

                route_choice = input("Choose a route (1 or 2): ")

                if route_choice == "1":
                    player.location = "Forest"
                    print("You chose the Forest Path.")
                    save_game(player)

                elif route_choice == "2":
                    player.location = "Meadow"
                    print("You chose the Meadow Path.")
                    save_game(player)

                else:
                    print("Invalid route. Please choose 1 or 2.")

            else:
                print("Take a key before choosing a route.")

        elif choice == "3":
            player.location = "Village"
            save_game(player)

        elif choice == "4":
            save_game(player)
            print("Game saved. See you next time!")
            break

        elif choice == "5":
            print("Game exited.")
            break

        else:
            print("Invalid choice. Please select a number from the menu.")

    # ---------------- FOREST PATH: BEARS ----------------

    elif player.location == "Forest":
        print("\nYou are on the Forest Path.")
        print(forest.description)
        print("\nA bear suddenly appears on the path!")
        print("You must escape from the bear to reach the Palace.")
        print("\n1.. Try to run past the bear")
        print("\n2. Return to the Cave")
        print("\n3. Save and Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            print("\nYou are escaped from the bear!")
            print("You safely reach the Palace.")
            player.forest_completed = True
            player.location = "Palace"
            save_game(player)

      
        elif choice == "2":
            player.location = "Cave"
            save_game(player)

        elif choice == "3":
            save_game(player)
            print("Game saved. See you next time!")
            break

        else:
            print("Invalid choice. Please select a number from the menu.")

    # ---------------- MEADOW PATH: SNAKES ----------------

    elif player.location == "Meadow":
        print("\nYou are on the Meadow Path.")
        print(meadow.description)
        print("\nA snake appears in the grass!")
        print("You must escape from the snake to reach the Palace.")
        print("\n1. Try to step past the snake")
        print("\n2. Return to the Cave")
        print("\n3. Save and Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            print("\nYou carefully escaped from the snake!")
            print("You safely reach the Palace.")
            player.location = "Palace"
            save_game(player)

        elif choice == "2":
            player.location = "Cave"
            save_game(player)

        elif choice == "3":
            save_game(player)
            print("Game saved. See you next time!")
            break

        else:
            print("Invalid choice. Please select a number from the menu.")

    # ---------------- PALACE ----------------

    elif player.location == "Palace":
        print("\nYou are in the Palace.")

        if not player.has_sword:
            print("The Palace door is locked.")
            print("You need your key to open it.")
            print("\n1. Open the door with your key")
            print("2. Return to the Forest Path")
            print("3. Return to the Meadow Path")
            print("4. Save and Exit")

            choice = input("Choose an option: ")

            if choice == "1":
                if player.has_key:
                    player.has_key = False
                    player.has_sword = True
                    player.is_warrior = True
                    print(f"\nYou opened the door and found a {sword.name.lower()}!")
                    print("You are now a Warrior!")
                    print("You can fight enemies to collect diamonds.")
                    save_game(player)
                else:
                    print("You do not have a key. Return to the Cave.")

            elif choice == "2":
                player.location = "Forest"
                save_game(player)

            elif choice == "3":
                player.location = "Meadow"
                save_game(player)

            elif choice == "4":
                save_game(player)
                print("Game saved. See you next time!")
                break

            else:
                print("Invalid choice. Please select a number from the menu.")

        else:
            print("\nYou are a Warrior and you have a sword.")
            print("Diamonds collected:", player.diamonds)
            print("\n1. Fight an enemy")
            print("2. Save and Exit")
            print("3. Exit")

            choice = input("Choose an option: ")

            if choice == "1":
                print("\nYou defeated an enemy!")
                player.diamonds += 1
                print(f"You collected one {diamond.name.lower()}.")
                print("Diamonds collected:", player.diamonds)

                if player.diamonds < WINNING_DIAMONDS:
                    remaining = WINNING_DIAMONDS - player.diamonds
                    print("You need", remaining, "more diamond(s) to win.")
                else:
                    print("You have collected all five diamonds!")

                save_game(player)

            elif choice == "2":
                save_game(player)
                print("Game saved. See you next time!")
                break

            elif choice == "3":
                print("Game exited.")
                break

            else:
                print("Invalid choice. Please select a number from the menu.")

    else:
        print("Unknown location in saved game. Returning to the Village.")
        player.location = "Village"
        save_game(player)
        