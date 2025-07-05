#Exercsie 2 Shopping Cart Program

item = input("Enter the item you want to buy: ")
price = float(input("Enter the price of the item: "))
quantity = int(input("Enter the quantity of the item: "))
total_cost = price * quantity

print(f"The total cost for {quantity} {item}(s) is: ${total_cost:.2f}") # ":.2f" formats the total cost to two decimal places.