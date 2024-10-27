# Write a python program to print the contents of a directory using the os module.
# Search online for the function which does that

import os

# Specify the directory path (or use '.' for the current directory)
directory_path = '/'

# List the contents of the directory
contents = os.listdir(directory_path)

# Print the contents
for item in contents:
    print(item)
