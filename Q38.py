"""Assignment 5 - Question 38
Convert lowercase file content to uppercase in another file.
Run this file directly in VS Code.
"""

with open("sample.txt", "r", encoding="utf-8") as source:
    content = source.read()
with open("uppercase.txt", "w", encoding="utf-8") as destination:
    destination.write(content.upper())
print("Converted content saved in uppercase.txt")
