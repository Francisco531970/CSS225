# Francisco Sanchez
# 10/10/2023

allowed_users = ["Francisco", "Robyn"]

user_name = input("Enter your name: ")

if user_name.lower() in allowed_users:
    print(f"Hello, {user_name}!")
else:
    print("Hello, Welcome!")