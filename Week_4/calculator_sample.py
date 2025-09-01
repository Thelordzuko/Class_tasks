import math

def add():
    try:
        while True:
            num1 = input("Enter first number: ").strip()
            num2 = input("Enter second number: ").strip()
            if num1.isalpha() or num2.isalpha():
                print("Entry cannot be a letter! Try again.")
                continue
            elif num1 == "" or num2 == "":
                print("Entry cannot be empty! Try again.")
                continue
            else:
                result = float(num1) + float(num2)
                print(f"Result is: {result}")
            break
    except Exception as e:
        print("Invalid input. Please try again later.")
def subtract():
    try:
        while True:
            num1 = input("Enter first number: ").strip()
            num2 = input("Enter second number: ").strip()
            if num1.isalpha() or num2.isalpha():
                print("Entry cannot be a letter! Try again.")
            elif num1 == "" or num2 == "":
                print("Entry cannot be empty: ")
            else:
                result = float(num1) - float(num2)
                print(f"Result is: {result}")
            break
    except Exception as e:
        print("Invalid input. Please try again later.")

def divide():
    try:
        while True:
            num1 = input("Enter first number: ").strip()
            num2 = input("Enter second number: ").strip()
            if num1.isalpha() or num2.isalpha():
                print("Entry cannot be a letter! Try again.")
            elif num1 == "" or num2 == "":
                print("Entry cannot be empty! Try again.")
            else:
                result = float(num1) / float(num2)
                print(f"Result is: {result}")
            break
    except Exception as e:
        print("Invalid input. Try again later.")

def multiply():
    try:
        while True:
            num1 = input("Enter first number: ").strip()
            num2 = input("Enter second number: ").strip()
            if num1.isalpha() or num2.isalpha():
                print("Entry cannot be a letter! Try again.")
            elif num1 == "" or num2 == "":
                print("Entry cannot be empty! Try again.")
            else:
                result = float(num1) * float(num2)
                print(f"Result is: {result}")
            break
    except Exception as e:
        print("Invalid input. Try again later.")

def modulus():
    try:
        while True:
            num1 = input("Enter first number: ").strip()
            num2 = input("Enter second number: ").strip()
            if num1.isalpha() or num2.isalpha():
                print("Entry cannot be a letter! Try again.")
            elif num1 == "" or num2 == "":
                print("Entry cannot be empty! Try again.")
            else:
                result = float(num1) % float(num2)
                print(f"Result is: {result}")
            break
    except Exception as e:
        print("Invalid input. Try again later.")

def exponentiation():
    try:
        while True:
            num1 = input("Enter first number: ").strip()
            num2 = input("Enter second number: ").strip()
            if num1.isalpha() or num2.isalpha():
                print("Entry cannot be a letter! Try again.")
            elif num1 == "" or num2 == "":
                print("Entry cannot be empty! Try again.")
            else:
                result = float(num1) ** float(num2)
                print(f"Result is: {result}")
    except Exception as e:
        print("Invalid input. Try again later.")

def sqrt():
    try:
        while True:
            num1 = input("Enter first number: ").strip()
            if num1.isalpha():
                print("Entry cannot be a letter! Try again.")
            elif num1 == "":
                print("Entry cannot be empty! Try again.")
            else:
                num1 = float(num1)
                result = math.sqrt(num1)
                print(f"Result is: {result}")
                break
    except e:
        print("Invalid input. Try again later.")

while True:
    try:
        print("\n===== CALCULATOR =====")
        print("\n1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exponentiation")
        print("6. Modulus")
        print("7. Square root")
        print("0. Exit")
        choice = input("\nChoose your operation: ")
        if choice == "1":
            print("\n")
            add()
        elif choice == "2":
            print("\n")
            subtract()
        elif choice == "3":
            print("\n")
            multiply()
        elif choice == "4":
            print("\n")
            divide()
        elif choice == "5":
            print("\n")
            exponentiation()
        elif choice == "6":
            print("\n")
            modulus()
        elif choice == "7":
            print("\n")
            sqrt()
        elif choice == "0":
            print("\nYou canceled the operation.")
            break
        else:
            ("Error.")
            break
    except Exception as e:
        print("Invalid input, please try again later.")





        