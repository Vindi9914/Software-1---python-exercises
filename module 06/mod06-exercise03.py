number = int(input("Enter an integer: "))

if number < 2:
    print(number, "is not a prime number.")
else:
    prime = True

    for i in range(2, number):
        if number % i == 0:
            prime = False
            break

    if prime:
        print(number, "is a prime number.")
    else:
        print(number, "is not a prime number.")