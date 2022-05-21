import logging

# To override the default logging level, use the following code:
logging.basicConfig(filename='example.log', level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

# create logger
logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')

# By default, Only log messages with level of WARNING or higher, to change this, we can use the logging.basicConfig() function
# right after the import statement.

# Loggs to a file named example.log