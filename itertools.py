# Itertools : a collection of functions that operate on iterables
# Product, permutations, combinations, combinations_with_replacement,accumulate, chain, compress, dropwhile, groupby, islice,
# takewhile, tee, zip_longest

# 1. Product
# The product() function returns an iterator that aggregates elements from the iterables.
from itertools import product
a = [1, 4]
b = [1, 2]

prod = product(a, b) # Cartesian product of a and b. Cartesian product is a list of tuples.
print(prod) # <itertools.product object at 0x7f8b8b8b9c18>
print(list(prod)) # [(1, 1), (1, 2), (4, 1), (4, 2)]

# Repeating the same iterable multiple times
prod = product(a, b, a) # Cartesian product of a and b. Cartesian product is a list of tuples.  
print(prod) # <itertools.product object at 0x7f8b8b8b9c18>
print(list(prod)) # [(1, 1, 1), (1, 1, 2), (1, 2, 1), (1, 2, 2), (4, 1, 1), (4, 1, 2), (4, 2, 1), (4, 2, 2)]

# 2. Permutations

# Permutation: a sequence of all possible orderings of the elements of a given iterable.
# lexicographic order: the order of the elements in the permutation is determined by the order of the elements in the iterable.

# The permutations() function returns an iterator that generates all possible permutations of the given iterable.
# Permutations are produced in lexicographic sort order. If the given iterable is sorted, the permutation tuples will be produced in sorted order.
from itertools import permutations
a = [1, 2, 3]
perm = permutations(a) # Permutations of a. Permutations are produced in lexicographic sort order.
print(perm) # <itertools.permutations object at 0x7f8b8b8b9c18>
print(list(perm)) # [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]

# Specifying the length of the permutation
perm = permutations(a, 2) # Permutations of a with length 2. Permutations are produced in lexicographic sort order.
print(perm) # <itertools.permutations object at 0x7f8b8b8b9c18>
print(list(perm)) # [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]

# 3. Combinations
# Combination: a sequence of elements taken from the iterable.
# The combinations() function returns an iterator that generates all possible combinations of the given length.
# Combinations are produced in lexicographic sort order. If the given iterable is sorted, the combination tuples will be produced in sorted order.
# No repeated elements in the combinations.
from itertools import combinations
a = [1, 2, 3]
comb = combinations(a, 2) # Combinations of a with length 2. Combinations are produced in lexicographic sort order.
print(comb) # <itertools.combinations object at 0x7f8b8b8b9c18>
print(list(comb)) # [(1, 2), (1, 3), (2, 3)]

## 3.1 Combinations with replacement
# The combinations_with_replacement() function returns an iterator that generates all possible combinations of the given length,
# allowing repeated elements.
from itertools import combinations_with_replacement
a = [1, 2, 3]
comb = combinations_with_replacement(a, 2) # Combinations of a with length 2. Combinations are produced in lexicographic sort order.
print(comb) # <itertools.combinations_with_replacement object at 0x7f8b8b8b9c18>
print(list(comb)) # [(1, 1), (1, 2), (1, 3), (2, 2), (2, 3), (3, 3)]

# 4. Accumulate
# The accumulate() function returns an iterator that yields the accumulated sum of the elements in the given iterable.
# The optional initializer value specifies the value to start with.
from itertools import accumulate
a = [1, 2, 3, 4, 5]
acc = accumulate(a) # Accumulate the elements of a.
print(acc) # <itertools.accumulate object at 0x7f8b8b8b9c18>
print(list(acc)) # [1, 3, 6, 10, 15] -> 1 + 0, 1 +2, 3 + 3, 6 + 4, 10 + 5

# 5. Chain
# The chain() function returns an iterator that yields the elements of the given iterables in sequence.
# The chain() function is equivalent to:
# for elem in iterable:
#     yield elem
# for elem in iterable2:
#     yield elem
# for elem in iterable3:
#     yield elem
from itertools import chain
a = [1, 2, 3]
b = [4, 5, 6]
c = [7, 8, 9]

chn = chain(a, b, c) # Chain the elements of a, b, c.
print(chn) # <itertools.chain object at 0x7f8b8b8b9c18>
print(list(chn)) # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 6. Compress
# The compress() function returns an iterator that yields the elements from the given iterable corresponding to the given condition.
# The condition is a function that takes an element and returns True or False.
from itertools import compress
a = [1, 2, 3, 4, 5]
cond = [True, False, True, True, False] # True for elements that should be included, False for elements that should be excluded.

cmp = compress(a, cond) # Compress the elements of a with the condition.
print(cmp) # <itertools.compress object at 0x7f8b8b8b9c18>
print(list(cmp)) # [1, 3, 5]

# 7. Dropwhile
# The dropwhile() function returns an iterator that yields the elements from the given iterable,
# except those elements that satisfy the given condition.
from itertools import dropwhile
a = [1, 2, 3, 4, 5]
cond = [True, False, True, True, False] # True for elements that should be included, False for elements that should be excluded.
drpw = dropwhile(lambda x: x < 3, a) # Dropwhile the elements of a that satisfy the condition. Drop all elements that are less than 3.
print(drpw) # <itertools.dropwhile object at 0x7f8b8b8b9c18>
print(list(drpw)) # [3, 4, 5]

# 8. Filterfalse
# The filterfalse() function returns an iterator that yields the elements from the given iterable,
# except those elements that satisfy the given condition.
from itertools import filterfalse
a = [1, 2, 3, 4, 5]
cond = [True, False, True, True, False] # True for elements that should be included, False for elements that should be excluded.
fltrf = filterfalse(lambda x: x < 3, a) # Filterfalse the elements of a that satisfy the condition.
print(fltrf) # <itertools.filterfalse object at 0x7f8b8b8b9c18>
print(list(fltrf)) # [3, 4, 5]

# 9. Groupby
# The groupby() function returns an iterator that groups the elements from the given iterable 
# into a sequence of tuples where the first element of each tuple is the value returned by the key
# function applied to the first element from the iterable, the second element is the iterable of all elements equal 
# to the group, and the third element is the iterable of all elements not equal to the group.
from itertools import groupby
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
grp = groupby(a, lambda x: x % 2) # Group the elements of a by the condition.
print(grp) # <itertools.groupby object at 0x7f8b8b8b9c18>
print(list(grp)) # [(False, [1, 3, 5, 7, 9]), (True, [2, 4, 6, 8, 10])]

# 10. Tee
# The tee() function returns two iterators that both iterate over the same iterable.
# The first iterator returned by the function is a reference to the iterable.
# The second iterator returned by the function is a copy of the iterable.
from itertools import tee
a = [1, 2, 3, 4, 5]
t = tee(a) # Tee the elements of a.
print(t) # (<itertools.tee object at 0x7f8b8b8b9c18>, <itertools.tee object at 0x7f8b8b8b9c18>)
print(list(t[0])) # [1, 2, 3, 4, 5]
print(list(t[1])) # [1, 2, 3, 4, 5]

# 11. Zip
# The zip() function returns an iterator that aggregates elements from each of the iterables.
# The iterator stops when the shortest iterable is exhausted.
from itertools import zip
a = [1, 2, 3]
b = [4, 5, 6]
z = zip(a, b) # Zip the elements of a and b. Generate tuples of the form (a[0], b[0]), (a[1], b[1]), (a[2], b[2]).
print(z) # <itertools.zip object at 0x7f8b8b8b9c18>
print(list(z)) # [(1, 4), (2, 5), (3, 6)]


