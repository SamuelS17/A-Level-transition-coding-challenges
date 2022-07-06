tree = [0,"Q. Is it a mammal","Q. Would it be found on a farm or in homes","Q. Is it a bird","Q. Do humans eat this animal in the uk","Q. Does it always stay on land","Q. Can it fly","Q. Is it an insect","Q. Does it have wool","Q. Can you ride on it","Q. Does it have stripes","Q. Does it spend most of its life in the water","A Sparrow","Q. Does it live in colder regions","Q. Can it fly (in general)","Q. Has it usually got eight limbs","A sheep","Q. Do we drink its milk","A horse","Q. Does it bark","A Tiger","A Lion","Q. is it bigger than an elephant","A Seal",24,25,"A Penguin","An ostrich","Q. Does it produce honey","Q. Can it sting/bite you","Q. Does it live in water","A squid",32,33,"A cow","A Pig",36,"A Cow","A Dog","A Cat",40,41,42,43,"A Whale","A Dolphin",46,47,48,49,50,51,52,53,54,55,"A bee","A wasp","An ant","A termite","An octopus","A spider"]
print("Pick one of the following animals and then answer the questions so that I can guess which one it is: \n \n horse, cow, sheep, pig, dog, cat, lion, tiger, whale, dolphin, seal, penguin, ostrich, sparrow, spider, ant, bee, wasp, termite, octopus, squid \n")
current_item = 1
while tree[current_item][0] == "Q":
    ans = input(tree[current_item]+ "? ").lower()
    if ans in ("y","yes","yeah"):
        current_item = current_item*2
    else:
        current_item = current_item*2 + 1
print("I believe you are looking for", tree[current_item])