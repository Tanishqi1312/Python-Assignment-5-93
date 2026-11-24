"""Assignment 5 - Question 9
Display lines containing a particular word.
Run this file directly in VS Code.
"""

word = input("Word to search: ").casefold()
with open("sample.txt", "r", encoding="utf-8") as file:
    for line_no, line in enumerate(file, 1):
        if word in line.casefold():
            print(f"Line {line_no}: {line}", end="")
