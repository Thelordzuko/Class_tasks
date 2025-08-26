#  Price display with type casting
price = float(input("Good afternoon. What is the price of garri per paint? ")) #Asking for the price as a string and converting it to float
confirm = input(f"Just to confirm, it is {price} right? ") # Displaying the amount as a float but without the naira and kobo sign
print(f"Thank you for your time, #{price}k is a fair price.") # Displaying the amount as a float with the naira and kobo sign
