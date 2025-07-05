# String Manipulation Methods 

name = input("Enter your full name: ")
phone_number = input("Please enter your phone number: ")

result = len(name)
result = name.find("L")
result = name.rfind("e")
name = name.capitalize()
name = name.upper()
name = name.lower()
name = name.isdigit()
result = name.isalpha()
result = phone_number.count("-")
result = phone_number.replace("-", "")


print(result)

# print(help(str)) # Gieves you a comprehensive list of string manipulation methods

