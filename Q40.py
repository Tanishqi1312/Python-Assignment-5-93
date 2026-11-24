"""Assignment 5 - Question 40
Merge two text files into a third.
Run this file directly in VS Code.
"""

with open("file1.txt", "r", encoding="utf-8") as first:
    content1 = first.read()
with open("file2.txt", "r", encoding="utf-8") as second:
    content2 = second.read()
with open("merged.txt", "w", encoding="utf-8") as output:
    output.write(content1 + "\n" + content2)
print("Files merged into merged.txt")
