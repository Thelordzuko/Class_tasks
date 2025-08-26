name = input("Enter student's name: ")
age = int(input("Enter student's age: "))
gender = input("Enter student's gender: ")
courses = input("Enter courses (separated by spaces): ").split()
courses = [course.strip() for course in courses]
student_data = {}
student_data['Name'] = name
student_data['Age'] = age
student_data['Gender'] = gender
student_data['Courses'] = courses

# using escape sequences
print("\n\t    STUDENT\'S BIO DATA ")
print(f"\tName    : {student_data['Name']}")
print(f"\tAge     : {student_data['Age']}")
print(f"\tGender  : {student_data['Gender']}")
print("\tCourses :")
for i, course in enumerate(student_data['Courses'], start=1):
    print(f"\t  {i}. {course}")