import os

def Dir():
    directory = os.path.dirname(os.path.abspath('__file__'))
    return directory