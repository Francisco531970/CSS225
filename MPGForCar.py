# Francisco Sanchez
# 10/12/23

# This program computes the MPG rate for a car

# Prompt the user to enter the number of miles driven and gallons used
miles_driven = float(input("Enter the number of miles driven: "))
gallons_used = float(input("Enter the number of gallons used: "))

# Calculate MPG
mpg = miles_driven / gallons_used

# Print the result
print(f"Your car's MPG is {mpg: .2f} miles per gallon.")
