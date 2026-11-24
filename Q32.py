"""Assignment 5 - Question 32
Count uppercase and lowercase letters in file.
Run this file directly in VS Code.
"""

with open("sample.txt", "r", encoding="utf-8") as file:
    text = file.read()
print("Uppercase:", sum(ch.isupper() for ch in text))
print("Lowercase:", sum(ch.islower() for ch in text))
