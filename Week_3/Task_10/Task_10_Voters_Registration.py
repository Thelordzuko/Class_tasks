# Unique Voters Registration System
# This program registers voters by storing their names in a set.
# If a voter tries to register more than once, it gives a warning.
# At the end, it displays the total number of unique voters.

# Create an empty set to store unique voters
voters = set()

while True:
    try:
        # Ask for voter name
        name = input("Enter voter's name (or type 'exit' to finish): ").title()

        # Check if user wants to stop registration
        if name == "Exit":
            break

        # Check for duplicate registration
        if name in voters:
            print(f"!!!Warning: {name} has already been registered!")
        else:
            voters.add(name)  # Add voter to the set
            print(f"{name} has been successfully registered ✅")

    except Exception as e:
        # Handle unexpected errors with steeze
        print(f"An error occurred: {e}. Please try again.")

# Display final result
print("\n=== Registration Complete ===")
print(f"Total unique voters registered: {len(voters)}")
print("List of registered voters:", voters)