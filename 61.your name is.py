from unicodedata import name


name_ = input("Enter your name: ")
age = input("Enter your age: ")
form = input("Enter your form: ")
details = "Your name is "+name_+", your age is "+age+", your form is "+form
print(details)
f = open("details.txt","w")
f.write(details)
f.close()