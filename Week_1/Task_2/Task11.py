#  Nigerian Currency Converter
naira = float(input("How much do you want to convert in Naira(#)? ")) 
dollar = float(input("What is the exchange rate of US dollars($) in Naira? "))
pounds = float(input("What is the exchange rate of British pounds(£) in Naira? "))
dollar_result = naira/dollar #conversion of amount in naira to dollar
pounds_result = naira/pounds #conversion of amount in naira to british pounds
dollar_result_in_thousands = f"{dollar_result:,}" #to add the thousands separator
pounds_result_in_thousands = f"{pounds_result:,}" #to add the thousands separator 
print(f"Therefore:\n US Dollars amount = ${dollar_result_in_thousands}\n British Pounds amount = £{pounds_result_in_thousands}") #printed result with currency symbol and thousand separator using escape sequences