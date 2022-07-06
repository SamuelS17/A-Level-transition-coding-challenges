n = int(input("Enter an integer: "))
factorial = 1
for i in range(0,n):
    factorial = (n-i)*factorial
if n == 0:
    factorial = 1
print(factorial)