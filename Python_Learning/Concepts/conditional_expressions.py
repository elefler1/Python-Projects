# Conditional Expression = A one-line shortcut for the if-else statement (ternary operator)
#                          Print or assign one of two values based on a condition
#                          X if condition is else Y

num = 5
a = 6
b = 7
age = 25
temp = 30
user_role = "guest"

print("Positive" if num > 0 else "Negative")
result = "Even" if num % 2 == 0 else "Odd"
max_num = a if a > b else b
min_num = a if a < b else b
status = "Adult" if age >= 18 else "Child"
weather = "HOT" if temp > 20 else "COLD"
access_level = "Full Access" if user_role == "admin" else "Limited Access"


print (access_level)

