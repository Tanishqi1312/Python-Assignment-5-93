"""Assignment 5 - Question 19
Store multiplication table in text file.
Run this file directly in VS Code.
"""

n = int(input("Enter number: "))
with open("table.txt", "w", encoding="utf-8") as file:
    for i in range(1, 11): file.write(f"{n} x {i} = {n*i}\n")
print("Table saved in table.txt")
