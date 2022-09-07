word = input("Enter a word: ")
if word.upper() == word[::-1].upper():
  print("The word",word, "is a palindrome.")
else:
  print("The word",word, "is not a palindrome.")