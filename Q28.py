"""Assignment 5 - Question 28
Change file pointer using seek().
Run this file directly in VS Code.
"""

with open("sample.txt", "r", encoding="utf-8") as file:
    file.seek(5)
    print("Position after seek:", file.tell())
    print("Remaining content:", file.read())
