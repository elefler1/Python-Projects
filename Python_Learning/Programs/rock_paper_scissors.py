# Rock, Paper, Scissors Game
# This program allows the user to play Rock, Paper, Scissors against the computer.

import random

choices = ("rock", "paper", "scissors")  # Tuple containing the choices for the game, including 'q' to quit
running = True  # Flag to control the game loop

print()
print("Welcome to Rock, Paper, Scissors!")

while running:

    player = None  # Initialize player variable to None
    computer = random.choice(choices)  # Randomly selects one of the options from the tuple
    print()
    player = input("Please choose rock, paper, or scissors (q to quit): ").lower()

    if player == "q":  # If the player chooses 'q', exit the game
        print("Thanks for playing!")
        print()
        running = False
    elif player not in choices:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        continue  # If the player's choice is invalid, prompt them again
    elif player == computer:
        print(f"Computer chose: {computer}")  # Displays the computer's choice
        print("It's a tie!")
    elif (player == "rock" and computer == "scissors") or (player == "paper" and computer == "rock") or (player == "scissors" and computer == "paper"):
        print(f"Computer chose: {computer}")
        print("You win!")
    else:
        print(f"Computer chose: {computer}")
        print("You lose!")
        

        