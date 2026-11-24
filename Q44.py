"""Assignment 5 - Question 44
Delete file using os module.
Run this file directly in VS Code.
"""

import os
path = input("Filename to delete: ")
if os.path.isfile(path):
    os.remove(path)
    print("File deleted.")
else:
    print("File not found.")
