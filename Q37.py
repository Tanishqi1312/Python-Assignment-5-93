"""Assignment 5 - Question 37
Display lines starting with a character.
Run this file directly in VS Code.
"""

ch = input("Starting character: ")
with open("sample.txt", "r", encoding="utf-8") as file:
    for line in file:
        if line.startswith(ch): print(line, end="")
