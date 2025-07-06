# Python Countdown Timer Program

# import time

# my_time = int(input("Enter the tiem in seconds: "))


# for x in range( my_time, 0, -1):
#     hours = int(x / 3600)
#     minutes = int(x / 60) % 60
#     seconds = x % 60
#     print(f"{hours:02}:{minutes:02}:{seconds:02}")
#     time.sleep(1)

# print("TIME'S UP!")

# Advanced Countdown Timer Program

# Here’s a Python program that allows the user to input hours, minutes, and seconds, and then counts down to zero:

import time

def countdown_timer(hours, minutes, seconds):
    total_seconds = hours * 3600 + minutes * 60 + seconds

    while total_seconds > 0:
        # Calculate hours, minutes, and seconds remaining
        hrs, remainder = divmod(total_seconds, 3600)
        mins, secs = divmod(remainder, 60)
        
        # Display the countdown timer
        print(f"{hrs:02}:{mins:02}:{secs:02}", end="\r")
        time.sleep(1)
        
        # Decrement the total seconds
        total_seconds -= 1

    print("Time's up!")

# Get user input
try:
    hours = int(input("Enter hours: "))
    minutes = int(input("Enter minutes: "))
    seconds = int(input("Enter seconds: "))
    
    if hours < 0 or minutes < 0 or seconds < 0:
        print("Please enter non-negative values.")
    else:
        countdown_timer(hours, minutes, seconds)
except ValueError:
    print("Invalid input! Please enter integers only.")

# How it works:
# The user inputs hours, minutes, and seconds.
# The program converts the input into total seconds.
# It uses a loop to decrement the total seconds while displaying the remaining time in HH:MM:SS format.
# The time.sleep(1) function ensures the countdown updates every second.
# When the countdown reaches zero, it prints "Time's up!".

# This program is simple, user-friendly, and handles basic input validation.