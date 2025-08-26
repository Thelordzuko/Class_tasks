#  Electricity Bill Formatter
name = input("Dear customer, Please input your full name here: ")
units = int(input("Please input the Units consumed (kWh) "))
cost = float(input("Please input the Cost per unit: #"))
total = units * cost 
print(f"ELECTRICITY BILL:\n\t NAME: {name}\n\t UNITS CONSUMED:{units}kWh\n\t TOTAL: #{total}.") # The total cost displayed using escape sequences for line breaks