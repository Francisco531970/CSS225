# Francisco Sanchez
# 10/10/2023

# In this program greets the people whose names are in the program

# Here is the list of people allowed in
allowed_users = ["Francisco", "Robyn"]

# The user enters their name
user_name = input("Enter your name: ")

# If the correct name is used, it greets them with their name. If the name isn't right, it just greets them.
if user_name.lower() in allowed_users:
    print(f"Hello, {user_name}!")
else:
    print("Hello, Welcome!")
