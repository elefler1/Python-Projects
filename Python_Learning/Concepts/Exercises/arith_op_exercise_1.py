# Circumference of a Circle
# This program calculates the circumference of a circle given its radius.

import math

radius = float(input("Enter the radius of the circle: "))
circumference = 2 * math.pi * radius
print(f"The circumference of the circle is: {round(circumference, 2)}cm")