"""Assignment 5 - Question 12
Write five student names to a file.
Run this file directly in VS Code.
"""

names = ["Aman", "Riya", "Neha", "Rahul", "Priya"]
with open("students.txt", "w", encoding="utf-8") as file:
    for name in names: file.write(name + "\n")
print("Names written.")
