import os
import time
import logging
from logging.handlers import RotatingFileHandler
import datetime
fileMaxByte = 1024
#logging.basicConfig(filename="../log/temp.log", level=logging.INFO)
logger = logging.getLogger(__name__)
fileHandler = RotatingFileHandler(filename="../log/temp.log", maxBytes=1024, backupCount=2)
logger.addHandler(fileHandler)
logger.setLevel(logging.INFO)
while 1:
    with open("/sys/class/thermal/thermal_zone0/temp", "r") as f:
        thermal = f.readline().strip()

    if int(thermal) < 60000:
        logger.info(str(datetime.datetime.now()) + ' ' + thermal)
    else:
        os.system("sudo shutdown now")
    time.sleep(0.1)