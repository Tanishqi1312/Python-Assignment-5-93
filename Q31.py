"""Assignment 5 - Question 31
Count vowels in text file.
Run this file directly in VS Code.
"""

with open("sample.txt", "r", encoding="utf-8") as file:
    text = file.read().lower()
print("Vowels =", sum(ch in "aeiou" for ch in text))
