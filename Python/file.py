# Opening a file

f = open('test.txt', 'r')               # 'r' - Opening the file for reading. 'w' - writing. 'a' - append. 'x' - create. 'r+' - read and write to a file

print(f.name)
print(f.mode)
f.close()

# Opening a file using context manager (Better way). The above method needs the file to be closed if it is opened. 
# If it is not closed, leaks can happen that can cause to run over the maximum allowed file descriptors on the system. 
# The applications can throw an error.

with open('test.txt', 'r') as f:
# This will allow us to work with the file within this block and after we exit the block, the file will be automatically closed.
# This will also close the file if there are any exceptions that are thrown or anything like that
    pass

# The f variable declared in the context manager method is accessible outside the scope of with statement as well.
# But the file is closed so we can not read or write or do anything like that from it.
print(f.closed)

with open('test.txt', 'r') as f:
    # f_contents = f.read()
    # print(f_contents)
    # f_contents = f.readlines()
    # print(f_contents)
    f_contents = f.readline()
    print(f_contents, end='')
    f_contents = f.readline()
    print(f_contents)

with open('test.txt', 'r') as f:
    for line in f:
        print(line, end='')                 # This helps in printing one line at a time and prevents memory issue

with open('test.txt', 'r') as f:
    f_contents = f.read(100)                # This will read 100 characters from the file
    print(f_contents)

    f_contents = f.read(100)                # This will read 100 more characters from the file
    print(f_contents)

    f_contents = f.read(100)                # This will read 100 more characters from the file. Since everything has been printed, it will return an empty string
    print(f_contents)

# Using the above method to read large files by iterating over small chunks
with open('test.txt', 'r') as f:
    size_to_read = 10
    f_contents = f.read(size_to_read)
    print(f_contents, end='*')

    f.seek(0)                               # seeks the cursor to the specified index

    f_contents = f.read(size_to_read)
    print(f_contents, end='*')

    print(f.tell())
    
    while len(f_contents) > 0:
        print(f_contents, end='*')
        f_contents = f.read(size_to_read)


with open('test2.txt', 'w') as f:
    f.write('Test')
    f.seek(0)                               # seeks the cursor to the index mentioned
    f.write('R')

# Writing from one file to another
with open('test.txt', 'r') as rf:
    with open('test_copy.txt', 'w') as wf:
        for line in rf:
            wf.write(line)

# Copying an image
with open('cat.jpeg', 'rb') as rf:              # rb - read binary
    with open('cat_copy.jpeg', 'wb') as wf:     # wb - write binary
        for img in rf:
            wf.write(img)

# Copying an image using a chunk size
with open('cat.jpeg', 'rb') as rf:
    with open('cat_copy1.jpeg', 'wb') as wf:
        chunk_size = 8192
        rf_chunk = rf.read(chunk_size)
        while len(rf_chunk) > 0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)