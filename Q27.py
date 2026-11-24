"""Assignment 5 - Question 27
Display file pointer using tell().
Run this file directly in VS Code.
"""

with open("sample.txt", "r", encoding="utf-8") as file:
    print("Current position:", file.tell())
    file.read(5)
    print("After reading 5 characters:", file.tell())
