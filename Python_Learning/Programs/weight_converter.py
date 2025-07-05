# Python Weight Converter Program

def kg_to_lbs(kg):
    return kg * 2.20462

def lbs_to_kg(lbs):
    return lbs / 2.20462

print("Welcome to the Weight Converter!")
print("1. Convert kg to lbs")
print("2. Convert lbs to kg")

choice = input("Enter your choice (1/2): ")

if choice == "1":
    kg = float(input("Enter weight in kg: "))
    print(f"{kg} kg is equal to {round(kg_to_lbs(kg), 1)} lbs")
elif choice == "2":
    lbs = float(input("Enter weight in lbs: "))
    print(f"{lbs} lbs is equal to {round(lbs_to_kg(lbs), 1)} kg")
else:
    print("Invalid choice")


# Alternative implementation using a single conversion function

weight = float(input("Enter weight (e.g., 70kg or 154lbs): "))
unit = input("Is this in kg or lbs? ")

if unit == "kg":
    weight = weight * 2.20462
    unit = "lbs"
elif unit == "lbs":
    weight = weight / 2.20462195
    unit = "kg"
else:
    print(f"{unit} is an invalid unit. Please enter 'kg' or 'lbs'.")

print(f"The weight in {unit} is: {round(weight, 1)} {unit}")

