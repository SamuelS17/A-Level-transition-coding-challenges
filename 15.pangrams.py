import string
words = input("Enter a string: ")
letters = list(string.ascii_lowercase)
pangram = True
for i in letters:
    if i not in words.lower():
        print("This is not a pangram")
        pangram = False
        break
if pangram:
    print("This is a pangram")