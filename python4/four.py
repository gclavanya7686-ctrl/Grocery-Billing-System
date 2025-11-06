# Grocery Billing System

grocery = {
    "rice": 60,
    "curd": 50,
    "salt": 88,
    "pickle": 94
}

print("Welcome to Lavanya’s Grocery Store")
print("\nAvailable items (Price per unit):")
print("------------------------------------")
for item, price in grocery.items():
    print(f"{item.capitalize():<10} : ₹{price}")

cart = {}
total = 0

while True:
    choice = input("\nEnter the item name to add to cart (or type 'done' to finish): ").lower()
    if choice == "done":
        break
    elif choice in grocery:
        qty = int(input(f"Enter the quantity of {choice}: "))
        cost = grocery[choice] * qty
        cart[choice] = cost
        total += cost
        print(f"Added {qty} x {choice} = ₹{cost}")
    else:
        print("Invalid item. Please choose from the available list.")

print("\n--------- Final Bill ---------")
for item, cost in cart.items():
    print(f"{item.capitalize():<10} : ₹{cost}")
print("------------------------------")
print(f"Total Amount: ₹{total}")
print("------------------------------")
print("Thank you for shopping with us!")
