print("\t\t\t\tWELCOME TO THE NIGERIAN AGRICULTURAL USSD SYSTEM\n This interface was created to help Nigerian farmers access real-time market prices and manage basic crop information.)")

while True:
    try:
        entry = input("Please proceed below:\n\t1. Register (for new users)\n\t2. Log in (for existing users)\n\t3. Exit\t\t").strip()
        if entry == "":
            print("Entry cannot be empty, try again!")
        elif entry.isalpha():
            print("Please select from 1-3")
            continue
        elif entry == "1":
            print("Let's get you signed up!")

            while True:
                name = input("Enter only your first name here: ").strip()
                if name == "":
                    print("Name cannot be empty! Try again")
                    continue
                elif name.isdigit():
                    print("Name cannot be a number! Try again")
                    continue
                elif name.isdigit() and name.isalpha():
                    print("Name cannot include a number! Try again.")
                    continue
                elif name.isalpha():
                    print(f"Welcome {name}.")

                    while True:
                        number = input("Enter your phone number: ").strip()
                        if number == "":
                            print("Number cannnot be empty!")
                            continue
                        elif number.isdigit() and len(number) == 11:

                            while True:
                                location = input("Enter location of your business(State): ")
                                if location == "":
                                    print("Location cannot be empty!")
                                    continue
                                elif location.isalpha():

                                    while True:
                                        try:
                                            crop = int(input("Select your primary crop:\n1.  Rice\n2.  Beans\n3.  Garri\n4.  Plantain\n5.  Cocoa\n6.  Palm fruit\n7.  Yam\n8.  Oil\n9.  Vegetables\n10. Others\t\t"))
                                            if crop == 10:
                                                spec = input("Please specify your primary crop: ")
                                            elif crop.isalpha():
                                                print("Please select from 1-10")
                                                continue
                                            elif crop == "":
                                                print("Input cannot be empty! Try again")
                                                continue
                                            elif crop.isdigit() and 1 <= int(crop) <= 7:
                                                
                                                while True:
                                                    size = input("Select your farm size:\n1. 1-5 plots of land\n2. 6 plots - 2 acres of land\n3. 1 hectare or more")
                                                    if size.isalpha():
                                                        print("Please select from 1-3")
                                                    elif size == "":
                                                        print("Farm size cannot be empty! Try again")
                                                    elif size == "1" or size == "2" or size == "3":
                                                        print(f"Thank you for your time {name}, you have been succesfully registered. Log in to continue.")
                                                    else:
                                                        print("Invalid farm size. Try again.")
                                            else:
                                                print("Invalid selection.")
                                        except Exception as e:
                                            print("Error. Try again.")
                                else:
                                    print("Input a valid location!")
                        else:
                            print("Input a valid phone number!")
                else:
                    print("Invalid input. Try again later")
                    
        elif entry == "2":
            print("Welcome back! Enter your details below to log in.")
            username = input("Username: ")
            password = input("Password: ")
        elif entry == "3":
            print("Thank you for using THE NIGERIAN AGRICULTURAL USSD SYSTEM. We hope to see you again soon!")
            break
        else:
            print("Please select from 1-3")
    except Exception as e:
        print("Invalid input. Try again later.")