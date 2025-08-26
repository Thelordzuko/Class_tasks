# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# score = int(input("Enter you test score: "))

# eligibility = (age < 18) and (score > 70)
# print(f"Candidate: {name}\nAge: {age}\nScore: {score}\nEligible: {eligibility}")
# """
# The code collects the inputs name, age and score respectively. 
# Then the eligibility is dependent on the user being less than 18 and with a score greater than 70.  
# The output is either true or false depending of if the criterias are met.
# """


citizenship = input("Are you a citizen of Nigeria? Yes or No: ").title()
enrollment = input("Are you a registered, full-time undergraduate student in a recognized Nigerian university?\n Yes or No: ").title()
scholarship = input("Are you currently receiving any other scholarship from an entity in the Oil and Gas industry?\n Yes or No: ").title()
Qualification = input("Do you have five distinctions (As and Bs) in relevant subjects, including English and Mathematics?\n Yes or no: ").title()

eligibility = (citizenship == "Yes") and (enrollment == "Yes") and (scholarship == "No") and (Qualification == "Yes")
print(f"Dear Applicant,\n Your eligibility is: {eligibility}")()