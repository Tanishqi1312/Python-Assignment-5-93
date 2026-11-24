"""Assignment 5 - Question 47
Check whether path is file or directory.
Run this file directly in VS Code.
"""

import os
path = input("Enter path: ")
if os.path.isfile(path): print("It is a file.")
elif os.path.isdir(path): print("It is a directory.")
else: print("Path does not exist.")
