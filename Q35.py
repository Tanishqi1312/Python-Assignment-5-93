"""Assignment 5 - Question 35
Search for word and report whether it exists.
Run this file directly in VS Code.
"""

word = input("Word to search: ").casefold()
with open("sample.txt", "r", encoding="utf-8") as file:
    exists = word in file.read().casefold().split()
print("Word exists." if exists else "Word not found.")
