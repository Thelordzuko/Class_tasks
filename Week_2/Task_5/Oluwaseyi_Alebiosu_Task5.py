# Task 1
item_1 = input("Please input your first favourite Nigerian dish: ") # collects input
item_2 = input("Please input your second favourite Nigerian dish: ") # collects input
item_3 = input("Please input your third favourite Nigerian dish: ") # collects input
dishes_list = (f"{item_1} {item_2} {item_3}").split() #to put dishes on the same line
dishes = tuple(dishes_list)
print(dishes)
print("\n".join(dishes))

# Task 2
friend_1 = input("Please input your first best friend's name: ") # collects input
friend_2 = input("Please input your second best friend's name: ") # collects input
friend_3 = input("Please input your third best friend's name: ") # collects input
friend_4 = input("Please input your fourth best friend's name: ") # collects input
friend_5 = input("Please input your fifth best friend's name: ") # collects input
friends_list = (f"{friend_1}, {friend_2}, {friend_3}, {friend_4}, {friend_5} ").split()
friends = tuple(friends_list)
print(friends[::-1])

# Task 3
state_1 = input("Please input a Nigerian state: ") # collects input
state_2 = input("Please input another Nigerian state: ") # collects input
state_3 = input("Please input another Nigerian state: ") # collects input
state_4 = input("Please input another Nigerian state: ") # collects input
state_5 = input("Please input another Nigerian state: ") # collects input
state_list = (f"{state_1}, {state_2}, {state_3}, {state_4}, {state_5}").split()
states = tuple(state_list)
print(f"{states[0]} {states[-1]}")
print("Lagos" in states)
print(len(states))

# Task 4
name = input("What is your first name? ")
age = input("How old are you? ")
colour = input("What is your favourite colour? ")
hometown = input("What is your hometown? ")
details = (f"{name} {age} {colour} {hometown}").split()
profile = tuple(details)
name, age, colour, hometown = profile
print(f"\n{name}\n{age}\n{colour}\n{hometown}\n")

# Task 5
item1 = input("Input your first item for your shopping list: ")
item2 = input("Second item: ")
item3 = input("Third item: ")
shopping_items = (f"{item1} {item2} {item3}").split()
shopping_list = tuple(shopping_items) 
shopping_list  = list(shopping_list)
item4 = input("Input the fourth item for your shopping list: ")
item5 = input("Input the fifth item for your shopping list: ")
new_items = (f"{item4} {item5}").split()
shopping_list.extend(new_items)
print("|".join(shopping_list))

# Task 6
day = ("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")
month = ("January","February","March","April","May","June","July","August","September","October","November","December")
details = (
    input("Enter your name: "),
    input("Enter your gender: "),
    input("Enter your course track: "),
    input("Enter the current month number (1-12): "),
    input("Enter the current day number (1-7): ")
)
name, gender, track, month, day = details
month = int(month) -1
day = int(day)
print(f"Stunent\'s name is: {name}\n Gender: {gender}\n Course track: {track}\n Month number: {month}\n Day number: {day}")

