# Errors and Exceptions

# Diffence errors and exceptions
# Errors are when something goes wrong
# Exceptions are when something goes wrong and you need to handle it


# Types of errors:
# 1. IndentationError - occurs when there is no indentation in Python code.
# 2. NameError - occurs when a variable is not defined.
# 3. TypeError - occurs when a function or operation is applied to the wrong type of argument.
# 4. ValueError - occurs when a function or operation is applied to the wrong value.
# 5. SyntaxError - occurs when there is invalid syntax in Python code.

# Types of exceptions:
# 1. IndexError - occurs when an index is out of range.
# 2. KeyError - occurs when a key is not found in a dictionary.
# 3. AttributeError - occurs when an attribute is not found.
# 4. ZeroDivisionError - occurs when a division by zero occurs.
# 5. FileNotFoundError - occurs when a file is not found.
# 6. IOError - occurs when an I/O operation (such as a read or write) fails.
# 7. OSError - occurs when an operating system (OS) error occurs.
# 8. RuntimeError - occurs when a runtime error occurs.
# 9. RecursionError - occurs when a recursive function call reaches the maximum recursion depth.
# 10. EOFError - occurs when the end of a file is reached unexpectedly.
# 11. BrokenPipeError - occurs when a pipe, socket, or file is broken.
# 12. EnvironmentError - occurs when an error occurs in an environment.
# 13. Warning - occurs when a warning is issued.
# 14. DeprecationWarning - occurs when a deprecated feature is used.
# 15. FutureWarning - occurs when a feature is about to be deprecated.
# 16. ImportWarning - occurs when there is a problem with an imported module.
# 17. UnicodeWarning - occurs when a Unicode-related error occurs.
# 18. UnicodeError - occurs when a Unicode-related error occurs.
# 19. BytesWarning - occurs when a bytes-related error occurs.
# 20. BytesWarning - occurs when a bytes-related error occurs.
# 21. UserWarning - occurs when a user-defined warning occurs.
# 22. ReferenceError - occurs when an invalid reference is made.
# 23. SystemError - occurs when a system error occurs.
# 24. AssertionError - occurs when an assertion fails.


# Raising Exceptions
# raise ExceptionName
# raise ExceptionName(arguments)
# raise ExceptionName from ExceptionObject
# raise ExceptionName(arguments) from ExceptionObject

# Example 1: Using raise
x = -5
if x < 0:
    raise ValueError('Negative value')

# Example 2: using assert
x = -5
assert x >= 0, 'Negative value'

# Example 3: using try/except
try:
    x = 5 / 0
except Exception as e:
    print(e)

# Example 3.1: using try/except with multiple exceptions
try:
    x = 5 / 0
except (ZeroDivisionError, TypeError):
    print('Error')

## or

try:
    x = 5 / 0
    b = 'a' + 5
except ZeroDivisionError as e:
    print("Error:", e)
except TypeError as e:
    print("Error:", e)

# Example 4: using try/except/else
try:
    x = 5 / 0
except Exception as e:
    print(e)
else:
    print('No exceptions')

# Example 5: using try/except/finally
try:
    x = 5 / 0
except Exception as e:
    print(e)
finally:
    print('Executing finally clause')


# Example 6: using try/except/else/finally
try:
    x = 5 / 0
except Exception as e:
    print(e)
else:
    print('No exceptions')
finally:
    print('Executing finally clause')

# Example 7: using try/finally
try:
    x = 5 / 0
except Exception as e:
    print(e)
finally:
    print('Executing finally clause')


## Defining custom exceptions
# Example 1: simple custom exception
class ValueTooSmallError(Exception):
    pass

def check_number(number):
    if number < 5:
        raise ValueTooSmallError('Value is too small')

check_number(4) # Raises ValueTooSmallError exception as : __main__.ValueTooSmallError: Value is too small

# Example 2: custom exception with arguments
class ValueTooSmallError(Exception):
    def __init__(self, message, value):
        self.value = value
        self.message = message

try:
    check_number(4)
except ValueTooSmallError as e:
    print(e.message, e.value) # Prints: Value is too small 4


# Using custom exceptions with try/except
try:
    check_number(4)
except ValueTooSmallError as e:
    print(e) # Prints ValueTooSmallError: Value is too small