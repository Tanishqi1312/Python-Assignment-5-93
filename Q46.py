"""Assignment 5 - Question 46
Display filenames in a directory.
Run this file directly in VS Code.
"""

import os
directory = input("Directory path: ")
if os.path.isdir(directory):
    for filename in os.listdir(directory): print(filename)
else:
    print("Directory not found.")
