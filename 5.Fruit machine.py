from random import choice as r
import time
symbols = ["Cherry", "Bell", "Lemon", "Orange", "Star", "Skull"]
credits = 1.0
stop = False
print ("The Rules: \nYou start with £1.00 and every spin costs 20p\nIf you get 2 of the same symbol you win 50p\nIf you get 3 of the same symbol you get £1/nIf you get 3 bells you get £5\nHowever if you get 2 skulls you lose £1\nIf you get 3 skulls you lose all your money\n")
'''f = open("Highscore.txt","r")
print("The current highscore is £"+f.read()+"0")
f.close()'''
print("Bank: £"+str(credits)+"0")
while not stop and credits>= 0.20:
    input("Click enter to spin")
    credits = credits-0.2
    symbol1 = r(symbols)
    symbol2 = r(symbols)
    symbol3 = r(symbols)
    time.sleep(0.5)
    print(symbol1)
    time.sleep(0.5)
    print(symbol2)
    time.sleep(0.5)
    print(symbol3)
    time.sleep(1)
    spin = [symbol1,symbol2,symbol3]
    if spin.count("Skull")==3:
        print("You lose all your money")
        credits = 0.0
    elif spin.count("Bell")==3:
        print("You win £5")
        credits+=5.0
    elif len(set(spin))==1:
        print("You win £1")
        credits+=1.0
    elif spin.count("Skull")==2:
        print("You lose £1")
        credits-=1.0
        if credits<0:
            credits_owed = 0-credits
            print("You owe ME £"+str(round(credits_owed,2))+"0")
    elif len(set(spin))==2:
        print("You win 50p")
        credits+=0.5
    else:
        print("You didn't win anything")
    if credits>=0.2:
        print("Bank: £"+str(round(credits,2))+"0")
        again = input("Would you like to spin again y/n: ").lower()
        if again == "n":
            stop = True

print("You finished with £"+str(round(credits,2))+"0")
#self-extension - i don't know why it wasn't working
'''f=open("Highscore.txt", "r+")
current_highscore = f.read()
print(current_highscore)
if float(current_highscore)<credits:
    f.write(str(credits))
    print("You got a new highscore - congratulations!")
f.close()'''