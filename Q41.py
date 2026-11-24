"""Assignment 5 - Question 41
Check whether a file exists.
Run this file directly in VS Code.
"""

import os
path = input("Enter file path: ")
print("File exists:", os.path.isfile(path))
