"""Assignment 5 - Question 3
Read first 10 characters.
Run this file directly in VS Code.
"""

with open("sample.txt", "r", encoding="utf-8") as file:
    print(file.read(10))
