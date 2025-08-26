# Dictionary to store available items and their quantities
Store = {"Rice": 10, "Beans": 100, "Garri": 20}

while True:  # loop runs until a valid purchase is made
    purchase = input("Please input the item you want to buy: ").title()  # get item name from user (capitalize first letter)
    
    if purchase in Store:  # check if the entered item exists in the store
        try:
            qty = int(input(f"How many bags of {purchase} do you want to purchase? "))  # ask user for quantity
            
            # check if requested quantity is valid (not less than 1 and not more than available stock)
            if 1 <= qty <= Store[purchase]:
                print(f"\tPURCHASE SUCCESSFUL! Here is the inventory:\nBefore purchase: {Store}")  # show stock before purchase
                Store[purchase] -= qty  # deduct purchased quantity from the store
                print(f"After purchase: {Store}")  # show updated stock after purchase
                break  # exit loop after successful purchase
            else:
                # inform user of insufficient stock or invalid quantity
                print(f"Sorry, we only have {Store[purchase]} bags of {purchase} available.")
        
        except ValueError:
            # handle invalid input (non-integers like letters or symbols)
            print("Invalid input! Please enter a number for quantity.")
    
    else:
        # if the item is not in the store dictionary
        print("Item unavailable. Please try again.")