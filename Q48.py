"""Assignment 5 - Question 48
Demonstrate os.path.exists() and getsize().
Run this file directly in VS Code.
"""

import os
path = input("Enter path: ")
print("Exists:", os.path.exists(path))
if os.path.exists(path) and os.path.isfile(path):
    print("Size in bytes:", os.path.getsize(path))
