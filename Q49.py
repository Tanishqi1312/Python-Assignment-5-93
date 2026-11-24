"""Assignment 5 - Question 49
Rename text file and display its contents.
Run this file directly in VS Code.
"""

import os
old = input("Filename to rename: ")
new = input("New filename: ")
if os.path.isfile(old):
    os.rename(old, new)
    with open(new, "r", encoding="utf-8") as file: print(file.read())
else:
    print("File not found.")
