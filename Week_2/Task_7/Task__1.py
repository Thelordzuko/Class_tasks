# Ask the user to input the student's name and store it in the variable 'name'
name = input("Enter student's name: ")

# Ask the user to input the student's age, convert it to an integer, and store in 'age'
age = int(input("Enter student's age: "))

# Ask the user to input the student's gender and store it in 'gender'
gender = input("Enter student's gender: ")

# Ask the user to input courses (separated by spaces) and split them into a list
courses = input("Enter courses (separated by spaces): ").split()

# Remove extra spaces from each course name
courses = [course.strip() for course in courses]

# Create an empty dictionary to store student data
student_data = {}

# Store the collected details into the dictionary
student_data['Name'] = name
student_data['Age'] = age
student_data['Gender'] = gender
student_data['Courses'] = courses

# Print a formatted header using escape sequences (\n for new line, \t for tab)
print("\n\t    STUDENT\'S BIO DATA ")

# Print the student's name, age, and gender
print(f"\tName    : {student_data['Name']}")
print(f"\tAge     : {student_data['Age']}")
print(f"\tGender  : {student_data['Gender']}")

# Print the student's courses in a numbered list
print("\tCourses :")
for i, course in enumerate(student_data['Courses'], start=1):
    print(f"\t  {i}. {course}")
