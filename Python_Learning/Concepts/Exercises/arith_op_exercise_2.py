# Area of a Circle
# This program calculates the area of a circle given its radius.

import math

radius = float(input("Enter the radius of the circle: "))
area = math.pi * radius**2
print(f"The area of the circle is: {round(area, 2)}cm²")