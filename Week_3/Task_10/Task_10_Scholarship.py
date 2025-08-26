# Federal Government Scholarship Eligibility Checker
# This program collects details from an applicant 
# and checks if they are eligible for the scholarship 
# based on nationality, enrollment status, scholarship history, and O'level results.

print("\t==== FEDERAL GOVERNMENT SCHOLARSHIP ====")

try:
    # Collect applicant's name
    name = input("Dear applicant, please input your name: ").strip().title()

    # Ask for nationality and convert to Title case
    citizen = input(f"Hello {name}. What is your nationality? ").strip().title()

    # Check if applicant is Nigerian
    if citizen in ["Nigerian", "Nigeria"]:
        # Ask if applicant is a registered full-time undergraduate
        enrollment = input("Are you a registered, full-time undergraduate student in a recognized Nigerian university?\nYes or No: ").strip().title()
        if enrollment == "Yes":
            # Ask if applicant is already receiving another scholarship
            scholarship = input("You're almost there!\nAre you currently receiving any other scholarship from an entity in the Oil and Gas industry?\nYes or No: ").strip().title()
            if scholarship == "No":
                # Ask if applicant has required O'level results
                olevels = input("Finally, do you have five distinctions (As and Bs) in relevant subjects, including English and Mathematics?\nYes or No: ").strip().title()
                if olevels == "Yes":
                    # Final approval message
                    print(f"\nCONGRATULATIONS {name}!!!\nYou are eligible for the Federal Government Scholarship.")
                else:
                    # Reject if O'level results not good enough
                    print("\nUnfortunately, you need better O'level results to meet the requirements. Thank you for your time.")
            else:
                # Reject if already receiving another scholarship
                print("\nSorry, you are not eligible for this scholarship. Thank you for your time.")
        else:
            # Reject if not a full-time student
            print("\nUnfortunately, you must be a full-time student to qualify. Thank you for your time.")
    else:
        # Reject if not Nigerian
        print("\nSorry, you must be a citizen of Nigeria to be eligible for this scholarship. Thank you for your time.")

except Exception as e:
    print("\nOops! Something went wrong. Please restart and provide valid information.")