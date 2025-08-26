student = {}   # Create an empty dictionary to store student details

student["name"] = input("Enter your name: ")   # Take input for student's name
student["age"] = int(input("Enter your age: "))  # Take input for student's age and convert to integer
student["scores"] = [30, 40, 55, 85]   # Assign a list of scores to the student

avg_scores = sum(student["scores"])/len(student["scores"])   # Calculate the average of the scores

student["Passed"] = avg_scores >= 50   # Check if average score is 50 or above and store True/False

C = (student["age"] >= 13) and (student["age"] <= 19)   # Check if student is a teenager (between 13 and 19)

# Print student record with details:
# Name, Age, Scores, Passed status, and Teenager status (but currently prints Passed instead of Teenager)
print(f"Student Record:\n Name: {student["name"]}\n Age: {student["age"]}\n Scores: {student["scores"]}\n Passed: {student["Passed"]}\n Teenager: {student["Passed"]}")   