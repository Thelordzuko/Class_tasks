#  Transport fare calculator
dist = float(input("what is the distance of your trip in km? "))
fare = float(input("How much is the fare per km? "))
total = dist * fare
total_dist = f"{total:.2f}"
print(f"Therefore, the total fare would be #{total_dist}.") # The total fare displayed to 2 decimal places