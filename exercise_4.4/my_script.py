import sys
import os
import logging
os.makedirs("my_file_log", exist_ok=True)
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s', filename="my_file_log/logfile.log")

logging.debug("Ok")



