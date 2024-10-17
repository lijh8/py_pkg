import os
from logging2.logging2 import *

if __name__ == "__main__":
    logfile = "app.log"
    logfile = os.path.join(os.path.dirname(os.path.realpath(__file__)), logfile)
    logging2(logfile)

    INFO("")

    a="abc"  # str is immutable
    b=list(a)  # list is mutable
    b[0]="A"
    a="".join(b)
    print(a)
