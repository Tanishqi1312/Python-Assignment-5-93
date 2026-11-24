"""Assignment 5 - Question 22
Demonstrate write mode (w).
Run this file directly in VS Code.
"""

file = open("write_demo.txt", "w", encoding="utf-8")
file.write("Written using write mode.\n")
file.close()
print("File written.")
