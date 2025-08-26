#Zukode
#ZukoBank USSD interface

balance = 10000  # initial account balance

while True:  # loop runs until user chooses to exit
    print("\nWelcome to ZukoBank USSD services:")  # display welcome message
    print("1. Balance check")  # option to check balance
    print("2. Airtime recharge")  # option to buy airtime
    print("3. Transfer")  # option to transfer money
    print("4. Exit")  # option to exit program

    choice = input("Enter choice: ")  # user selects an option

    if choice == "1":  # balance check option
        print(f"Your balance is {balance}")  # show account balance
    elif choice == "2":  # airtime recharge option
        amount = int(input("Input airtime amount: #"))  # ask for recharge amount
        if amount <= balance:  # check if user has enough money
            balance -= amount  # deduct recharge amount from balance
            print(f"Airtime recharge successful! Your balance is #{balance}")  # success message
        else:
            print("Insufficient funds. Thank you for your time!")  # failure message
    elif choice == "3":  # money transfer option
        amt = int(input("Enter transfer amount: "))  # ask for transfer amount
        if amt <= balance:  # check if user has enough money
            balance -= amt  # deduct transfer amount
            print(f"Transfer successful! Your balance is {balance}")  # success message
        else:
            print("Insufficient funds. Transfer failed.")  # failure message
    elif choice == "4":  # exit option
        print("Thank you for using ZukoBank. Have a nice day!")  # goodbye message
        break  # stop the loop and end the program
    else:
        print("Invalid option. Please try again.")  # if input is not 1–4