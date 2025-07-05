# Logical Operators = evaluate multiple conditions (or, and, not)
#                     or = at least one condition is true
#                     and = all conditions are true
#                     not = negates a condition (reverses its truth value)

# Logical Operator OR:

# temp = 36
# is_raining = False

# if temp > 35 or temp < 0 or is_raining:
#     print("The outdoor event is cancelled.")
# else:
#     print("The outdoor event is still scheduled.")


# Logical Operator AND:

temp = 20
is_sunny = False

if temp >= 28 and is_sunny:
    print("It's HOT outside 🥵")
    print("It is SUNNY.🌞")
elif temp <= 0 and is_sunny:
    print("It's COLD outside!🥶")
    print("It is SUNNY.🌞")
elif 28 > temp > 0 and is_sunny:
    print("It's WARM outside!😊")
    print("It is SUNNY.🌞")


# Logical Operator NOT:


elif temp >= 28 and not is_sunny:
    print("It's HOT outside 🥵")
    print("It's CLOUDY.🌥️")   
elif temp <= 0 and not is_sunny:
    print("It's COLD outside!🥶")
    print("It's CLOUDY.🌥️")
elif 28 > temp > 0 and not is_sunny:
    print("It's WARM outside!😊")
    print("It's CLOUDY.🌥️")
