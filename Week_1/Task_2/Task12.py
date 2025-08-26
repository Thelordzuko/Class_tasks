# Simulated USSD Menu Interaction
greeting = input("How e dey be now?? Welcome to ZukoBank USSD interface.\n Please dial *323# to proceed. ")
menu = input("Please select a transaction you want to make?\n\t 1. Airtime Recharge\n\t 2. Data Bundles\n\t 3. TV Subscription ")
if menu == "1":
    print("You just selected 1. (Airtime Recharge)")
    amount = int(input("How much airtime would you like to purchase? "))
    print(f"TRANSACTION SUCCESSFUL. You have succesfully purchased #{amount} airtime to your line.")
elif menu == "2":
    print("You just selected 2. (Data Bundles)")
    data = int(input("Please input the amount of data to purchase: "))
    print(f"TRANSACTION SUCCESSFUL. You have successfully purchased #{data} data to your line.")
elif menu == "3":
    print("You just selected 3. (TV subscription)")
    subscription = int(input("Please input the amount for subscription: "))
    print(f"TRANSACTION SUCCESSFUL. You have successfully subscribed #{subscription} to your line.")
success = print("Thank you for using our services.")
