# Francisco Sanchez
# 10/12/23

# This program is going the calculate the day you return from vacation

# The user will enter the starting day number (0 for Sunday, 1 for Monday, ..., 6 for Saturday)
starting_day = int(input("Enter the starting day number (0-6, where 0 is Sunday, 1 is Monday, etc.): "))

# The user will enter the length of their stay in nights
length_of_stay = int(input("Enter the length of your stay in nights: "))

# Calculate the day of the week you will return on
return_day = (starting_day + length_of_stay) % 7

# Define a list of day names
day_names = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

# Print the result
print(f"You will return on a {day_names[return_day]}.")
