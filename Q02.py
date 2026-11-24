"""Assignment 5 - Question 2
Read entire file using read().
Run this file directly in VS Code.
"""

with open("sample.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print(content)
