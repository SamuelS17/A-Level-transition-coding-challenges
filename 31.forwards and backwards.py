word = input("Enter a word: ")
if word == word[::-1]:
  print("This is a palindrome")
else:
  print("This is not a palindrome")