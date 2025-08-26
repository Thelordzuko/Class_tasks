#Task 1
quote = input("What is your favourite quote? ") #collects input from user
print(f"\"{quote.title()}\" is a profound quote. Thank you for your time.") #prints input with quotation marks and title case

#Task 2
shopping_list = [] # creates an empty list
item_1 = input("Please input your first shopping item: ") # collects input
item_2 = input("Please input your second shopping item: ")  # collects input
item_3 = input("Please input your third shopping item: ") # collects input
shopping_list.extend([item_1, item_2, item_3]) # simultaneously adds them to the empty list
print(",".join(shopping_list)) # displays as a single string separated by comas

#Task 3
sent = input("Please input a sentence: ") # collect input
split_sent = sent.split() # splits the sentence
print(f"The sentence has {len(split_sent)} words.") #prints how many words

#Task 4
names = input("Enter 5 names separated by spaces: ") #collects input
names = names.split() #splits
names = [name.lower() for name in names] # Converts the names to lowercase per line
names.sort()  # Sorts the names alphabetically
names = [print(name) for name in names] # prints line by line (iterates)

#Task 5
names_list = [input(f"Enter the name of student {i + 1}: ") for i in range(3)] #individually collects names
scores_list = [input(f"Enter the score for {name}: ") for name in names_list] # individually collects scores
print(f"NAME \t\tSCORE")
[print(f"{names_list[i]} \t\t{scores_list[i]}") for i in range(len(names_list))]

#Task 6
word = input("Please input a word: ") # collect input
print(f"This word has {len(word)} letters") #prints the length of a word
print(word.isupper()) #checks if its all upper
print(word.islower()) #checks if its all lower
print(word.istitle()) ##checks if its title case
print(word[::-1]) #reverses the word using word slicing

#Task 7
cities = ["Berlin","Lagos","Ibadan","Asaba","Delta"] # a list of cities
city = input("Enter a new city: ") # collects an input(cities)
cities[2] = city # changes the second value in the list with the new input
cities.pop(-1) # removes the last city in list of cities
cities.insert(0,"California") # insert a new city at the beginning 
print(cities) #prints the  new list of cities