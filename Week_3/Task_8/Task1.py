num1 = int(input("Enter first number: ")) 
num2 = int(input("Enter second number: ")) 

print(f"{num1} == {num2} : {num1 == num2}")
#{num1} == {num2} simply shows the inputed values separated by the operator because they are in separate brackets
#{num1 == num2} simply shows if the first and second input are equal to eachother thus it will give either true or false

print(f"{num1} != {num2} : {num1  != num2}")
#{num1} != {num2}  simply shows the inputed values separated by the operator but doesn't run because they are in separate curly brackets
#{num1 != num2} shows if the first and second input are not equal to eachother thus it will give either true or false

print(f"{num1} > {num2} : {num1 > num2}")
#{num1} != {num2}  simply shows the inputed values separated by the operator but doesn't run because they are in separate curly brackets
#{num1 != num2} shows if the first input is greater than the second input thus it will give either true or false

print(f"{num1} < {num2} : {num1 < num2}")
#{num1} != {num2}  simply shows the inputed values separated by the operator but doesn't run because they are in separate curly brackets
#{num1 != num2} shows if the first input is less than the second input thus it will give either true or false

#The program can be used in any of the following scenarios:
#i.   To check the ratio of females to male in a given setting
#ii.  To check eligibility for ad,ission based on age and cut-off mark
#iii. To check the status of a student's score in an exam if he/she passed or not

#Eligibility for admission
age = 14
score = 78
#must be older or equal to 16 and score above 70
fulfilled = (age >= 16) and (score > 75)
print("Admission criteria:", fulfilled) #output-false
