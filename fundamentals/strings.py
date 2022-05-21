# A string is a sequence of characters that is immutable.

#### X-tics of a string

# 1. Can be created with single or double quotes
# 2. Can be concatenated with +
# 3. Can be indexed with []
# 4. Can be sliced with [start:stop:step]
# 5. Can be iterated with for loops

#Creating a string
# 1. Single quotes
my_string = 'Hello World'
print(my_string) # prints Hello World
# 2. Double quotes
my_string = "Hello World"
print(my_string) # prints Hello World
# 3. Triple quotes
my_string = """Hello World"""
print(my_string) # prints Hello World

# Accessing a substring of a string
# 1. Indexing
my_string = 'Hello World'
print(my_string[0]) # prints H
print(my_string[-1]) # prints d
print(my_string[0:5]) # prints Hello
print(my_string[:5]) # prints Hello
print(my_string[5:]) # prints World
print(my_string[::2]) # prints HloWrd
print(my_string[::-1]) # prints dlroW olleH

# Concatenating strings
# 1. +
my_string = 'Hello' + ' World'
print(my_string) # prints Hello World
# 2. +=
my_string = 'Hello'
my_string += ' World'
print(my_string) # prints Hello World
# 3. *
my_string = 'Hello' * 3
print(my_string) # prints HelloHelloHello
# 4. *=
my_string = 'Hello'
my_string *= 3
print(my_string) # prints HelloHelloHello

# Slicing strings
# 1. Slicing
my_string = 'Hello World'
print(my_string[0:5]) # prints Hello
print(my_string[::2]) # prints HloWrd
print(my_string[::-1]) # prints dlroW olleH
# 2. Slicing with step
my_string = 'Hello World'
print(my_string[0:5:2]) # prints Hlo
print(my_string[::-2]) # prints dloW
# 3. Slicing with negative step
my_string = 'Hello World'
print(my_string[0:5:-1]) # prints HloW
print(my_string[::-2]) # prints dloW
# 4. Slicing with negative start
my_string = 'Hello World'
print(my_string[-1::-1]) # prints dlroW olleH
# 5. Slicing with negative stop
my_string = 'Hello World'
print(my_string[-1::-1]) # prints dlroW olleH
# 6. Slicing with negative start and stop
my_string = 'Hello World'
print(my_string[-1::-1]) # prints dlroW olleH
# 7. Slicing with negative start and step
my_string = 'Hello World'
print(my_string[-1::-2]) # prints dloW
# 8. Slicing with negative stop and step
my_string = 'Hello World'
print(my_string[-1::-2]) # prints dloW
# 9. Slicing with negative start, stop and step
my_string = 'Hello World'
print(my_string[-1::-2]) # prints dloW

# Iterating over a string
# 1. for loop
my_string = 'Hello World'
for char in my_string:
    print(char) # prints H e l l o w o r l d
# 2. for loop with index
my_string = 'Hello World'
for index, char in enumerate(my_string):
    print(index, char) # prints 0 H, 1 e, 2 l, 3 l, 4 o, 5 w, 6 o, 7 r, 8 l, 9 d

# String methods
# 1. len()
my_string = 'Hello World'
print(len(my_string)) # prints 11
# 2. lower()
my_string = 'Hello World'
print(my_string.lower()) # prints hello world
# 3. upper()
my_string = 'Hello World'
print(my_string.upper()) # prints HELLO WORLD
# 4. replace()
my_string = 'Hello World'
print(my_string.replace('World', 'Universe')) # prints Hello Universe
# 5. split()
my_string = 'Hello World'
print(my_string.split()) # prints ['Hello', 'World']
# 6. split() with a delimiter
my_string = 'Hello World'
print(my_string.split(' ')) # prints ['Hello', 'World']
# 7. split() with a delimiter and maxsplit
my_string = 'Hello World'
print(my_string.split(' ', 1)) # prints ['Hello', 'World']
# 8. startswith()
my_string = 'Hello World'
print(my_string.startswith('Hello')) # prints True
# 9. endswith()
my_string = 'Hello World'
print(my_string.endswith('World')) # prints True
# 10. find()
my_string = 'Hello World'
print(my_string.find('World')) # prints 6
# 11. find() with a start index
my_string = 'Hello World'
print(my_string.find('World', 6)) # prints 6
# 12. find() with a start index and a stop index
my_string = 'Hello World'
print(my_string.find('World', 6, 11)) # prints 6
# 13. find() with a start index, a stop index and a step
my_string = 'Hello World'
print(my_string.find('World', 6, 11, 1)) # prints 6
# 14. count()
my_string = 'Hello World'
print(my_string.count('l')) # prints 3
# 15. count() with a start index
my_string = 'Hello World'
print(my_string.count('l', 6)) # prints 2
# 16. count() with a start index and a stop index
my_string = 'Hello World'
print(my_string.count('l', 6, 11)) # prints 2
# 17. count() with a start index, a stop index and a step
my_string = 'Hello World'
print(my_string.count('l', 6, 11, 1)) # prints 2


# Joining strings
# 1. join()
my_string = 'Hello'
my_string = my_string.join(' World')
print(my_string) # prints Hello World
# 2. join() with a list
my_string = 'Hello'
my_string = my_string.join([' World', ' Universe'])
print(my_string) # prints Hello World Universe
# 3. join() with a tuple
my_string = 'Hello'
my_string = my_string.join((' World', ' Universe'))
print(my_string) # prints Hello World Universe
# 4. join() with a range
my_string = 'Hello'
my_string = my_string.join(range(10))
print(my_string) # prints Hello0123456789
# 5. join() with a range and a step
my_string = 'Hello'
my_string = my_string.join(range(10, 20, 2))
print(my_string) # prints Hello1416181920
# 6. join() with a range and a step and a start index
my_string = 'Hello'
my_string = my_string.join(range(10, 20, 2), 1)
print(my_string) # prints Hello1416181920
# 7. join() with a range and a step and a start index and a stop index
my_string = 'Hello'
my_string = my_string.join(range(10, 20, 2), 1, 3)
print(my_string) # prints Hello1416181920
# 8. join() with a range and a step and a start index, a stop index and a step
my_string = 'Hello'
my_string = my_string.join(range(10, 20, 2), 1, 3, 1)
print(my_string) # prints Hello1416181920
# 9. join() with a range and a step and a start index, a stop index and a step and a separator
my_string = 'Hello'
my_string = my_string.join(range(10, 20, 2), 1, 3, 1, '-')
print(my_string) # prints Hello-14-16-18-20
# 10. join() with a range and a step and a start index, a stop index and a step and a 
# separator and a prefix
my_string = 'Hello'
my_string = my_string.join(range(10, 20, 2), 1, 3, 1, '-', 'prefix')
print(my_string) # prints prefix-14-16-18-20
# 11. join() with a range and a step and a start index, a stop index and a step and a 
# separator and a prefix and a suffix
my_string = 'Hello'
my_string = my_string.join(range(10, 20, 2), 1, 3, 1, '-', 'prefix', 'suffix')
print(my_string) # prints prefix-14-16-18-20suffix
# 12. join() with a range and a step and a start index, a stop index and a step and a \
# separator and a prefix and a suffix and a separator
my_string = 'Hello'
my_string = my_string.join(range(10, 20, 2), 1, 3, 1, '-', 'prefix', 'suffix', 'separator')
print(my_string) # prints prefix-14-16-18-20suffixseparator
# 13. join() with a range and a step and a start index, a stop index and 
# a step and a separator and a prefix and a suffix and a separator and a prefix
my_string = 'Hello'
my_string = my_string.join(range(10, 20, 2), 1, 3, 1, '-', 'prefix', 'suffix', 'separator', 'prefix2')
print(my_string) # prints prefix-14-16-18-20suffixseparatorprefix2

# String formatting
# 1. format()
my_string = 'Hello {0}'
print(my_string.format('World')) # prints Hello World
# 2. format() with a list
my_string = 'Hello {0}'
print(my_string.format(['World', ' Universe'])) # prints Hello ['World', ' Universe']
# 3. format() with a tuple
my_string = 'Hello {0}'
print(my_string.format(('World', ' Universe'))) # prints Hello ('World', ' Universe')
# 4. format() with a range
my_string = 'Hello {0}'
print(my_string.format(range(10))) # prints Hello range(0, 10)
# 5. format() with a range and a step
my_string = 'Hello {0}'

# fstring
my_string = f'Hello {"World"}'
print(my_string) # prints Hello World
# 6. fstring with a list
my_string = f'Hello {"World", " Universe"}'
# fstring.format_map()
my_string = 'Hello {name}'
print(my_string.format_map({'name': 'World'})) # prints Hello World

