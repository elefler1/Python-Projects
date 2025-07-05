# Account Creation Exercsise

# Username Validation:
#   1. Username must not be longer than 12 characters
#   2. Username must not contain spaces
#   3. username must contain digits


while True:
    username = input("Enter new username: ")
    if len(username) > 12:
        print("Username cannot be more than 12 character")
        continue
    elif not username.find(" ") == -1:
        print("Username must not contain spaces")
        continue
    elif not username.isalpha():
        print("Username may not contain numbers")
        continue
    else:
        print(f"New username set to {username}")
        break

# Password Validation:
#   1. Password must contain at least 10 characters
#   2. Password must not contain spaces
#   3. Password must contain digits
#   4. Password must contin at least one uppercae letter
#   5. Password must contain at least one lowercase letter


while True:
    password = input("Enter new password: ")
    if len(password) < 10:
        print("Password must contain at least 10 characters")
        continue
    elif not password.find(" ") == -1:
        print("Password must not contain spaces")
        continue
    elif password.isupper():
        print("Password must contain at least one uppercase letter")
        continue
    elif password.islower():
        print("Password must contain at least one lowercase letter")
        continue
    elif password.isdigit():
        print("Password must contain at least one number")
        continue
    else:
        print("Account creation successful!")
        break
