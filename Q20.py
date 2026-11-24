"""Assignment 5 - Question 20
Store first 100 natural numbers in text file.
Run this file directly in VS Code.
"""

with open("numbers.txt", "w", encoding="utf-8") as file:
    file.write("\n".join(str(n) for n in range(1, 101)))
print("Numbers saved.")
