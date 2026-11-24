"""Assignment 5 - Question 45
Create directory using os module.
Run this file directly in VS Code.
"""

import os
directory = input("New directory name: ")
os.makedirs(directory, exist_ok=True)
print("Directory created:", directory)
