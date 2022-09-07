from random import randint as r
length = r(8,15)
password = ""
for i in range(length):
  char = chr(r(33,126))
  password += char
print("Your password is: ", password)
f=open("password.txt","w")
f.write(password)
f.close()