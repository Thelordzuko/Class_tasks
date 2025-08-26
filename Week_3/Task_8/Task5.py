Store = {"Rice": 10, "Beans": 100, "Garri": 20}   # Dictionary storing items and their available quantities

purchase = input(f"Please input the item you want to buy: ").title()   # Ask user for item to buy and capitalize first letter
qty = int(input(f"How many {purchase} you want to purchase: "))        # Ask user how many units of the item they want

print(f"Before purchase: {Store}")   # Print store items before purchase

Store[purchase] -= qty   # Deduct the purchased quantity from the store's stock

print(f"After purchase: {Store}")   # Print store items after purchase