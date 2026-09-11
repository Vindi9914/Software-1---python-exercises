name = input("What is your name? ")
age = int(input("How old are you? "))

if age < 12:
    print("You are a minor.")
    exit()

print("Welcome", name + "!")

while True:
    print()
    print("Main menu:")
    print("explore")
    print("treasure")
    print("rest")
    print("lopeta")

    command = input("Choose a command: ")

    if command == "explore":
        print("You explore the forest and discover a hidden path.")

    elif command == "treasure":
        print("You search for treasure and find a gold coin!")

    elif command == "rest":
        print("You rest by the campfire and recover your energy.")

    elif command == "lopeta":
        print("Goodbye!")
        break

    else:
        print("Unknown command.")