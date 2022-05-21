import logging

try:
    a = [1, 2, 3]
    a = a[4]
except IndexError as e:
    logging.error(e) # ERROR:root:list index out of range
    logging.error(e, exc_info=True) # If you want to see the traceback, use exc_info=True
    logging.error(e, exc_info=True, stack_info=True) # Addition: stack_info=True to see the stack trace
