# A dictionary is a collection of key-value pairs.
# A key is a string that uniquely identifies the value.
# A value can be any Python object.
# Dicts are mutable, so you can change their values.
# Dicts are unordered, so you can't access them by index.
# Dicts are created with curly braces.

# Creating a dictionary
mydict = {"name": "Max", "age": 27} # Key-value pairs are separated by a colon
print(mydict) # {'name': 'Max', 'age': 27}

mydict = dict(name="Max", age=27) # Using a dict constructor, you dont need to specify the key-value pairs/ Uing quotes is not necessary
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