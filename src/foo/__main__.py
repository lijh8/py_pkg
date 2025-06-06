import os

# change to the top level package root directory
# $ cd ~/Documents/py_pkg/src ;
# $ ls
# __init__.py     foo             logging2
# $
# $ python3 -m foo ;  # src/foo/__main__.py
# $ PYTHONPATH=~/Documents/py_pkg/src python3 foo/__main__.py ;

# module file in other directory
from logging2.logging2 import *

# module file in same directory
# import foo2  # $ PYTHONPATH=~/Documents/py_pkg/src python3 foo/__main__.py ;
from foo import foo2  # $ python3 -m foo ;

if __name__ == "__main__":
    logfile = "app.log"
    logfile = os.path.join(os.path.dirname(os.path.realpath(__file__)), logfile)
    logging2(logfile)

    CRITICAL("")
    ERROR("")
    WARNING("")
    INFO("")
    DEBUG("")

    foo2.foo()  # call function from module at same directory

"""
$ cd ~/Documents/py_pkg/src
$
$ ls
__init__.py     foo             logging2
$
$ find . -print | sed -e 's;[^/]*/;|____;g;s;____|; |;g'

.
|____ __init__.py
|____foo
| |____ __init__.py
| |____foo2.py
| |____app.log
| |____ __main__.py
|____logging2
| |____ __init__.py
| |____logging2.py
$
$
# the current directory is the top level package root directory ;
$ cd ~/Documents/py_pkg/src
$
$ python3 -m foo ;  # with __main__.py
$ python3 -m foo.__main__ ;
$ PYTHONPATH=~/Documents/py_pkg/src python3 -m foo.__main__ ;
$ PYTHONPATH=~/Documents/py_pkg/src python3 foo/__main__.py ;
$
"""
