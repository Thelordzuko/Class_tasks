# === Admission Enrollment Program ===
# This program simulates an admission screening process based on UTME score,
# school of choice, O'Level credits, and Post-UTME score.

print("\t\t===ADMISSION ENROLLMENT FORM===")  

# --- Step 1: Collect applicant's details ---
name = input("Dear applicant, what is your name? ") 
dept = input(f"Nice to meet you {name}. What department are you applying into? ")  

# Handle age input
while True:
    try:
        age = int(input(f"How old are you {name}? "))
        break
    except ValueError:
        print("Invalid input. Please enter a number for age.")

# Handle UTME score input
while True:
    try:
        score = int(input("Please input your UTME score: "))
        break
    except ValueError:
        print("Invalid input. Please enter a number for UTME score.")

# --- Step 2: Check UTME score validity ---
if 200 <= score <= 400:
    # --- Step 3: Confirm university choice ---
    school = input("Which university was your first choice? ").lower()
    
    if school == "unilag":
        # --- Step 4: Check O'Level requirements ---
        olevels = input("Do you have five (5) credit passes at one sitting in relevant O'Level subjects, including English Language and Mathematics? ").lower()
        
        if olevels == "yes":
            print("Way to go!\nYou are eligible to participate in the university's online Post-UTME screening.")
            
            # --- Step 5: Evaluate Post-UTME performance ---
            while True:
                try:
                    post_utme = int(input("Finally, please input your Post-UTME score(0-100): "))
                    break
                except ValueError:
                    print("Invalid input. Please enter a number between 0 and 100.")

            if 60 <= post_utme <= 100:
                print(f"\t\t!!!!CONGRATULATIONS!!!!\nDear {name}, you have been offered provisional admission into the department of {dept}. You may proceed to register on the school portal.")
            else:
                print("Sorry, your Post-UTME score is invalid. Better luck next time!")
        else:
            print("Sorry, you need to have the specified credits to be considered for admission.")
    else:
        print("Only UNILAG applicants are considered for admission.")
else:
    print("Invalid UTME score. Try again next time!")