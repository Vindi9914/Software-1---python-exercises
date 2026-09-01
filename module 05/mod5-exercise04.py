import random

number = random.randint(1, 10)

guess = int(input("Guess the number: "))

while guess != number:
    if guess > number:
        print("Too high")
    else:
        print("Too low")

    guess = int(input("Guess again: "))

print("Correct")
