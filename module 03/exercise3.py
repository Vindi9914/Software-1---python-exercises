import math
length = input ("Enter the length of the rectangle: ")
width = input ("Enter the width of the rectangle: ")

length = float(length)
width = float(width)

perimeter = 2 * (length + width)

area = length * width

print("The perimeter of the rectangle is: " + str(perimeter))
print("The area of the rectangle is: " + str(area))