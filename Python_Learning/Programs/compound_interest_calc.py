# Python Compound Interest Calculator


# Example 1 (Traditional):

principle = 0
rate = 0
time = 0

while principle <= 0:
    principle = float(input("Enter the principle amount: "))
    if principle <= 0:
        print("Principle cannot be less than or equal to zero")

while rate <= 0:
    rate = float(input("Enter the interest rate amount: "))
    if rate <= 0:
        print("Interest rate cannot be less than or equal to zero")

while time <= 0:
    time = int(input("Enter the time in years: "))
    if time <= 0:
        print("Time cannot be less than or equal to zero")

total = principle * pow(1 + rate /100, time)
print(f"Balance after {time} year/s: ${total:.2f}")


# Examplke 2 (While True):

principle = 0
rate = 0
time = 0

while True:
    principle = float(input("Enter the principle amount: "))
    if principle < 0:
        print("Principle cannot be less than zero")
    else:
        break

while True:
    rate = float(input("Enter the interest rate amount: "))
    if rate < 0:
        print("Interest rate cannot be less than zero")
    else:
        break

while True:
    time = int(input("Enter the time in years: "))
    if time < 0:
        print("Time cannot be less than zero")
    else:
        break

total = principle * pow(1 + rate /100, time)
print(f"Balance after {time} year/s: ${total:.2f}")
