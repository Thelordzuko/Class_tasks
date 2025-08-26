# 1.
fruits = {
    input("Enter your favourite fruit: "),
    input("Enter another favourite fruit: "),
    input("Enter another favourite fruit: ")
}
print(f"Your favourite fruits are: {fruits}")

#2.
people = (input("Welcome to this seminar! Please use a space after every name inputed: "))
people.split()
people = set(people)
people = list(people)
people.sort()
print(f"The list of attendees are: {people}")

#3.
seat_numbers = {"1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50"}
bookings =  input("Please enter the seat numbers to be booked separated by a space: ")
seat_numbers.discard(bookings)
print(f"The available seat numbers are:\n {seat_numbers}") 

#4.
voters_list = set()
name1 = input("Enter the voter's name: ").title()
if name1 not in voters_list:
    voters_list.add(name1)
else:
    print("This user is already registered")
name2 = input("Enter the voter's name: ").title()
if name2 not in voters_list:
    voters_list.add(name2)
else:
    print(f"This user {name2} is already registered")
name3 = input("Enter the voter's name: ").title()
if name3 not in voters_list:
    voters_list.add(name3)
else:
    print(f"This user {name3} is already registered")
print("Voter registration successful. The total of registered users is:", len(voters_list))