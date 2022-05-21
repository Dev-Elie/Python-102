import logging

# To override the default logging level, use the following code:
# log to file:
# logging.basicConfig(filename='example.log', level=logging.DEBUG, format='%(asctime)s:%(name)s:%(levelname)s:%(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

# log to termnal
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
import helper