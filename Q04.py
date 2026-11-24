"""Assignment 5 - Question 4
Read file line by line using readline().
Run this file directly in VS Code.
"""

with open("sample.txt", "r", encoding="utf-8") as file:
    line = file.readline()
    while line:
        print(line, end="")
        line = file.readline()
