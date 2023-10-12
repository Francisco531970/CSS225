# Francisco Sanchez
# 10/12/23

# This code is to find the area of a circle by entering a radius

import math

# Prompt the user to enter the radius
radius = float(input("Enter the radius of the circle: "))

# Calculate the area of the circle
area = math.pi * (radius ** 2)

# Print the result
print(f"The area of a circle with radius {radius} is {area: .2f}")
