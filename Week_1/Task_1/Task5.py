#  Daily Market Teport
name = input("Please input the market name: ")
number = int(input("Please input the number of traders: "))
revenue = float(input("Please input the daily revenue of the market: "))
revenue_formatted = f"{revenue:,}"
print(f"At {name} market, there are {number} traders. The daily generated revenue is #{revenue_formatted}") #Result displayed using f-string formatting and commas for thousands separator
