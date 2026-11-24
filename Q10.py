"""Assignment 5 - Question 10
Display file lines in reverse order.
Run this file directly in VS Code.
"""

with open("sample.txt", "r", encoding="utf-8") as file:
    for line in reversed(file.readlines()):
        print(line, end="")
