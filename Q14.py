"""Assignment 5 - Question 14
Accept user text and store in file.
Run this file directly in VS Code.
"""

text = input("Enter text to save: ")
with open("user_text.txt", "w", encoding="utf-8") as file:
    file.write(text)
print("Text saved.")
