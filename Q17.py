"""Assignment 5 - Question 17
Copy one text file to another.
Run this file directly in VS Code.
"""

with open("sample.txt", "r", encoding="utf-8") as source:
    content = source.read()
with open("copy.txt", "w", encoding="utf-8") as destination:
    destination.write(content)
print("File copied.")
