year1 = int(input("Enter a year: "))
year2 = int(input("Enter a year after the first one: "))
total = 0
for i in range(year1, year2):
    if len(set(str(i)))<len(str(i)):
        print(i)
        total+=1
print("There are "+str(total)+" years with a repeating digit in this range")