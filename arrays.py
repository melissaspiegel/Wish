"""
 Operations on Arrays
"""
numbers = [1, 2, 3, 4, 5, 6]

# Accessing Elements
# use the index operator on a list to access values using an index. Note that index values start 0
print("Accessing Array Elements",numbers[2]) # returns 3 

# Using an index that is out of bounds of the 
# current range of values results in a runtime error.
# Results IndexError: list index out of range
# print(numbers[12])

# List legnth
# To Determine the number of items in a list use the len function
# Returns 6
# print(len(numbers))

for i in range(len(numbers)):
    # print(numbers[i])
    continue

# Time Complexity: 0(N) - Linear Time
# range(len(numbers)) generates a sequence of indices from 0 to len(numbers) - 1.
# numbers[i] accesses elements by index similiar to how arrays work in low level languages
for i in range(len(numbers)):
  print(f"Index {i} → Value {numbers[i]}")

# ======= List Operators ===========

# To add to a list, use the append(x) method
numbers.append(7)
# To add (or concatenate) one list to another, use extend(iterable)
numbers.extend([8, 9, 10])
# To insert an item into a list at a given position. Here the value 11 is inserted at index position 10.
numbers.insert(10, 11)
# Use the remove(x) method to remove an item from a list. remove() takes a value as an argument and removes the first element in the list that matches the argument.
numbers.remove(11)
# Searching for the position of an element in a list is possible using the index(x)
numbers.index(4)
# Updates first element in list to 22
numbers[0] = 22 

# Creating Array Slices
# Often times you will want to extract or query only a ortion of an array.
# Array slices are created when a range is used with a subscript
# Subscript example


