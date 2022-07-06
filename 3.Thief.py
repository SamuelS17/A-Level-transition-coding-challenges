
'''digits = []
for i in range(4):
    digits.append(input("Enter a digit: "))
    digits2 = digits
sequence = ""
'''
#I gave up so i did this
num1,num2,num3,num4 = (input("Enter the 4 digits (leave a space bar between each digit): ")).split()
print("Here are all the possible combinations:")
print(num1+num2+num3+num4)
print(num1+num2+num4+num3)
print(num1+num3+num2+num4)
print(num1+num3+num4+num2)
print(num1+num4+num2+num3)
print(num1+num4+num3+num2)
print(num2+num1+num3+num4)
print(num2+num1+num4+num3)
print(num2+num3+num1+num4)
print(num2+num3+num4+num1)
print(num2+num4+num1+num3)
print(num2+num4+num3+num1)
print(num3+num1+num2+num4)
print(num3+num1+num4+num2)
print(num3+num2+num1+num4)
print(num3+num2+num4+num1)
print(num3+num4+num1+num2)
print(num3+num4+num2+num1)
print(num4+num1+num2+num3)
print(num4+num1+num3+num2)
print(num4+num2+num1+num3)
print(num4+num2+num3+num1)
print(num4+num3+num1+num2)
print(num4+num3+num2+num1)
#it still works




'''
digits2 = digits
for i in range(0,3):
    sequence+=digits[i]
    digits.remove(digits[i])
    for j in range(0,2):
        sequence+=digits[j]
        digits.remove(digits[j])
        for k in range(0,1):
            sequence+=digits[k]
            digits.remove(digits[k])
            sequence+=digits[0]
            print(sequence)
            sequence = ""
    print(digits2)
    digits = digits2
    print(digits2)
    '''