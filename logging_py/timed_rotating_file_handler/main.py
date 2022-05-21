# Rotating time handler : https://docs.python.org/3/library/logging.handlers.html#logging.handlers.TimedRotatingFileHandler
# Useful when you want to keep a log file for a long time.

from cgitb import handler
import logging
import time
from logging.handlers import TimedRotatingFileHandler

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# create a rotating file handler that rolls over after every second with interval of 5 seconds

# s : seconds
# m : minutes
# h : hours
# d : days
# w : weeks
# midnight : roll over at midnight
# w0 : roll over on the first of the week
# M : roll over at the beginning of the month
# H : roll over at the beginning of the hour

handler = TimedRotatingFileHandler('timed_app.log', when='s', interval=5, backupCount=5)
logger.addHandler(handler)

# test the logger with the following code:
for _ in range(6):
    logger.info('This is an info message')
    time.sleep(5)
