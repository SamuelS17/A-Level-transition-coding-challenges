vowels = ["a","e","i","o","u"]
word = input("Enter a word: ")
reverse = word[::-1]
print(reverse)
count = 0
for letters in word:
    if letters in vowels:
        count+=1
count = str(count)
print("There are %s vowels in this word" % count)