import logging
logger = logging.getLogger(__name__) # this will create a logger with the name of the module (helper_logging)
logger.propagate = False
logger.info('Hello from helper_logging')
