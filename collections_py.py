# Collections: containers used for storing data

## 1. Counter: # Counter is a dictionary subclass that counts hashable objects.
from collections import Counter

a = "aaaaajdkdlllldjjjjjdnnnnndtttt"
my_counter = Counter(a)
print(my_counter) # Counter({'j': 6, 'a': 5, 'd': 5, 'n': 5, 'l': 4, 't': 4, 'k': 1})

# Counter methods
# 1. items() - returns a list of (element, count) pairs
print(my_counter.items()) # dict_items([('a', 5), ('j', 6), ('d', 5), ('k', 1), ('l', 4), ('n', 5), ('t', 4)])
# 2. keys() - returns a list of unique elements
print(my_counter.keys()) # dict_keys(['a', 'j', 'd', 'k', 'l', 'n', 't'])
# 3. values() - returns a list of counts of each element
print(my_counter.values()) # dict_values([5, 6, 5, 1, 4, 5, 4])
# 4. most_common() - returns a list of the n most common elements and their counts
print(my_counter.most_common(3)) # [('a', 5), ('j', 6), ('d', 5)]
# 5. subtract() - subtracts a counter from another
print(my_counter.subtract({'a': 1, 'j': 1, 'd': 1, 'k': 1, 'l': 1, 'n': 1, 't': 1})) # Counter({'a': 4, 'j': 5, 'd': 4, 'k': 0, 'l': 3, 'n': 4, 't': 3})
# 6. update() - adds/updates counts for elements in another counter
print(my_counter.update({'a': 1, 'j': 1, 'd': 1, 'k': 1, 'l': 1, 'n': 1, 't': 1})) # None
print(my_counter) # Counter({'a': 6, 'j': 7, 'd': 6, 'k': 2, 'l': 4, 'n': 6, 't': 6})
# 7. clear() - removes all elements from the counter
my_counter.clear()
print(my_counter) # Counter()
# 8. copy() - returns a copy of the counter
my_counter.update({'a': 1, 'j': 1, 'd': 1, 'k': 1, 'l': 1, 'n': 1, 't': 1})
my_counter_copy = my_counter.copy()
print(my_counter_copy) # Counter({'a': 1, 'j': 1, 'd': 1, 'k': 1, 'l': 1, 'n': 1, 't': 1})
# 9. fromkeys() - returns a new counter with elements from a set of keys
print(Counter.fromkeys(['a', 'j', 'd', 'k', 'l', 'n', 't'])) # Counter({'a': 0, 'j': 0, 'd': 0, 'k': 0, 'l': 0, 'n': 0, 't': 0})
# 10. elements() - returns an iterator over elements repeating each as many times as its count
print(my_counter.elements()) # <generator object Counter.elements at 0x7f8b8f8f8b50>

## 2. defaultdict: # defaultdict is a dictionary subclass that provides default values for missing keys.
from collections import defaultdict

d = defaultdict(int)
d['a'] = 1
d['b'] = 2
d['c'] = 3
print(d) # defaultdict(<class 'int'>, {'a': 1, 'b': 2, 'c': 3})
print(d['d']) # 0 # default value for missing keys

## 3. OrderedDict: # OrderedDict is a dictionary that remembers the order in which keys were first inserted.
from collections import OrderedDict
# This can be useful when using older versions of Python, as with Python 3.7 the order of keys is guaranteed.

ordered_dict = OrderedDict()
ordered_dict['a'] = 1
ordered_dict['b'] = 2
ordered_dict['c'] = 3
ordered_dict['d'] = 4
ordered_dict['e'] = 5
ordered_dict['f'] = 6

print(ordered_dict) # OrderedDict([('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5), ('f', 6)]) # order of keys is preserved

## 4. namedtuple: # namedtuple is a factory function for creating immutable data objects.
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y']) # This will create a class "Point" with two attributes x and y
pt = Point(1, 2)
print(pt) # Point(x=1, y=2)
print(pt.x) # 1
print(pt.y) # 2


## 5. deque: # deque is a double-ended queue.
# It provides fast insertion and removal of elements from both ends.
from collections import deque
d = deque()

## Available methods:
# 1. append() - adds an element to the right side
d.append(1)
d.append(2)
d.append(3)
d.append(4)
# 2. popleft() - removes an element from the left side
# 3. popright() - removes an element from the right side
print(d) # deque([1, 2, 3, 4])
print(d.popleft()) # 1
print(d) # deque([2, 3, 4])
print(d.pop()) # 4
print(d) # deque([2, 3])
print(d.popright()) # 3
# 3. clear() - removes all elements from the deque
d.clear() # removes all elements from the deque
print(d) # deque([])
# 4. count() - returns the number of elements with the specified value
d.append(1)
d.append(2)
d.append(3)
d.append(4)
print(d.count(1)) # 1
print(d.count(2)) # 2
print(d.count(3)) # 1
print(d.count(4)) # 1
# 5. extend() - adds elements from the other iterable to the right side
d.extend([1, 2, 3, 4])
print(d) # deque([1, 2, 3, 4])
# 6. extendleft() - adds elements from the other iterable to the left side
d.extendleft([1, 2, 3, 4])
print(d) # deque([1, 2, 3, 4, 1, 2, 3, 4])
# 7. index() - returns the index of the first element with the specified value
print(d.index(1)) # 0
print(d.index(2)) # 1
print(d.index(3)) # 2
# 8. insert() - inserts an element at the specified position
d.insert(0, 1)
d.insert(1, 2)
d.insert(2, 3)
d.insert(3, 4)
print(d) # deque([1, 2, 3, 4, 1, 2, 3, 4])
# 9. remove() - removes the first element with the specified value
d.remove(1)
print(d) # deque([2, 3, 4, 1, 2, 3, 4])
# 10. reverse() - reverses the elements in the deque
d.reverse()
print(d) # deque([4, 3, 2, 1, 4, 3, 2, 1])
# 11. rotate() - rotates the deque left by the specified number of steps
d.rotate(2)
print(d) # deque([3, 4, 1, 2, 3, 4, 1, 2])
# 12. sort() - sorts the deque in place
d.sort()
print(d) # deque([1, 1, 2, 2, 3, 3, 4, 4])
# 13. copy() - returns a shallow copy of the deque
d.append(1)
d.append(2)
d.append(3)
d.append(4)
d.append(5)
d.append(6)
d.append(7)







