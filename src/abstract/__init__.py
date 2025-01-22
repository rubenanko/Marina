import sys
import os

if sys.platform == "linux" or sys.platform == "unix":   from .linux import *
elif sys.platform =="win32":    from .windows import *

class Size:
    def __init__(self,width : int, height : int):
        self.lines = height
        self.columns = width

def getConsoleSize():
    return os.get_terminal_size()