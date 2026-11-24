"""Assignment 5 - Question 11
Create text file and write welcome message.
Run this file directly in VS Code.
"""

with open("welcome.txt", "w", encoding="utf-8") as file:
    file.write("Welcome to Python file handling!")
print("welcome.txt created.")
