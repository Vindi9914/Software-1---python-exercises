airports = {}

while True:
    print()
    print("Airport Data Management")
    print("1. Enter a new airport")
    print("2. Fetch airport information")
    print("3. Quit")

    option = input("Please choose an option (1-3): ")

    if option == "1":
        icao = input("Enter the ICAO code: ")
        name = input("Enter the airport name: ")

        airports[icao] = name

        print(f"Airport {name} with ICAO code {icao} has been added.")

    elif option == "2":
        icao = input("Enter the ICAO code: ")

        if icao in airports:
            print(f"The airport with ICAO code {icao} is {airports[icao]}.")
        else:
            print(f"No airport found with ICAO code {icao}.")

    elif option == "3":
        print("Thank you for using the Airport Data Management system. Goodbye!")
        break