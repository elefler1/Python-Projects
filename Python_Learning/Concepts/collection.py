# Collections = Single "variable" to store multiple values
# 1. List = [] Ordered, Mutable, Allows Duplicates
# 2. Tuple = () Ordered, Immutable, Allows Duplicates
# 3. Set = {} Unordered, Mutable, No Duplicates
# 4. Dictionary = A collection of {key:value} pairs ordered and changeable. No Duplicates in keys

# Lists:
# Lists are used to store multiple items in a single variable.

fruits = ["apple", "orange", "banana", "kiwi"]

print(dir(fruits)) # List of all methods and attributes
print(help(fruits)) 
print (len(fruits)) # Length of the list
print("apple" in fruits)  # Check if "apple" is in the list
print (fruits[0])  # Accessing the first element
for fruit in fruits: 
    print(fruit) # Iterating through the list
fruits[0] = "pineapple"  # Changing the first element
print(fruits)

fruits.append("pineapple")  # Adding an element to the end of the list
fruits.insert(0, "grape")  # Adding an element at the beginning of the list
fruits.remove("banana")  # Removing an element from the list
fruits.sort()  # Sorting the list
fruits.reverse() # Reversing the list
fruits.clear()  # Clearing the list
print(fruits.index("kiwi")) # Finding the index of an element
print(fruits.count("apple"))  # Counting occurrences of an element

print(fruits)

# Tuples:
# Tuples are similar to lists, but they are immutable (cannot be changed after creation).

fruits_tuple = ("apple", "orange", "banana", "kiwi")

print(dir(fruits_tuple))  # List of all methods and attributes
print(help(fruits_tuple))  # Help documentation for tuples
print(len(fruits_tuple))  # Length of the tuple
print("apple" in fruits_tuple)  # Check if "apple" is in the tuple
print(fruits_tuple[0])  # Accessing the first element
for fruit in fruits_tuple:  # Iterating through the tuple
    print(fruit)
print(fruits_tuple.index("kiwi"))  # Finding the index of an element
print(fruits_tuple.count("apple"))  # Counting occurrences of an element

print(fruits_tuple)

# Sets:
# Sets are used to store multiple items in a single variable, but they do not allow duplicates

fruits_set = {"apple", "orange", "banana", "kiwi"}

print(dir(fruits_set))  # List of all methods and attributes
print(help(fruits_set))  # Help documentation for sets
print(len(fruits_set))  # Length of the set
print("apple" in fruits_set)  # Check if "apple" is in the set
fruits_set.add("pineapple")  # Adding an element to the set
fruits_set.remove("banana")  # Removing an element from the set
fruits_set.pop()  # Removing a random element from the set
fruits_set.clear()  # Clearing the set

print(fruits_set)

# Dictionaries:
# Dictionaries are used to store data values in key:value pairs.

capitals = {
    "USA": "Washington, D.C.",
    "France": "Paris",
    "Germany": "Berlin",
    "Italy": "Rome",
    "Spain": "Madrid"
}

print(dir(capitals))  # List of all methods and attributes
print(help(capitals))  # Help documentation for dictionaries
print(capitals.get("USA"))  # Accessing the value for a key

if capitals.get("Russia"):
    print("That country exists in the dictionary")
else:
    print("That country does not exist in the dictionary") # Checks to see if a key exists in the dictionary

capitals.update({"Canada": "Ottawa"})  # Adding a new key-value pair
capitals["Mexico"] = "Mexico City"  # Adding a new key-value pair
capitals.pop("Spain")  # Removing a key-value pair
capitals.popitem()  # Removing the last inserted key-value pair
capitals.clear()  # Clearing the dictionary

print(capitals.keys())  # Getting all keys
keys = capitals.keys()
for key in keys:
    print(key)  # Printing all keys in the dictionary

print(capitals.values())  # Getting all values
values = capitals.values()
for value in values:
    print(value)  # Printing all values in the dictionary

print(capitals.items())  # Getting all key-value pairs
items = capitals.items()
for key, value in capitals.items():
    print(f"{key}: {value}")  # Printing all key-value pairs in the dictionary


# 2Dlists: # A list of lists
# A 2D list is a list that contains other lists as its elements.

fruits = ["apple", "orange", "banana", "kiwi"] # A list of fruits
vegetables = ["carrot", "broccoli", "spinach"] # A list of vegetables
meats = ["chicken", "beef", "pork"] # A list of meats

groceries = [fruits, vegetables, meats] # A 2D list of grocery items

print(groceries[0])  # Accessing the first list (fruits)
print(groceries[1])  # Accessing the second list (vegetables)
print(groceries[2])  # Accessing the third list (meats)
print(groceries[0][0])  # Accessing the first element of the first list (apple)
print(groceries[0][1])  # Accessing the second element of the first list (orange)
print(groceries[1][0])  # Accessing the first element of the second list (carrot)

# Alternate way of creating a 2D list

groceries = [
    ["apple", "orange", "banana", "kiwi"],  # Fruits
    ["carrot", "broccoli", "spinach"],  # Vegetables
    ["chicken", "beef", "pork"]  # Meats
]

for collection in groceries:
    for food in collection:
        print(food, end=" ")
    print()  # Print a newline after printing all food items