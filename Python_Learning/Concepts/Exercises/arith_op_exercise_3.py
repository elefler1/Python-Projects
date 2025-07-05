# Hypotenuse of a right triangle
# The hypotenuse is calculated using the Pythagorean theorem
# hypotenuse = sqrt(base^2 + height^2)

import math

a = float(input("Enter side A of the triangle: "))
b = float(input("Enter side B of the triangle: "))
c = math.sqrt(pow(a, 2) + pow(b, 2))
# Alternatively, you can calculate it using the following line for shorter code:
# c = math.hypot(a, b)

print(f"The hypotenuse of the triangle is: {round(c, 2)}cm")
