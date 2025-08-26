user_input = input("Enter three names separated by commas: ")
name_list = [name.strip() for name in user_input.split(",")]
unique_names = set(name_list)
name_lengths = {name: len(name) for name in unique_names}
print("\n\t--- Registered Members ---")
for name, length in name_lengths.items():
    print(f"\t{name} (Length: {length}")# Ask user to enter names
user_input = input("Enter three names separated by commas: ")
name_list = [name.strip() for name in user_input.split(",")]
unique_names = set(name_list)
name_lengths = {name: len(name) for name in unique_names}
print("\n\t--- Registered Members ---")
for name, length in name_lengths.items():
    print(f"\t{name} (Length: {length})")