# A dictionary is a collection of key-value pairs.
# A key is a string that uniquely identifies the value.
# A value can be any Python object, including other dictionaries but not lists. Using a list returns an error(Unhashable type: 'list').
# Dicts are mutable, so you can change their values.
# Dicts are unordered, so you can't access them by index.
# Dicts are created with curly braces.

# Creating a dictionary
mydict = {"name": "Max", "age": 27} # Key-value pairs are separated by a colon
print(mydict) # {'name': 'Max', 'age': 27}

mydict = dict(name="Max", age=27) # Using a dict constructor, you dont need to specify the key-value pairs/ Using quotes is not necessary
print(mydict) # {'name': 'Max', 'age': 27}

# Accessing elements in a dictionary
# Indexing
mydict = {"name": "Max", "age": 27}
print(mydict["name"]) # Max
print(mydict["age"]) # 27
# print(mydict["height"]) # KeyError: 'height'

# Modifying a dictionary
mydict = {"name": "Max", "age": 27}
mydict["name"] = "Maximilian" # Modifying a value
print(mydict) # {'name': 'Maximilian', 'age': 27}

# Adding a new key-value pair
mydict = {"name": "Max", "age": 27}
mydict["height"] = 1.75 # Adding a new key-value pair
print(mydict) # {'name': 'Max', 'age': 27, 'height': 1.75}

# Removing a key-value pair
# Using del
# del(): 
mydict = {"name": "Max", "age": 27}
del mydict["age"] # Removing a key-value pair
print(mydict) # {'name': 'Max'}

# Using pop
# pop(): removes the last key-value pair from a dictionary, can use a key to remove a specific key-value pair
mydict = {"name": "Max", "age": 27}
mydict.pop("age")
print(mydict) # {'name': 'Max'}

# Using popitem 
# popitem(): Removes the last inserted key-value pair
mydict = {"name": "Max", "age": 27}
mydict.popitem() # Removing a key-value pair
print(mydict) # {'name': 'Max'}

# Using clear
# clear(): Removes all key-value pairs from a dictionary
mydict = {"name": "Max", "age": 27}
mydict.clear() # Removing all key-value pairs
print(mydict) # {}

# Checking if a key is in a dictionary
# in: checks if a key is in a dictionary
mydict = {"name": "Max", "age": 27}
"name" in mydict # True
"age" in mydict # True
"height" in mydict # False

# Checking if a value is in a dictionary
# in: checks if a value is in a dictionary
mydict = {"name": "Max", "age": 27}
"Max" in mydict # True
27 in mydict # True
1.75 in mydict # False

# Checking if a key-value pair is in a dictionary
# in: checks if a key-value pair is in a dictionary
mydict = {"name": "Max", "age": 27}
("name", "Max") in mydict # True
("age", 27) in mydict # True
("height", 1.75) in mydict # False

# Check for an item in a dictionary using the in operator and the get() method
# get(): Returns the value for the specified key, or a default value if the key is not found
mydict = {"name": "Max", "age": 27} 
mydict.get("name") # Max    
mydict.get("age") # 27
mydict.get("height") # None
mydict.get("height", 1.75) # 1.75


# Checking using the keys() method
# keys(): returns a list of all keys in a dictionary
mydict = {"name": "Max", "age": 27}
print(mydict.keys()) # dict_keys(['name', 'age'])

# for loop with a value
mydict = {"name": "Max", "age": 27}
for value in mydict.values():
    print(value) # Max, 27

# for loop with a key-value pair
mydict = {"name": "Max", "age": 27}
for key, value in mydict.items():
    print(key, value) # name Max, age 27

# Print value given a key using for loop
mydict = {"name": "Max", "age": 27}
for key in mydict:
    print(mydict[key]) # Max, 27

# Checking if a dictionary is empty
# len(): checks the number of key-value pairs in a dictionary
mydict = {"name": "Max", "age": 27}
len(mydict) # 2

# Looping through a dictionary
# for loop
mydict = {"name": "Max", "age": 27}
for key in mydict:
    print(key) # name, age

# Copy a dictionary
# copy(): returns a copy of a dictionary
mydict = {"name": "Max", "age": 27}
mydict2 = mydict.copy()
print(mydict2) # {'name': 'Max', 'age': 27}

# assignment operator
mydict = {"name": "Max", "age": 27}
mydict2 = mydict
mydict2["name"] = "Maximilian"
print(mydict) # {'name': 'Maximilian', 'age': 27}
print(mydict2) # {'name': 'Maximilian', 'age': 27}

# Observe that the two dictionaries are the same, however the two variables are different.
# This is because the two variables are pointing to the same dictionary.
# This is called a shallow copy.

# using the dict() constructor
mydict = dict(name="Max", age=27)
mydict2 = dict(mydict)
print(mydict2) # {'name': 'Max', 'age': 27}

# Using th isinstance() function to check if a variable is a dictionary
# isinstance(): checks if an object is an instance of a class
mydict = {"name": "Max", "age": 27}
isinstance(mydict, dict) # True
isinstance(mydict, list) # False
isinstance(mydict, tuple) # False
isinstance(mydict, set) # False
isinstance(mydict, str) # False
isinstance(mydict, int) # False
isinstance(mydict, float) # False
isinstance(mydict, bool) # False
isinstance(mydict, type) # False

# Merging two dictionaries
# update(): merges two dictionaries, overwriting the values for common keys
mydict = {"name": "Max", "age": 27}
mydict2 = {"height": 1.75}
mydict.update(mydict2)
print(mydict) # {'name': 'Max', 'age': 27, 'height': 1.75}

