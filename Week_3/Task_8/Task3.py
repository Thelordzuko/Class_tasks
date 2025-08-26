items = ['Shoe', 'Shirt', 'Tie', 'Belt', 'Socks']
prices = [1500, 1000, 1800, 1600, 2000]
cart_total = 0
add_items = []
print("AVAILABLE ITEMS WITH THEIR PRICES")
print(f"{items[0]}\t\t#{prices[0]}")
print(f"{items[1]}\t\t#{prices[1]}")
print(f"{items[2]}\t\t#{prices[2]}")
print(f"{items[3]}\t\t#{prices[3]}")
print(f"{items[4]}\t\t#{prices[4]}")
print("ITEMS IN CART")
item1 = input(f"Add {items[0]} to cart? Yes or No: ").title()
item2 = input(f"Add {items[1]} to cart? Yes or No: ").title()
item3 = input(f"Add {items[2]} to cart? Yes or No: ").title()
item4 = input(f"Add {items[3]} to cart? Yes or No: ").title()
item5 = input(f"Add {items[4]} to cart? Yes or No: ").title()

if item1 == ("Yes"):
    cart_total += prices[0]
    add_items.append(items[0])
    print(f"\nAdded {items[0]} to cart")
if item2 == ("Yes"):
    cart_total += prices[1]
    add_items.append(items[1])
    print(f"Added {items[1]} to cart")
if item3 == ("Yes"):
    cart_total += prices[2]
    add_items.append(items[2])
    print(f"Added {items[2]} to cart")
if item4 == ("Yes"):
    cart_total += prices[3]
    add_items.append(items[3])
    print(f"Added {items[3]} to cart")
if item5 == ("Yes"):
    cart_total += prices[4]
    add_items.append(items[4])
    print(f"Added {items[4]} to cart")
print("\n\t\t=== Cart summary ===")
print(f"Items in cart: {", ".join(add_items)}")
print(f"Total items: {len(add_items)}")
print(f"Total Price:, #{cart_total:,}")
