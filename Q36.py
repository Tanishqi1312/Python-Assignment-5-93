"""Assignment 5 - Question 36
Find longest word in file.
Run this file directly in VS Code.
"""

with open("sample.txt", "r", encoding="utf-8") as file:
    words = file.read().split()
print("Longest word:", max(words, key=len) if words else "No words")
