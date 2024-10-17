import os
from logging2.logging2 import *
from main import main2

if __name__ == "__main__":
    logfile = "app.log"
    logfile = os.path.join(os.path.dirname(os.path.realpath(__file__)), logfile)
    logging2(logfile)

    INFO("")
    main2.main2()
