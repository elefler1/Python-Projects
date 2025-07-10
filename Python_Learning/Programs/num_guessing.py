# Python Number Guessing Game
# This program generates a random number and asks the user to guess it.

import random

lowest_num = 1
highest_num = 100

answer = random.randint(lowest_num, highest_num)
guesses = 0
is_running = True

# print(answer)  # For testing purposes, you can see the answer

print(f"Welcome to the number guessing game!")
print(f"I'm thinking of a number between {lowest_num} and {highest_num}. Can you guess it?")

while is_running:
    guess = input(f"Guess a number between {lowest_num} and {highest_num}: ")
    if guess.isdigit():
        guess = int(guess)
        guesses += 1

        if guess < lowest_num or guess > highest_num:
            print(f"That number is out of range. Please enter a number between {lowest_num} and {highest_num}.")
        elif guess < answer:
            print("Too low! Try again!")
        elif guess > answer:
            print("Too high! Try again!")
        else:
            print("Congratulations! You've guessed the number!")
            print(f"Number of guesses: {guesses}")
            is_running = False
    else:
        print("That is not a number. Please enter a valid number.")
        continue
    