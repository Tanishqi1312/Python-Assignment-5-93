"""Assignment 5 - Question 5
Read all lines using readlines().
Run this file directly in VS Code.
"""

with open("sample.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()
print("".join(lines))
