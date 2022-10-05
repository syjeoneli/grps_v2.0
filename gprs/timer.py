# Define timer functions
import atexit
from time import time, strftime, localtime
from datetime import timedelta

def secondsToStr(elapsed=None):
    if elapsed is None:
        return strftime("%Y-%m-%d %H:%M:%S", localtime())
    else:
        return str(timedelta(seconds=elapsed))

def log(s, elapsed=None, start=None):
    line = "="*80
    print(line)
    print(secondsToStr(), '-', s)
    if elapsed:
        print("Elapsed time:", elapsed)
    print(line)

def endlog(start):
    end = time()
    elapsed = end-start
    log("Ending Analysis", secondsToStr(elapsed))

def exitlog(start):
    exit = time()
    elapsed = exit-start
    print("\n")
    log("Exiting Program", secondsToStr(elapsed))
