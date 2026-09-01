while True:
    inches = float(input("Enter length in inches (negative value to quit): "))
    if inches < 0:
        print("Program ended.")
        break
    centimeters = inches * 2.54
    print(f"{inches} inches is {centimeters:.2f} centimeters")