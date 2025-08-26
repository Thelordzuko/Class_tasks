# Federal Government Scholarship Eligibility Checker
# This program collects details from an applicant 
# and checks if they are eligible for the scholarship 
# based on nationality, enrollment status, scholarship history, and O'level results.

print("\t==== FEDERAL GOVERNMENT SCHOLARSHIP ====")

# Collect applicant's name
name = input("Dear applicant, please input your name: ")

# Ask for nationality and convert to Title case
citizen = input(f"Hello {name}. What is your nationality? ").title()

# Check if applicant is Nigerian
if citizen == "Nigerian" or citizen == "Nigeria":
    # Ask if applicant is a registered full-time undergraduate
    enrollment = input("Are you a registered, full-time undergraduate student in a recognized Nigerian university?\n Yes or No: ").title()
    if enrollment == "Yes":
        # Ask if applicant is already receiving another scholarship
        scholarship = input("You're almost there!\nAre you currently receiving any other scholarship from an entity in the Oil and Gas industry?\n Yes or No: ").title()
        if scholarship == "No":
            # Ask if applicant has required O'level results
            olevels = input("Finally, do you have five distinctions (As and Bs) in relevant subjects, including English and Mathematics?\nYes or No: ").title()
            if olevels == "Yes":
                # Final approval message
                print(f"CONGRATULATIONS {name}!!!\nYou are eligible for the Federal Government Scholarship.")
            else:
                # Reject if O'level results not good enough
                print("Unfortunately, You need better o'level results to meet the requirements. Thank you for your time.")
        else:
            # Reject if already receiving another scholarship
            print("Sorry, you are not eligible for this scholarship. Thank you for your time.")
    else:
        # Reject if not a full-time student
        print("Unfortunately, you must be a full-time student to qualify. Thank you for your time.")
else:
    # Reject if not Nigerian
    print("Sorry, you must be a citizen of Nigeria to be eligible for this scholarship. Thank you for your time.")