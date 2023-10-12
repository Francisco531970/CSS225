# Francisco Sanchez
# 10/12/23

# This program converts Fahrenheit to Celsius

# Enter the temperature in Fahrenheit
fahrenheit = float(input("Enter the temperature in degrees Fahrenheit: "))

# Convert Fahrenheit to Celsius
celsius = (fahrenheit - 32) * 5/9

# Print the result
print(f"{fahrenheit} degrees Fahrenheit is equal to {celsius: .2f} degrees Celsius")
