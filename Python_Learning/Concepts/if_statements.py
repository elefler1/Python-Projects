# if = Run code only IF condition is True
# else = Run code if condition is False

age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote.")
elif age <= 0:
    print("Age cannot be zero or negative. Please enter a valid age.")
else:
    print("You are not eligible to vote.")
# The code checks if the user is eligible to vote based on their age.
# If the age is 18 or older, it prints that the user is eligible to vote
# Be sure to consider the order of your conditions. The condition for age <= 0 should come before the condition for age < 18.


# Asking a user if they would like some food.

response = input("Would you like some food? (Y/N): ")

if response == "Y":
    print("Great! What would you like to eat?")
else:
    print("Okay, maybe another time.")


# # Asking a user what their name is.

name = input("What is your name? ")

if name == "":
    print("You must enter a name.")
else:
    print(f"Hello, {name}!")

# Using booleans with if statements

online = True

if online:
    print("The user is online.")
else:
    print("The user is offline.")
