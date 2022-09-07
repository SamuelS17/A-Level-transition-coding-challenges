listOfNums = []
for i in range(0,10):
    num = int(input("Enter a number"))
    listOfNums.append(num)
print("Unsorted list:")
print(listOfNums)
sort=False
while not sort:
    sort=True
    for i in range (0,len(listOfNums)-1):
        if listOfNums[i]>listOfNums[i+1]:
            listOfNums[i], listOfNums[i+1] = listOfNums[i+1], listOfNums[i]
            sort=False
asc_or_desc = input("Would you like this list in ascending or descending order?(a/d): ")
print("Sorted list:")
if asc_or_desc == 'a':
    print(listOfNums)
elif asc_or_desc == 'd':
    print(listOfNums[::-1])