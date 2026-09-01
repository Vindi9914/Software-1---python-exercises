username = "python"
password = "rules"

attempts = 0

while attempts < 5:
    user = input("Enter username: ")
    pwd = input("Enter password: ")

    if user == username and pwd == password:
        print("Welcome")
        break

    attempts = attempts + 1

    if attempts < 5:
        print("Incorrect username or password. Please try again.")

if attempts == 5:
    print("Access denied")      