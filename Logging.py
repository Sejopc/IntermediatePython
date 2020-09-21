import logging

# Only messages from level warning or above are printed; but we can change that using the basic configuration, as such:
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                datefmt='%m/%d/%Y %H:%M:%S')
# we can log to 5 different log levels. They indicate the severity of the events.
logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')

# To log in different modules rather than 'root', is best practice to create your own logger in your modules.
# Here, we have created another module called 'helper-logging'. # It's good practice to create your own logger in your modules with the getLogger function and __name__
import helper_logging
# As you notice, it logs in the console using the same basicConfig as above. We can change that
# by specifying our own module class to not propagate into the other modules where it is imported.
import helper_logging2 # It won't be printed to the console.

print("####")

### Log handlers ###
logger = logging.getLogger(__name__)

# create handler
stream_h = logging.StreamHandler()
file_h = logging.FileHandler('File.log')

# level and the format
stream_h.setLevel(logging.WARNING)
file_h.setLevel(logging.ERROR)

formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
stream_h.setFormatter(formatter)
file_h.setFormatter(formatter)

logger.addHandler(stream_h)
logger.addHandler(file_h)

logger.warning('This is a warning')
logger.error('This is an error')

print("####")
### Other configuration methods ###

import logging.config
logging.config.fileConfig('Logging.conf') # we can also use .dictConfig and pass a dictionary with the config.
logger = logging.getLogger('simpleExample')
logger.debug('This is a DEBUG message')

print("####")
### Capturing stacktraces/Traceback in your log ###
try:
    a = [1,2,3]
    val = a[4]
except IndexError as e:
    logging.error(e, exc_info=True)

import traceback
try:
    a = [1,2,3]
    val = a[4]
except:
    logging.error("The error is %s", traceback.format_exc())

print("####")
### Rotating file handler ###

from logging.handlers import RotatingFileHandler

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# roll over after 2KB, and keep up to 5 backup logs: app.log.1, app.log.2, app.log.3,...
handler = RotatingFileHandler('app.log', maxBytes=2000, backupCount=5)
logger.addHandler(handler)

for _ in range(10000):
    logger.info('Hello, world!') # after running this, will create the 6 files (app.log and the other 5 back up ones with the contents of Hello, world!)

### Time rotating file handler ###
# Instead of rotating based on size, we'll do it based on time
from logging.handlers import TimedRotatingFileHandler
import time
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# s(seconds),m(minutes),h(hours),d(day),midnight,w0(weekdays;monday),w1(tuesday)
handler2 = TimedRotatingFileHandler('timed_test.log', when='s', interval=5, backupCount=5)
logger.addHandler(handler2)

for _ in range(6):
    logger.info("Hello, world!") # will create 6 files as well (timed_test.log and the 5 backups, within 5 seconds each, and with the timestamp on the logname for the backup files.)
    time.sleep(5)


'''
NOTE

If we have a lot of different modules and use many many different things,
he recommends to use the JSON format for logging, and you can download this tool:
python-json-logger (Github: madzak/python-json-logger)
'''
