'''Global Logging configuration for the project'''

import logging
from datetime import datetime

filename = 'log/' + str(datetime.now()) +".log"
logging.basicConfig(filename=filename, filemode='a',format='%(asctime)s - %(message)s')
log = logging
