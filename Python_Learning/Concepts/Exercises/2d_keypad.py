# 2D Tuple Keypad Exercsise:

num_pad = ((1, 2, 3), 
           (4, 5, 6), 
           (7, 8, 9), 
           ("*", 0, "#"))

for row in num_pad:
    for num in row:
        print(num, end=' ') # Print each number in the row
    print()  # New line after each row