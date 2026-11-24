"""Assignment 5 - Question 6
Count characters in text file.
Run this file directly in VS Code.
"""

with open("sample.txt", "r", encoding="utf-8") as file:
    content = file.read()
print("Characters =", len(content))
