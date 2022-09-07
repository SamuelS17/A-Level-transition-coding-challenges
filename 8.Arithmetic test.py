import random as r
total = 0
operations = ["+", "-", "/", "X"]
name = input("Enter your name: ")
for i in range (0,10):
    operation = r.choice(operations)
    num1 = r.randint(1,12)
    num2 = r.randint(1,12)
    sum = str(num1)+operation+str(num2)
    if operation == "+":
        ans = num1+num2
    elif operation == "-":
        ans = num1-num2
    elif operation == "/":
        ans = round(num1/num2,0)
    else:
        ans = num1*num2
    print(sum)
    studentAns = int(input("Enter your answer (to the nearest whole number): "))
    if ans == studentAns:
        print("That is correct")
        total+=1
print("This student's total score was", str(total))