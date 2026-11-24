"""Assignment 5 - Question 26
Demonstrate append/read mode (a+).
Run this file directly in VS Code.
"""

file = open("ar_demo.txt", "a+", encoding="utf-8")
file.write("Appended using a+ mode.\n")
file.seek(0)
print(file.read())
file.close()
