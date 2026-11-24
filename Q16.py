"""Assignment 5 - Question 16
Demonstrate write mode versus append mode.
Run this file directly in VS Code.
"""

with open("mode_demo.txt", "w", encoding="utf-8") as file:
    file.write("This replaces old content.\n")
with open("mode_demo.txt", "a", encoding="utf-8") as file:
    file.write("This is appended content.\n")
with open("mode_demo.txt", "r", encoding="utf-8") as file:
    print(file.read())
