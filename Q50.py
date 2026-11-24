"""Assignment 5 - Question 50
Create, write, read, close and delete a text file.
Run this file directly in VS Code.
"""

import os
filename = "temporary_demo.txt"
with open(filename, "w", encoding="utf-8") as file:
    file.write("This file will be read and then deleted.")
with open(filename, "r", encoding="utf-8") as file:
    print(file.read())
os.remove(filename)
print("File closed and deleted.")
