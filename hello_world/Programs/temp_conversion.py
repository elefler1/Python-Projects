# Temperature Conversion Program

unit = input("Enter the unit of temperature (C for Celsius, F for Fahrenheit): ")
temp = float(input("Enter the temperature value: "))

if unit == "C":
    converted = (temp * 9/5) + 32
    print(f"{temp}°C is equal to {round(converted, 1)}°F")
elif unit == "F":
    converted = (temp - 32) * 5/9
    print(f"{temp}°F is equal to {round(converted, 1)}°C")
else:
    print(f"{unit} is an invalid unit. Please enter 'C' or 'F'.")

