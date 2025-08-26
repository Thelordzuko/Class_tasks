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
state_list = (f"{state_1}, {state_2}, {state_3}, {state_4}, {state_5}") .split()
states = tuple(state_list)
print(states[0])
prinit(states[-1])