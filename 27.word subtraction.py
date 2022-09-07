word1 = input("Enter the first word: ")
word2 = input("Enter the second word: ")
num1 = 0
num2 = 0
for i in word1:
    num1 += ord(i)
for j in word2:
    num2 += ord(j)
ans = num1 - num2
print(ans)