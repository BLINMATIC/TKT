import os
import sys

def cd(path):
    os.chdir(path)
    return ""

def ls():
    return str(os.listdir())

def at():
    return os.getcwd()

def md(path):
    os.mkdir(path)
    return ""

def rm(path):
    os.rmdir(path)
    return ""

def sz(path):
    return str(os.path.getsize(path))