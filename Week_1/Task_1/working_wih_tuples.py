# creating tuples 

# 1. Using parentheses ()
fruits = ("apple", "banana", "cherry")
print(fruits) 

# 2. Without parentheses (tuple packing)
numbers = 1, 2, 3
print(numbers)  

# 3. Single-item tuple (must include a comma)
single_item = ("apple",)
print(single_item)       
print(type(single_item)) 

# 4. Using the tuple() constructor
fruits_list = ["apple", "banana", "cherry"]
fruits_tuple = tuple(fruits_list)
print(fruits_tuple)  

#TUPLE XTERISTICS
# Ordered
colors = ("red", "green", "blue")
print(colors[0])  
print(colors[1])
# Immutable ( uncomment and run. This will cause an error)
# colors[1] = "yellow"  

# Allow duplicates
numbers = (1, 2, 2, 3)
print(numbers) 

# Mixed data types
mixed = ("apple", 3, True, 5.6)
print(mixed)

# Nested tuples
nested = (("a", "b"), (1, 2))
print(nested)  # (('a', 'b'), (1, 2))

#TUPLE OPERATIONS
# 1. Indexing
fruits = ("apple", "banana", "cherry")
print(fruits[1])   # banana
print(fruits[-1])  # cherry

# 2. Slicing
print(fruits[0:2])   # ('apple', 'banana')
print(fruits[::-1])  # ('cherry', 'banana', 'apple')

# 3. Concatenation
tuple1 = (1, 2)
tuple2 = (3, 4)
result = tuple1 + tuple2
print(result)  # (1, 2, 3, 4)

# 4. Repetition
nums = (1, 2)
print(nums * 3)  # (1, 2, 1, 2, 1, 2)

# 5. Membership
fruits = ("apple", "banana", "cherry")
print("banana" in fruits)  # True
print("grape" not in fruits)  # True

# 6. Iteration
for S in fruits:
    print(S) # print out each individual item in the list of items
for fruit in fruits:
    print(fruit) # print out each individual item in the list of items

#UNPACKING TUPLES
# dont count() and dot index()

numbers = (1, 2, 2, 3, 4)

print(numbers.count(2))  # 2  (counts occurrences of 2)
print(numbers.count(4))  # 1  (counts occurrences of 4)
print(numbers.index(3))  # 3  (position of first occurrence of 3)
print(numbers.index(2))  # 1  (position of first occurrence of 2)

# Converting Between List and Tuple
# Tuple to List
t = (1, 2, 3)
lst = list(t)
lst.append(4)
print(lst)  # [1, 2, 3, 4]

# List back to Tuple
t = tuple(lst)
print(t)  # (1, 2, 3, 4)

# Tuple to List
fruits = ("apple", "banana", "cherry")
lst = list(fruits)
lst.append(3.142)
print(lst) # ['apple', 'banana', 'cherry', 3.142]

# List back to Tuple
fruits = tuple(lst)
print(fruits) # ('apple', 'banana', 'cherry', 3.142)

# Built-in Functions with Tuples
nums = (4, 1, 7, 3)
print(len(nums))   # 4
print(max(nums))   # 7
print(min(nums))   # 1
print(sum(nums))   # 15