from player import Player
from room import village, cave, forest, palace
from item import apple, key, sword, diamond


# Get player information
name = input("Enter your name: ")
age = int(input("Enter your age: "))

# Age restriction
if age <= 12:
    print("Sorry, you cannot get access to play this game.")
    exit()

# Create player
player = Player(name, age)

print(f"\nWelcome {player.name}!")
print("Your adventure begins in the Village.")


while True:

    # Winning condition
    if player.diamonds >= 5:
        print("\nCongratulations!")
        print("You collected 5 diamonds.")
        print("You are the winner!")
        break


    # ---------------- VILLAGE ----------------

    if player.location == "Village":

        print("\n--------------------")
        print("You are in the Village.")
        

        print("\n1. Pick apples")
        print("2. Go to Cave")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":

            # One pick gives 100 apples
            player.apples += 100

            print("\nYou picked 100 apples.")
            print("Total apples:", player.apples)

            # Every 100 apples gives one key to the Cave
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

        elif choice == "2":

            player.location = "Cave"

        elif choice == "3":

            print("\nGame exited.")
            break

        else:

            print("\nInvalid choice.")


    # ---------------- CAVE ----------------

    elif player.location == "Cave":

        print("\n--------------------")
        print("You are in the Cave.")
        print("--------------------")

        print("Keys available in the Cave:", player.keys)

        print("\n1. Take a key")
        print("2. Go back to Village")
        print("3. Exit")

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

            else:

                print("\nThere are no keys in the Cave.")
                print("Go back to the Village and pick more apples.")

        elif choice == "2":

            player.location = "Village"

        elif choice == "3":

            print("\nGame exited.")
            break

        else:

            print("\nInvalid choice.")


    # ---------------- FOREST ----------------

    elif player.location == "Forest":

        print("\n--------------------")
        print("You are in the Forest.")
        print("--------------------")

        print("There are bears in the Forest!")

        print("\n1. Try to escape from the bears")
        print("2. Go back to Cave")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":

            print("\nYou escaped from the bears!")
            print("You successfully passed the Forest.")

            player.forest_completed = True
            player.location = "Palace"

        elif choice == "2":

            player.location = "Cave"

        elif choice == "3":

            print("\nGame exited.")
            break

        else:

            print("\nInvalid choice.")


    # ---------------- PALACE ----------------

    elif player.location == "Palace":

        print("\n--------------------")
        print("You are in the Palace.")
        print("--------------------")

        # Sword has not been collected yet
        if player.has_sword is False:

            print("You have reached the Palace.")
            print("Use your key to open the Palace door.")

            print("\n1. Open the door")
            print("2. Go back")
            print("3. Exit")

            choice = input("Choose an option: ")

            if choice == "1":

                player.has_sword = True
                player.is_warrior = True

                print("\nYou opened the Palace door!")
                print("You found a sword.")
                print("You are now a Warrior!")

            elif choice == "2":

                player.location = "Forest"

            elif choice == "3":

                print("\nGame exited.")
                break

            else:

                print("\nInvalid choice.")

        # Sword already collected
        else:

            print("Now You are a Warrior.")
            print("You have a sword.")
            print("Enemies are inside the Palace.")

            print("\n1. Fight an enemy")
            print("2. Exit")

            choice = input("Choose an option: ")

            if choice == "1":

                
                print("You defeated the enemy!")

                # One enemy gives one diamond
                player.diamonds += 1

                print("\ncongradulations! You win a diamond!")
                print("Diamonds collected:", player.diamonds)

                if player.diamonds < 5:

                    print(
                        "You need",
                        5 - player.diamonds,
                        "more diamond(s)."
                    )

                else:

                    print("\nYou collected 5 diamonds!")

            elif choice == "2":

                print("\nGame exited.")
                break

            else:

                print("\nInvalid choice.")