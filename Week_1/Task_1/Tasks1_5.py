#Task 1
# A Python program that prints out inputed information on separate lines
name = input("A pleasant day to you! Please enter your full name: ")
print("Hello,", name + ".")
university = input("Please enter your university of study: ")
print("Wonderful!")
lga = input("Please enter your local government area: ")
print("You\'re almost there,", name + ".")
Fav_food = input("Enter your favourite Nigerian Food: ")
print(f"Confirm your info: \n{name}\n{university}\n{lga}\n{Fav_food}")
confirm = input("Is your information correct? ")
print("Thank you for your time. have a great day!")


#Task 2
# A Python program that stores your name and state of origin in variables
name = input("What is your full name? ")
state = input(f"Hello {name}. What is your state of origin? ")
print(f"Thank you for your time! Your information is: \nName: {name} \nState of origin: {state}")


#Task 3
# A Python program for a simple timetable for a Nigerian secondary school using tab spacing and new lines
print("\t\t\t\t\t\t\tFIRELORD SECONDARY SCHOOL, ABEOKUTA, OGUN STATE.")
print("\t\t\t\t\t\t\t\t\tTIME-TABLE")
print("___________________________________________________________________________________________________________________________________________________________ ")
print("|\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t  |\n| DAY\TIME\t 8:00am - 10:00am\t 10:00am - 12:00pm\t 12:00pm -  2:00pm\t 2:00pm - 3:00pm\t 3:00pm - 5:00pm\t 5:00pm - 6:00pm  |")
print("|\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t  |\n| Monday\t    Mathematics\t\t\tFrench\t\t   Social Studies\t      Break\t\t      Yoruba \t\t      History     |")
print("| Tuesday\t  English Language\t   Home Economics\t       Physics\t\t      Break \t\t Basic Technology\t      Music       |")
print("| Wednesday\t      Biology\t\t       Commerce\t\t     Government\t\t      Break\t\t    Accounting\t\t    Economics     |")
print("| Thursday\t     Chemistry\t\t     Basic Science\t       French\t\t      Break\t\t Computer Science\t Social Studies   |")
print("| Friday\t    Mathematics\t\t\tHistory\t\t     Accounting\t\t      Break\t\t     Geography\t\t  Agric Science   |")
print("|_________________________________________________________________________________________________________________________________________________________|")


#Task 4
# Using variables to store name, class and best subject
name = input("Good Morning to you! Please enter you name: ")
print("Hello " + name + ",")
clas = input("What class are you presently in? ")
subject = input("What is your best subject? ")
# Using f-string to format and print the variables in a sentence
print(f"Your name is {name}. You are in {clas} class and your best subject is {subject}" )



# A short 3_line poem anout Nigeria printed with triple quotes
print("""
Nigeria, land of strength and flame,
Where dreams rise high and call your name,
Your heart beats bold through joy and pain.
""")
