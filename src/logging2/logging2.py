# logging2.py
import sys
import logging
from logging.handlers import RotatingFileHandler

CRITICAL = logging.critical
ERROR = logging.error
WARNING = logging.warning
INFO = logging.info
DEBUG = logging.debug


class logging2:
    def __init__(self, filename):
        size = (1024 * 1024) * 100  # MB
        count = 10
        fmt = "%(asctime)s %(levelname)s %(filename)s:%(lineno)d: %(message)s"
        datefmt = "%Y-%m-%d %H:%M:%S %Z"
        formatter = logging.Formatter(fmt, datefmt=datefmt)
        level = logging.DEBUG

        file_handler = RotatingFileHandler(filename, maxBytes=size, backupCount=count)
        file_handler.setFormatter(formatter)
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(formatter)
        handlers = [file_handler, console_handler]
        logging.basicConfig(handlers=handlers, level=level)
