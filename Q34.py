"""Assignment 5 - Question 34
Count occurrences of a word in file.
Run this file directly in VS Code.
"""

word = input("Word: ").casefold()
with open("sample.txt", "r", encoding="utf-8") as file:
    words = file.read().casefold().split()
print("Occurrences =", words.count(word))
