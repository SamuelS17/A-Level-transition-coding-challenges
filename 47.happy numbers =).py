nums_found=0
num = 1
total=0
count = 1
print("1 is a happy number")
while count<8:
    num+=1
    num2 = num
    checks = 0
    while num2!=1 and checks<100:
        num_string = str(num2)
        for i in num_string:
            total+= int(i)**2
        num2 = total
        total = 0
        checks +=1
    if checks<100:
        print(str(num)+" is a happy number")
        count+=1
