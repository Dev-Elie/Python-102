import logging

# Create a custom logger with the name of the module
logger = logging.getLogger(__name__) # __name__ is the name of the current module
logger.propagate = False # Do not propagate to parent/ancestor handlers
logger.info("This is a custom logger")


# Creating the above logger here, will create a propagation of the logger to all the modules that import this module.