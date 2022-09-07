total =0
for i in range (1, 100000000000000000000):
    #This won't run particularly quickly
    total += 1/(i**2)
pi = (total*6)**0.5
print(pi)