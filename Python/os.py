import os
from datetime import datetime

print(os.getcwd())

os.chdir('D:/Coding/')                      # chdir - change directory

print(os.getcwd())

print(os.listdir())                         # listdir - lists directory. if brackets are empty, it lists item in current directory.
print(os.listdir('D:/Coding/robotics'))

# Creating a directory
print("\nCreating")
os.mkdir('OS-Demo-2')
# os.makedirs('OS-Demo-2/Sub-Dir-1')        # This is similar to mkdir but it also creates a directory and subdirectory if a directory does not exist already
print(os.listdir())

# Renaming a directory
print("\nRenaming")
os.rename('OS-Demo-2', 'OS-Demo-1')
print(os.listdir())

# Removing directory
print("\nDeleting")
os.rmdir('OS-Demo-1')
# os.removedirs('OS-Demo-1')                # Same as mkdir and makedirs
print(os.listdir())

# Checking info about a file
print(os.stat('robotics'))
print(os.stat('robotics').st_size)
mod_time = os.stat('robotics').st_mtime         # Last modification time
print(datetime.fromtimestamp(mod_time))

for dirpath, dirnames, filename in os.walk('D:/Coding/robotics'):
    print('Current Path:', dirpath)
    print('Directories: ', dirnames)
    print('Files: ', filename)
    print()

# print(os.environ)                             # Prints all the environments
print(os.environ.get('USERPROFILE'))            # Gets the path of a particular environment

file_path = os.path.join(os.environ.get('USERPROFILE'), 'test.txt')     # join path without worrying about /. For example, adding as strings will give C:\Users\Amantest.txt. This function removes the stress
print(file_path)

print(os.path.basename('/tmp/test.txt'))        # Gives the basename
print(os.path.dirname('/tmp/test.txt'))         # Gives the directory name
print(os.path.split('/tmp/test.txt'))           # Gives both
print(os.path.exists('/tmp/test.txt'))          # Checks if a path exists

print(os.path.isdir('/tmp/fgdgd'))              # Checks if something is a directory
print(os.path.isfile('/tmp/fgdgd'))             # Checks if something is a file

print(os.path.splitext('/tmp/test.txt'))        # Splits the root and path, and the extension

print(dir(os.path))