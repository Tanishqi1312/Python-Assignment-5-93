"""Assignment 5 - Question 43
Rename file using os module.
Run this file directly in VS Code.
"""

import os
old = input("Existing filename: ")
new = input("New filename: ")
if os.path.isfile(old):
    os.rename(old, new)
    print("Renamed successfully.")
else:
    print("File not found.")
