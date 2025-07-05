# WHile Loop = execute code WHILE some condition remains true


# Example 1:

name = input("Enter your name: ")

while name == "":
    print("You did not enter your name. Please enter your name")
    name = input("Enter your name: ")
print(f"Hello, {name}")


# Example 2:

age = int(input("Enter your age: "))

while age < 0:
    print("Age must be a positive number")
    age = int(input("Enter your age: "))

print(f"You are {age} years old")


# Example 3:

food = input("Enter your favorite food (q to quit): ")

while not food == "q":
    print(f"Yum! We love {food} too.")
    food = input("What's another food you enjoy? (q to quit): ")

print("See you later!")


# Example 4:

num = int(input("Enter a number between 1 - 10: "))

while num < 1 or num > 10:
    print (f"The number you entered is not between 1 - 10.")
    num = int(input("Enter a number between 1 - 10: "))
print(f"The number you chose is {num}")