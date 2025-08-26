
items = ["Milk", "Bread", "Eggs", "Cheese", "Butter"]
price_list = {}
print("Enter the prices for the following items:")
for item in items:
    while True:
        price = input(f"Price of {item}: ")
        if price.replace('.', '', 1).isdigit():
            price_list[item] = float(price)  # Convert to float
            break
        else:
            print("Invalid input. Please enter a numeric value.")

print("\n\t--- Super Market Price List ---")
for item, price in price_list.items():
    print(f"\t{item}: ${price:.2f}")

print("\nAvailable items to update:", ', '.join(price_list.keys()))
item_to_update = input("Enter the name of the item to update price: ").strip()

# Input validation
if item_to_update in price_list.keys():
    while True:
        new_price = input(f"Enter the new price for {item_to_update}: ")
        if new_price.replace('.', '', 1).isdigit():
            price_list.update({item_to_update: float(new_price)})
            print(f"{item_to_update} price updated successfully.\n")
            break
        else:
            print("Invalid input. Please enter a numeric value.")
else:
    print("Item not found in the price list.")

# Display updated price list
print("\n\t--- Updated Price List ---")
for item, price in price_list.items():
    print(f"\t{item}: ${price:.2f}")
