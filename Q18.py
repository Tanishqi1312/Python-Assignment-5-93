"""Assignment 5 - Question 18
Write student details to a file.
Run this file directly in VS Code.
"""

name = input("Name: ")
roll = input("Roll number: ")
marks = input("Marks: ")
with open("student_details.txt", "w", encoding="utf-8") as file:
    file.write(f"Name: {name}\nRoll number: {roll}\nMarks: {marks}\n")
print("Student details saved.")
