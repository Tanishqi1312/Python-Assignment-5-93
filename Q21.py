"""Assignment 5 - Question 21
Demonstrate read mode (r).
Run this file directly in VS Code.
"""

file = open("sample.txt", "r", encoding="utf-8")
print(file.read())
file.close()
