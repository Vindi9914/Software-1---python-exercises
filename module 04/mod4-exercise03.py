gender = input("Enter biological gender (male/female): ").lower()

if gender == "female":
    hemoglobin = float(input("Enter hemoglobin value (g/l): "))
    if hemoglobin < 117:
        print("Your hemoglobin is low.")
    elif hemoglobin <= 155:
        print("Your hemoglobin is normal.")
    else:
        print("Your hemoglobin is high.")

elif gender == "male":
    hemoglobin = float(input("Enter hemoglobin value (g/l): "))
    if hemoglobin < 134:
        print("Your hemoglobin is low.")
    elif hemoglobin <= 167:
        print("Your hemoglobin is normal.")    
    else:
        print("Your hemoglobin is high.")
else:
    hemoglobin = float(input("Enter hemoglobin value (g/l): "))
    print("Invalid gender.")           