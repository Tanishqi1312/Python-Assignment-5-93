"""Assignment 5 - Question 15
Append text to existing file.
Run this file directly in VS Code.
"""

text = input("Text to append: ")
with open("user_text.txt", "a", encoding="utf-8") as file:
    file.write("\n" + text)
print("Text appended.")
