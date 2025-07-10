# Concession Stand Program
# This program simulates a concession stand where users can purchase items.

# Dictionary {key: item name, value: item price}

menu = {
    "hot dog": 3.50,
    "nachos": 4.00,
    "soda": 2.00,
    "candy": 1.50,
    "popcorn": 2.50,
    "pretzel": 3.00,
    "chips": 1.75,
}

cart = []  # List to hold items added to the cart
total = 0  # Variable to hold the total cost

print("------------- MENU -------------")
print()
for key, value in menu.items():
    print(f"{key:10}: ${value:.2f}")
print()
print("--------------------------------")

while True:
    food = input("Enter the item you want to purchase (q to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
       cart.append(food)

print("-----------YOUR CART-----------")
for food in cart:
    total += menu.get(food)
    print(food, end=" ")

print()
print(f"Total cost: ${total:.2f}")