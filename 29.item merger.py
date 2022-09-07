listA = ["milk","bread","orange juice","cereal"]
listB = ["milk","carrots","orange juice","cookies","chochalte bars"]
for items in listA:
  if items in listB:
    print(items, "is in both lists")
listC = set(listA+listB)
print(listC)