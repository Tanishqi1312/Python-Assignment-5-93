"""Assignment 5 - Question 23
Demonstrate append mode (a).
Run this file directly in VS Code.
"""

file = open("write_demo.txt", "a", encoding="utf-8")
file.write("Added using append mode.\n")
file.close()
print("Content appended.")
