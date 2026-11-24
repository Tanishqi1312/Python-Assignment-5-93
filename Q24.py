"""Assignment 5 - Question 24
Demonstrate read/write mode (r+).
Run this file directly in VS Code.
"""

file = open("rw_demo.txt", "w+", encoding="utf-8")
file.write("Read and write mode example.")
file.seek(0)
print(file.read())
file.close()
