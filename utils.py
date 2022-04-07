import os

def checkdir(name="image"):
    isdir = os.path.isdir(name)
    if not isdir:
        os.makedirs(name)