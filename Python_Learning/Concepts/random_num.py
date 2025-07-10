import random

# print(help(random))


number = random.randint(1, 6)  # Generates a random integer between 1 and 6 (inclusive)
number = random.randint(1, 100)  # Generates a random integer between 1 and 100 (inclusive)
number = random.random() # Generates a random float between 0.0 and 1.0 (exclusive of 1.0)

print(number)


# Rock, Paper, Scissors Game
option = ("Rock", "Paper", "Scissors") # Tuple of options for the game
option = random.choice(option)  # Randomly selects one of the options from the tuple

print(option)

cards = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]  # List of cards
card = random.choice(cards)  # Randomly selects one card from the list

print(f"Your card is: {card}")  # Prints the randomly selected card

