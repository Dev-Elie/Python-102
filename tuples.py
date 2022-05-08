# Tuples : ordered, immutable and allows duplicate elements
# Immutable : unable to be changed

# Tuples are useful for representing fixed data / data that cannot be changed

# Creating a tuple
my_tuple = ("Max", "John", "Mary")

# The parentheses are optional, so you can write:
my_tuple = "Max", "John", "Mary"

# If you have a tuple with only one element, you can write it without parentheses:
my_tuple = "Max"

# However, if you have a tuple with more than one element, you must use parentheses:
# Having a tuple with one element inside a parentheses will be considered as a string
my_tuple = ("Max")
print(type(my_tuple)) # <class 'str'>
# To get the type of a tuple, use the type() function or add a comma after the element

# Creating a tuple from an iterable
my_tuple = tuple(["Max", "John", "Mary"])

# Accessing elements in a tuple

# Indexing
my_tuple = ("Max", "John", "Mary")
print(my_tuple[0]) # Max
print(my_tuple[13]) # IndexError: tuple index out of range
print(my_tuple[-1]) # Mary

# Modifying a tuple
my_tuple = ("Max", "John", "Mary")
my_tuple[0] = "Maximilian" # TypeError: 'tuple' object does not support item assignment, a tuple is immutable

# Checking if an element is in a tuple  
my_tuple = ("Max", "John", "Mary")
print("Max" in my_tuple) # True
print("Maximilian" in my_tuple) # False

# Finding the length of a tuple
my_tuple = ("Max", "John", "Mary")
print(len(my_tuple)) # 3

# Counting the number of times an element occurs in a tuple
my_tuple = ("Max", "John", "Mary", "Max", "John", "Mary")
print(my_tuple.count("Max")) # 2

# Indexing the first occurrence of an element in a tuple
my_tuple = ("Max", "John", "Mary", "Max", "John", "Mary")
print(my_tuple.index("Max")) # 0

my_tuple = ("Max", "John", "Mary", "Max", "John", "Mary")
print(my_tuple.index("Max", 1)) # 3 (the first occurrence after the first one)

# Joining tuples
my_tuple = ("Max", "John", "Mary")
my_tuple2 = ("Maximilian", "John", "Mary")
my_tuple3 = my_tuple + my_tuple2
print(my_tuple3) # ('Max', 'John', 'Mary', 'Maximilian', 'John', 'Mary')

# Deleting a tuple
my_tuple = ("Max", "John", "Mary")
del my_tuple
# print(my_tuple) # NameError: name 'my_tuple' is not defined

# Converting a list to a tuple
my_list = ["Max", "John", "Mary"]
my_tuple = tuple(my_list)
print(my_tuple) # ('Max', 'John', 'Mary')

# Sorting a tuple
my_tuple = ("Max", "John", "Mary")
my_tuple.sort()
print(my_tuple) # ('John', 'Mary', 'Max')

# Reversing a tuple
my_tuple = ("Max", "John", "Mary")
my_tuple.reverse()
print(my_tuple) # ('Mary', 'John', 'Max')
print(my_tuple[::-1]) # ('Mary', 'John', 'Max') # Reversing the tuple


# Removing an element from a tuple
my_tuple = ("Max", "John", "Mary")
my_tuple.remove("John")
print(my_tuple) # ('Max', 'Mary')

# Removing an element from a tuple by index
my_tuple = ("Max", "John", "Mary")
del my_tuple[1]
print(my_tuple) # ('Max', 'Mary')

# Sliceing a tuple
my_tuple = ("Max", "John", "Mary")
print(my_tuple[1:]) # ('John', 'Mary') # From index 1 to the end
print(my_tuple[:2]) # ('Max', 'John') # From the beginning to index 2
print(my_tuple[::2]) # Beginning to end, skipping every second element, steps of 2
print(my_tuple[::1]) # Begins with the first element, skips 1 element, ends with the last element

# Unpacking a tuple
my_tuple = ("Max", "John", "Mary")
my_name, my_surname, my_lastname = my_tuple
print(my_name) # Max
print(my_surname) # John
print(my_lastname) # Mary

# Unpacking multiple elements from a tuple using *
my_tuple = ("Max", "John", "Mary")
my_name, *my_surname = my_tuple
print(my_name) # Max
print(my_surname) # ('John', 'Mary')

# Comparing a tuple to a list
import sys

my_tuple = ("Max", "John", "Mary")
my_list = ["Max", "John", "Mary"]
print(my_tuple == my_list) # True
print(my_tuple is my_list) # False

print(sys.getrefcount(my_tuple)) # 2
print(sys.getrefcount(my_list)) # 2

print(sys.getsizeof(my_tuple), "bytes") # 64 bytes
print(sys.getsizeof(my_list), "bytes") # 120 bytes


# Using timeit to measure the creation time of both tuples and lists
import timeit
print(timeit.timeit("my_tuple = ('Max', 'John', 'Mary')", number=1000000)) # 0.016634981002425775
print(timeit.timeit("my_list = ['Max', 'John', 'Mary']", number=1000000)) # 0.0591045210021548

# Observation: The creation of a tuple is faster than the creation of a list




