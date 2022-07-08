#this program uses the Luhn algorithm
#the number may fit the pattern but it is not necessarily a valid card numer e.g. 4200000000000000 fits the visa number pattern but is definitely not valid
card_number = input("Please enter your card number (no spaces): ")
num_length = len(card_number)
flipped = []
for i in range(0,num_length):
    flipped.append(card_number[num_length-i-1])

for j in range(0,num_length):
    if (j+1)%2==0:
        flipped[j] = int(flipped[j])*2

for k in range(0,num_length):
    if len(str(flipped[k])) >1:
        flipped.append(str(flipped[k])[1])
        flipped[k] = str(flipped[k])[0]
total = 0
for l in flipped:
    total+=int(l)
if total%10 ==0:
    card_type = ''
    if card_number[0] == '4' and (num_length == 13 or num_length) == 16:
        card_type = input("Is this card a Visa card (y/n): ").lower()
    elif (card_number[0:2] == '34' or card_number[0:2] == '37') and num_length == 15:
        card_type = input("Is this card an American Express card (y/n): ").lower()
    elif (int(card_number[0:2]) >= 51 and int(card_number[0:2]) <= 55) and num_length == 16:
        card_type = input("Is this card a MasterCard card (y/n): ").lower()
    elif (card_number[0:4]=='6011' or card_number[0:2] == '65') and num_length == 16:
        card_type = input("Is this card a Discover card (y/n): ").lower()
    else:
        print("Either this card is invalid or you use some rubbish little small card company!")

    if card_type == 'y':
        print("This card number is valid")
    else:
        print("This card number is invalid")
else:
    print("This card number is invalid")