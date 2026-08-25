import math

talents = input("Enter talents: ")
pounds = input("Enter pounds: ")
lots = input("Enter lots: ")

talents = float(talents)
pounds = float(pounds)
lots = float(lots)

total_grams = (talents * 20 * 32 + pounds *32 + lots ) * 13.3
kilograms = total_grams / 1000
remaining_grams = total_grams % 1000

print(f"The weight in modern units: ")
print(f"{kilograms:.0f} kilograms and {remaining_grams:.2f} grams")