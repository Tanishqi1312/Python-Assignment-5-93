"""Assignment 5 - Question 42
Display filename and available file information.
Run this file directly in VS Code.
"""

import os
path = input("Enter file path: ")
if os.path.exists(path):
    print("Name:", os.path.basename(path))
    print("Absolute path:", os.path.abspath(path))
    print("Size (bytes):", os.path.getsize(path))
else:
    print("Path does not exist.")
