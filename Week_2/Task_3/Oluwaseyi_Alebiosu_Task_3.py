#Oluwaseyi
# 1.
location = input("What is your location? ")
print(f"You are presently in {location.upper()}")

# 2.
location = "Python"
print(f"The first character of the string is {location[0]} and the last character is {location[-1]}")

# 3.
name = input("What is your name? ")
print(f"Hello {name}!")

# 4. 
character = "Oluwaseyi" 
print(character.find(character[-1])+1) 

# 5.
entry = "Hello World"
print(entry.replace("World", "Python"))

# 6.
entry = "Python can be difficult."
print("Python" in entry)

# 7.
colour = "Orange"
print(colour[-1::-1])

# 8.
school = "    Unilag     "
print(school.lstrip())

# 9.
entry = input("Dear User, what is on your mind?: ")
vowel_a = entry.lower().count("a")
vowel_e = entry.lower().count("e")
vowel_i = entry.lower().count("i")
vowel_o = entry.lower().count("o")
vowel_u = entry.lower().count("u")
number_of_vowels = vowel_a + vowel_e + vowel_i + vowel_o + vowel_u
print(f"The number of vowels in your sentence is {number_of_vowels}")

# 10.
entry = "1234"
int_entry = int(entry)
sol = int_entry * 2
print(sol)

#  11.
string = 'apple, banana, orange' 
print(string.split(',')) 

# 12.
sentence = input('Please enter a sentence :') 
print('\n'.join(sentence.split())) 

# 13.
address = "No. 13 market road, Ogun state."
print(address.replace(" ", "_"))

# 14.
fruit = "Banana"
print(fruit.count"a")

# 15.
entry = "Greatness from small beginnings."
print(entry.startswith("https://"))  # False