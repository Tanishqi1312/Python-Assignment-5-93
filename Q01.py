"""Assignment 5 - Question 1
Open existing text file in read mode and display contents.
Run this file directly in VS Code.
"""

with open("sample.txt", "r", encoding="utf-8") as file:
    print(file.read())
