numbers = []

while True:
    number = input("Enter a number (or press Enter to quit): ")

    if number == "":
        break

    numbers.append(float(number))

print(f"Smallest number: {min(numbers)}")
print(f"Largest number: {max(numbers)}")  