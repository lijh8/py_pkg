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

"""
$ cd ~/Documents/py_pkg/src
$
$ ls
__init__.py     foo             logging2        main
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
# the current directory is the top level package root directory ;
$ cd ~/Documents/py_pkg/src
$
$ pwd
/Users/ljh/Documents/py_pkg/src
$
$ python3 -m foo.main ;
$ PYTHONPATH=~/Documents/py_pkg/src python3 -m foo.main ;
$ PYTHONPATH=~/Documents/py_pkg/src python3 foo/main.py ;
$
"""
