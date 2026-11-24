"""Assignment 5 - Question 25
Demonstrate write/read mode (w+).
Run this file directly in VS Code.
"""

file = open("wr_demo.txt", "w+", encoding="utf-8")
file.write("Write and read mode example.")
file.seek(0)
print(file.read())
file.close()
