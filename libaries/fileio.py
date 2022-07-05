import os
import sys

def new(path):
    open(path, "w")
    return ""

def append(path, data):
    open(path, "a").write(data)
    return "written " + sys.getsizeof(data) + " bytes"

def wipe(path):
    open(path, "w").write()
    return ""

def read(path):
    return open(path, "r").read()

def sz(path):
    return str(sys.getsizeof(open(path, "r").read()))