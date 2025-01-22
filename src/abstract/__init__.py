import sys
import os

if sys.platform == "linux" or sys.platform == "unix":   from .linux import *
elif sys.platform =="win32":    from .windows import *

def getConsoleSize():
    return os.get_terminal_size()