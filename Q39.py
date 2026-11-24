"""Assignment 5 - Question 39
Write file content in reverse character order to another file.
Run this file directly in VS Code.
"""

with open("sample.txt", "r", encoding="utf-8") as source:
    content = source.read()
with open("reverse.txt", "w", encoding="utf-8") as destination:
    destination.write(content[::-1])
print("Reversed content saved.")
