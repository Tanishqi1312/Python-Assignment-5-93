"""Assignment 5 - Question 33
Count digits and special characters in file.
Run this file directly in VS Code.
"""

with open("sample.txt", "r", encoding="utf-8") as file:
    text = file.read()
digits = sum(ch.isdigit() for ch in text)
special = sum(not ch.isalnum() and not ch.isspace() for ch in text)
print("Digits:", digits, "Special characters:", special)
