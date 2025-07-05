# For loops = Execute a block of code a fixed number of time.
#             You can interate over a range, string, sequence, etc.


# Example 1 (Counter):

for x in reversed(range(1, 11)):
    print(x)
print("HAPPY NEW YEAR!")


# Example 2 (Over a String):

credit_card = "1234-5678-9012"

for x in credit_card:
    print(x)


# Example 3 (Continue/Break):

for x in range(1, 21):
    if x == 13:
        continue
    else:
        print(x)

for x in range(1, 21):
    if x == 13:
        break
    else:
        print(x)