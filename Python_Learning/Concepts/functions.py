# Function = A block of reusable code that performs a specific task
#            Place () after the function to invoke it

# Happy Birthday Function

def happy_birthday(name, age):
    print(f"Happy birthday to {name}!")
    print(f"You are {age} years old!")
    print(f"Happy birthday to {name}!")
    print()

happy_birthday("Bro", 25)
happy_birthday("Alice", 30)
happy_birthday("Charlie", 35)

# Invoice Display Function

def display_invoice(username, amount, due_date):
    print(f"Invoice for: {username}")
    print(f"Amount Due: ${amount}")
    print(f"Due Date: {due_date}")
    print()

display_invoice("Alice", 150, "2023-09-30")

# Return = Statement used to end a function and optionally send back a value

def add(x, y):
    z = x + y
    return z

def subtract(x, y):
    z = x - y
    return z

def multiply(x, y):
    z = x * y
    return z

def divide(x, y):
    z = x / y
    return z

print(add(1,2))
print(subtract(5,3))
print(multiply(4,2))
print(divide(8,2))

# Name Creation Function
def create_name(first_name, last_name):
    first = first_name.capitalize()
    last = last_name.capitalize()
    full_name = f"{first} {last}"
    return full_name

print(create_name("john", "doe"))
