# Sets : unordered and mutable collection of unique elements
# A set is created with braces just like a dictionary but no key-value pairs, 
# instead it has a set of unique elements, which are not duplicated.

# Sets are unordered and cannot be indexed.
# Sets are mutable and can be changed after creation.
# Sets are not iterable.
# Sets are not subscriptable.
# Sets are not hashable.

# Creating a set
# A set can be created with the set() function.
# The set() function takes a list as an argument and returns a set.

myset = set(1, 2, 3)
print(myset)

# Creating a set using curly braces
myset = {1, 2, 3}

# Adding elements to a set
myset.add(4)
print(myset) # {1, 2, 3, 4}

# Removing elements from a set
myset = {1, 2, 3, 4}
myset.remove(3)
print(myset) # {1, 2, 4}

# Using discard() to remove an element if it is present in the set
myset = {1, 2, 3, 4}
myset.discard(3)
print(myset) # {1, 2, 4}

# Using pop() to remove and return an arbitrary element from the set
myset = {1, 2, 3, 4}
myset.pop()
print(myset) # {1, 2, 3}

# Using clear() to remove all elements from the set
myset = {1, 2, 3, 4}
myset.clear()
print(myset) # set()

# Using del to remove a set
del myset

# Using the in operator to check if an element is in a set
myset = {1, 2, 3, 4}
print(1 in myset) # True
print(5 in myset) # False

# Using the not in operator to check if an element is not in a set
myset = {1, 2, 3, 4}
print(1 not in myset) # False
print(5 not in myset) # True

# Using the union() method to join two sets
# The union() method returns a new set with all the elements from both sets without duplicates.
myset = {1, 2, 3, 4}
myset2 = {3, 4, 5, 6}
myset3 = myset.union(myset2)
print(myset3) # {1, 2, 3, 4, 5, 6}

# Using the intersection() method to find the common elements in two sets
myset = {1, 2, 3, 4}
myset2 = {3, 4, 5, 6}
myset3 = myset.intersection(myset2)
print(myset3) # {3, 4}

# Using the difference() method to find the elements in the first set that are not in the second set
myset = {1, 2, 3, 4}
myset2 = {3, 4, 5, 6}
myset3 = myset.difference(myset2)
print(myset3) # {1, 2}

# Using the symmetric_difference() method to find the elements in either set that are not in both sets
myset = {1, 2, 3, 4}
myset2 = {3, 4, 5, 6}
myset3 = myset.symmetric_difference(myset2)
print(myset3) # {1, 2, 5, 6}

# Updateing a set
# The update() method adds all the elements from another set to the current set.
myset = {1, 2, 3, 4}
myset.update({5, 6})
print(myset) # {1, 2, 3, 4, 5, 6}

# Using intersection_update() to update the current set with the common elements in two sets
myset = {1, 2, 3, 4}
myset2 = {3, 4, 5, 6}
myset.intersection_update(myset2) # Updates the set by keeping only the common elements in both sets
print(myset) # {3, 4}

# Using difference_update() to update the current set with the elements in the first set that are not in the second set
myset = {1, 2, 3, 4}
myset2 = {3, 4, 5, 6}
myset.difference_update(myset2) # Updates the set by keeping only the elements in the first set that are not in the second set
print(myset) # {1, 2}

# Using symmetric_difference_update() to update the current set with the elements in either set that are not in both sets
myset = {1, 2, 3, 4}
myset2 = {3, 4, 5, 6}
myset.symmetric_difference_update(myset2) # Updates the set by keeping only the elements in either set that are not in both sets
print(myset) # {1, 2, 5, 6}

# Using the issubset() method to check if a set is a subset of another set
myset = {1, 2, 3, 4}
myset2 = {1, 2, 3, 4}
print(myset.issubset(myset2)) # True

# Using the issuperset() method to check if a set is a superset of another set
myset = {1, 2, 3, 4}
myset2 = {1, 2, 3, 4}
print(myset.issuperset(myset2)) # True

# Using the isdisjoint() method to check if a set has no common elements with another set
myset = {1, 2, 3, 4}
myset2 = {3, 4, 5, 6}
print(myset.isdisjoint(myset2)) # False

# Copying a set
# The copy() method returns a shallow copy of the set.
myset = {1, 2, 3, 4}
myset2 = myset.copy()
print(myset2) # {1, 2, 3, 4}

# Using the assignment operator to copy a set
myset = {1, 2, 3, 4}
myset2 = myset
print(myset2) # {1, 2, 3, 4}

#### The frozenset() function #################################################
# The frozenset() function returns an immutable frozenset object.
# The frozenset() function takes a list as an argument and returns a frozenset.

myfrozenset = frozenset(1, 2, 3)
print(myfrozenset) # frozenset({1, 2, 3})

myfrozenset.add(4) # AttributeError: 'frozenset' object has no attribute 'add'
myfrozenset.remove(3) # AttributeError: 'frozenset' object has no attribute 'remove'
