# School fees breakdown
name = input("Please input the school name: ")
tuition = float(input("Thank you. Please input the amount for tuition fee: "))
hostel = float(input("Then input the amount for the hostel fee: "))
feeding = float(input("How much is the feeding fee? "))
total = tuition + hostel + feeding
print(f"SCHOOL FEES BREAKDOWN\n NAME: {name}\n TUITION FEE: #{tuition}\n HOSTEL FEE: #{hostel}\n FEEDING FEE: #{feeding}\n TOTAL: #{total}") #Reciept format printed with each fee on a new line
