"""Assignment 5 - Question 30
Demonstrate close() and closed status.
Run this file directly in VS Code.
"""

file = open("sample.txt", "r", encoding="utf-8")
file.close()
print("Is file closed?", file.closed)
