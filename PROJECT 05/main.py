from player import Player
from room import village, cave, forest, palace
from item import apple, key, sword, diamond


SAVE_FILE = "savegame.txt"


# ---------------- FILE HANDLING ----------------

def read_file(filename):
    try:
        with open(filename, "r") as file:  
            return file.read()
    except FileNotFoundError:
        return ""


def save_game(player):
    with open(SAVE_FILE, "w") as file:
        file.write(f"name={player.name}\n")
        file.write(f"age={player.age}\n")
        file.write(f"location={player.location}\n")
        file.write(f"apples={player.apples}\n")
        file.write(f"keys={player.keys}\n")
        file.write(f"diamonds={player.diamonds}\n")
        file.write(f"has_sword={player.has_sword}\n")
        file.write(f"is_warrior={player.is_warrior}\n")
        file.write(f"forest_completed={player.forest_completed}\n")


def load_game(player_name):
    try:
        with open(SAVE_FILE, "r") as file:
            data = {}

            for line in file:
                key_name, value = line.strip().split("=", 1)
                data[key_name] = value

        if data.get("name") != player_name:
            return None

        player = Player(data["name"], int(data["age"]))

        player.location = data["location"]
        player.apples = int(data["apples"])
        player.keys = int(data["keys"])
        player.diamonds = int(data["diamonds"])
        player.has_sword = data["has_sword"] == "True"
        player.is_warrior = data["is_warrior"] == "True"
        player.forest_completed = data["forest_completed"] == "True"

        return player

    except (FileNotFoundError, ValueError, KeyError):
        return None


# ---------------- INTRODUCTION ----------------

print(read_file("intro.txt"))

print("\n" + "=" * 40)
print(read_file("instructions.txt"))
print("=" * 40)


# ---------------- PLAYER INFORMATION ----------------

name = input("\nEnter your name: ")

saved_player = load_game(name)

if saved_player is not None:

    print("\nA saved game was found for", name + "!")
    print("Location:", saved_player.location)
    print("Apples:", saved_player.apples)
    print("Keys:", saved_player.keys)
    print("Diamonds:", saved_player.diamonds)

    continue_game = input("\nDo you want to continue this game? (yes/no): ").lower()

    if continue_game == "yes":
        player = saved_player
        print("\nWelcome back,", player.name + "!")
    else:
        age = int(input("Enter your age: "))

        if age <= 12:
            print("Sorry, you cannot get access to play this game.")
            exit()

        player = Player(name, age)

else:

    age = int(input("Enter your age: "))

    if age <= 12:
        print("Sorry, you cannot get access to play this game.")
        exit()

    player = Player(name, age)


print(f"\nWelcome {player.name}!")
print("Your adventure begins in the Village.")


# ---------------- GAME LOOP ----------------

while True:

    # Winning condition
    if player.diamonds == 5:

        print("\nCongratulations!")
        print("You collected 5 diamonds.")
        print("You are the winner!")

        save_game(player)

        print("Your game has been saved.")
        break


    # ---------------- VILLAGE ----------------

    if player.location == "Village":

        print("\nYou are in the Village.")

        print("\n1. Pick apples")
        print("2. Go to Cave")
        print("3. Save and Exit")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":

            # One pick gives 100 apples
            player.apples += 100

            print("\nYou picked 100 apples.")
            print("Total apples:", player.apples)

            # Every 100 apples gives one key
            if player.keys < 5:

                player.keys += 1

                print("You earned a key!")
                print(
                    "There are",
                    player.keys,
                    "keys available in the Cave."
                )

            if player.keys == 5:
                print("All 5 keys are now available in the Cave.")

            save_game(player)

        elif choice == "2":

            player.location = "Cave"
            save_game(player)

        elif choice == "3":

            save_game(player)

            print("\nGame saved successfully.")
            print("Game exited.")
            break

        elif choice == "4":

            print("\nGame exited.")
            break

        else:

            print("\nInvalid choice.")


    # ---------------- CAVE ----------------

    elif player.location == "Cave":

        print("\nYou are in the Cave.")
        print("Keys available in the Cave:", player.keys)

        print("\n1. Take a key")
        print("2. Go back to Village")
        print("3. Save and Exit")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":

            if player.keys > 0:

                # Take one key from the Cave
                player.keys -= 1

                print("\nYou took a key from the Cave.")
                print(
                    "Keys remaining in the Cave:",
                    player.keys
                )

                print("\nWhat do you want to do?")
                print("1. Go to Forest")
                print("2. Go back to Village")

                next_choice = input("Choose an option: ")

                if next_choice == "1":

                    player.location = "Forest"

                elif next_choice == "2":

                    player.location = "Village"

                else:

                    print("\nInvalid choice.")

                save_game(player)

            else:

                print("\nThere are no keys in the Cave.")
                print("Go back to the Village and pick more apples.")

        elif choice == "2":

            player.location = "Village"
            save_game(player)

        elif choice == "3":

            save_game(player)

            print("\nGame saved successfully.")
            print("Game exited.")
            break

        elif choice == "4":

            print("\nGame exited.")
            break

        else:

            print("\nInvalid choice.")


    # ---------------- FOREST ----------------

    elif player.location == "Forest":

        print("\nYou are in the Forest.")
        print("There are bears in the Forest!")

        print("\n1. Try to escape from the bears")
        print("2. Go back to Cave")
        print("3. Save and Exit")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":

            print("\nYou escaped from the bears!")
            print("You successfully passed the Forest.")

            player.forest_completed = True
            player.location = "Palace"

            save_game(player)

        elif choice == "2":

            player.location = "Cave"
            save_game(player)

        elif choice == "3":

            save_game(player)

            print("\nGame saved successfully.")
            print("Game exited.")
            break

        elif choice == "4":

            print("\nGame exited.")
            break

        else:

            print("\nInvalid choice.")


    # ---------------- PALACE ----------------

    elif player.location == "Palace":

        print("\nYou are in the Palace.")

        # Sword has not been collected yet
        if player.has_sword is False:

            print("You have reached the Palace.")
            print("Use your key to open the Palace door.")

            print("\n1. Open the door")
            print("2. Go back")
            print("3. Save and Exit")
            print("4. Exit")

            choice = input("Choose an option: ")

            if choice == "1":

                player.has_sword = True
                player.is_warrior = True

                print("\nYou opened the Palace door!")
                print("You found a sword.")
                print("You are now a Warrior!")

                save_game(player)

            elif choice == "2":

                player.location = "Forest"
                save_game(player)

            elif choice == "3":

                save_game(player)

                print("\nGame saved successfully.")
                print("Game exited.")
                break

            elif choice == "4":

                print("\nGame exited.")
                break

            else:

                print("\nInvalid choice.")

        # Sword already collected
        else:

            print("Now you are a Warrior.")
            print("You have a sword.")
            print("Enemies are inside the Palace.")

            print("\n1. Fight an enemy")
            print("2. Save and Exit")
            print("3. Exit")

            choice = input("Choose an option: ")

            if choice == "1":

                print("\nYou defeated the enemy!")

                # One enemy gives one diamond
                player.diamonds += 1

                print("\nCongratulations! You won a diamond!")
                print("Diamonds collected:", player.diamonds)

                if player.diamonds < 5:

                    print(
                        "You need",
                        5 - player.diamonds,
                        "more diamond(s)."
                    )

                else:

                    print("\nYou collected 5 diamonds!")

                save_game(player)

            elif choice == "2":

                save_game(player)

                print("\nGame saved successfully.")
                print("Game exited.")
                break

            elif choice == "3":

                print("\nGame exited.")
                break

            else:

                print("\nInvalid choice.") 