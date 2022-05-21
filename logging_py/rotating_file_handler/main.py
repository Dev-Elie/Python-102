# Having a large application with lots of logging, it is important to keep the log files small.
# a rotating file handler is a good way to do this.

from cgitb import handler
from logging.handlers import RotatingFileHandler
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# create a rotating file handler, and set the max size to 2 MB with a backup of 5 files
handler = RotatingFileHandler('app.log', maxBytes=2000, backupCount=5)
logger.addHandler(handler) # register the handler to the logger, same to blueprints in flask

# Test the logger with the following code:
for _ in range(10000):
    logger.info('This is an info message')
    logger.warning('This is a warning message')
    logger.error('This is an error message')
    logger.critical('This is a critical message')