# Lambda expression : is a small anonymous function that can 
# take any number of arguments but has only one expression.

# Lambda functions are commonly used as callback functions,
# as an alternative to defining a full function with its own
# name.

add = lambda x, y: x + y
print(add(2, 3)) # 5

mult = lambda x, y: x * y
print(mult(2, 3)) # 6

points2D = [(1, -3), (3, 24), (5, 2), (7, 1), (9, -2)]
points3D = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 11, 12)]

# Sort points2D by y coordinate with the help of lambda
points2D.sort(key=lambda x: x[1])
print(points2D) # [(1, -3), (9, -2), (7, 1), (5, 2), (3, 24)] # sorted by y coordinate

# Sort points3D by z coordinate with the help of lambda
points3D.sort(key=lambda x: x[2])
print(points3D) # [(1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 11, 12)] # sorted by z coordinate

# Sort points2D by sum of x and y coordinates with the help of lambda
points2D.sort(key=lambda x: x[0] + x[1])
print(points2D) # [(1, -3), (9, -2), (5, 2), (7, 1), (3, 24)] # sorted by sum of x and y coordinates

# Using lambda with map()
# map() is a higher-order built-in function that takes a function and
# iterable as inputs, and returns an iterator that applies the function
# to each element of the iterable.

a = [1, 2, 3, 4, 5]
b = map(lambda x: x * 2, a)
print(list(b)) # [2, 4, 6, 8, 10]

# Using lambda with filter()
# filter() is a higher-order built-in function that takes a function and iterable as inputs, and returns an iterator with the elements from the
# iterable for which the function returns True.

a = [1, 2, 3, 4, 5]
b = filter(lambda x: x % 2 == 0, a) # filter even numbers
print(list(b)) # [2, 4]

# Using lambda with reduce()
# reduce() is a higher-order built-in function that takes a function and iterable as inputs, and returns a single value.
from functools import reduce
a = [1, 2, 3, 4, 5]
b = reduce(lambda x, y: x + y, a) # sum of all elements
print(b) # 15



