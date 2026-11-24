"""Assignment 5 - Question 7
Count lines in text file.
Run this file directly in VS Code.
"""

with open("sample.txt", "r", encoding="utf-8") as file:
    print("Lines =", len(file.readlines()))
