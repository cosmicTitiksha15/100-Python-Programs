# Basic concepts of File handling

# ----------------------------------File I/O in Python------------------------------------------------
# Python can be used to perform operations on a file.(read / write)
# Types of all files:
# 1. Text files: .txt, .log, .dcx etc
# 2. Binary files: .mov, .mp4, .jpeg, .png etc

# Opening a file
# We have to open a file before reading or writing
# f = open("file_name", "mode")
# data = f..read()
# f.close()

# Opening a file
f = open("demo.txt", "r")
# .read() method returns all data of a file in the form of a string.
data = f.read()
# .read(no_of_characters) can help read number of characters from the beginning.
print(data)
print(type(data))
f.close()

# **************** Modes in file handling ********************
# 'r' -> open for reading (default)
# 'w' -> open for writing, truncating the file first
# 'x' -> create a new file and open it for writing
# 'a' -> open for writing, appending to the end of the file, if it exists.
# 'b' -> binary mode
# 't' -> text mode (default)
# '+' -> open a disk file for updating(reading or writing) (default)

# data = f.read() -> reads entire file
# data = f.readline() -> reads one line at a time.
# data = f.readlines() -> returns the list of all comma seperated lines of a file

# ******************** Writing to a file *****************
f = open("demo.txt", "w")
f.write("This is a new file.") # Overwrites the entire file
f.close()

f = open("demo.txt", "a")
f.write(" adding at the end of the file.") # adds at the end of the file
f.close()
# If we open a file in "a" or "w" mode and it does not exist, python automatically create it for us.

# f = open("sample.txt", "w")
# f.close()


# ******************* Using 'with' syntax ********************

with open("sample.txt", "r") as f:
    data = f.read()
    print(data)
    # Using 'with' will automatically close the file.

# ******************* Deleting a file ***********************

# using the os module, Module (like a code library) is a file written by another programmer that generally has a function we can use

# import os
# os.remove(file_name)

# Some modules like 'os' comes preinstalled in python, but modules like 'tensorflow' need to be installed.