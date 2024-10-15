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


"""

# the current directory is the top level package root directory ;
$ cd ~/Documents/py_pkg/src
$
$ ls
__init__.py     foo             logging2
$
$ find . -print | sed -e 's;[^/]*/;|____;g;s;____|; |;g'

.
|______init__.py
|____foo
| |______init__.py
| |____main.py
| |____app.log
|____logging2
| |______init__.py
| |____logging2.py
$

$ cat foo/main.py
import os
from logging2.logging2 import *

logfile = "app.log"
logfile = os.path.join(os.path.dirname(os.path.realpath(__file__)), logfile)
logging2(logfile)

CRITICAL("")
ERROR("")
WARNING("")
INFO("")
DEBUG("")
$

$ pwd
/Users/ljh/Documents/py_pkg/src
$
$ python3 -m foo.main ;  # execute as module, at package root directory
$ PYTHONPATH=~/Documents/py_pkg/src python3 -m foo.main ;  # with PYTHONPATH, at any directory
$ PYTHONPATH=~/Documents/py_pkg/src python3 foo/main.py ;  # execute the script file, at any directory
$
"""
