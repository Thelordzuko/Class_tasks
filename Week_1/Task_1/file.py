state_1 = input("Please input a Nigerian state: ").title() # collects input
state_2 = input("Please input another Nigerian state: ").title() # collects input
state_3 = input("Please input another Nigerian state: ").title() # collects input
state_4 = input("Please input another Nigerian state: ").title() # collects input
state_5 = input("Please input another Nigerian state: ").title() # collects input
state_list = (f"{state_1}, {state_2}, {state_3}, {state_4}, {state_5}").split()
print(state_list)
states = tuple(state_list)
print(states)
print(f"{states[0]} {states[-1]}")
print("Lagos" in states)
