"""Assignment 5 - Question 8
Count words in text file.
Run this file directly in VS Code.
"""

with open("sample.txt", "r", encoding="utf-8") as file:
    print("Words =", len(file.read().split()))
