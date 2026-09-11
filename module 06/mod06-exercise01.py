import random
dice = int(input("How many dice to roll: "))
total = 0

for i in range(dice):
    roll = random.randint(1, 6)
    total += roll

print("Sum of the dice:", total)    