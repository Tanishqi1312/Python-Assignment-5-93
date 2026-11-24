"""Assignment 5 - Question 13
Write multiple lines using writelines().
Run this file directly in VS Code.
"""

lines = ["First line\n", "Second line\n", "Third line\n"]
with open("lines.txt", "w", encoding="utf-8") as file:
    file.writelines(lines)
print("Lines written.")
