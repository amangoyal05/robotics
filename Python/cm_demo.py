# We will take a look at handling different tasks with Context Managers to better manage our resources.

from contextlib import contextmanager
import os

# File opening
with open('sample.txt', 'r') as f:
    print(f.read())

# Creating context manager for file opening and automatically closing the file

# Using Class
class Open_File():
    
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_val, traceback):
        self.file.close()

with Open_File('sample.txt', 'r') as f:
    print(f.read())

print(f.closed)

# Using Function
@contextmanager
def open_file(file, mode):
    try:
        f = open(file, mode)
        yield f
    finally:
        f.close()

with open_file('sample.txt', 'r') as f:
    print(f.read())

print(f.closed)

@contextmanager
def change_dir(destination):
    try:
        cwd = os.getcwd()
        os.chdir(destination)
        yield
    finally:
        os.chdir(cwd)

with change_dir('D:/Coding/robotics/img'):
    print(os.listdir())
