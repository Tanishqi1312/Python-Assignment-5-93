"""Assignment 5 - Question 29
Read file from specified pointer position.
Run this file directly in VS Code.
"""

with open("sample.txt", "r", encoding="utf-8") as file:
    position = int(input("Starting character position: "))
    file.seek(position)
    print(file.read())
