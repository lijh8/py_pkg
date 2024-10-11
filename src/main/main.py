import os
from logging2.logging2 import *

logfile = "app.log"
logfile = os.path.join(os.path.dirname(os.path.abspath(__file__)), logfile)
logging2(logfile)

CRITICAL("")
ERROR("")
WARNING("")
INFO("")
DEBUG("")
