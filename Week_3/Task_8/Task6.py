utme = int(input("Input your JAMB score: "))   # Take JAMB score as integer input

choice = input("Which university is your first choice? " ).upper()   # Take university choice input and convert to uppercase

result = input("Do you have 5 credit passes at one sitting in relevant O'Level subjects, including English Language and Mathematics? Yes or No: ").title()   
# Ask if applicant has 5 credit passes in one sitting, capitalize first letter of response

screening = int(input("What is your Post-UTME score?  "))   # Take Post-UTME score as integer input

# Check eligibility conditions:
# - JAMB score between 200 and 400
# - University choice is UNILAG
# - 5 credit passes response is "Yes"
# - Post-UTME score is 270 or higher
eligibility  = (utme >= 200) and (utme <= 400) and (choice == "UNILAG") and (result == "Yes") and (screening >= 270)

# Display eligibility status to the applicant
print(f"Dear applicant, you eligibility for the Post-UTME screening is: {eligibility}")