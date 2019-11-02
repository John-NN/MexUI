import os

directory = os.path.dirname(os.path.abspath('__file__'))
print (directory)


def Dir():
    directory = os.path.dirname(os.path.abspath('__file__'))
    #print (directory)    
    return directory
