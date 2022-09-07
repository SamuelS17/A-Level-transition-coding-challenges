#this one I made by myself

import time
print("    _________")
print("  (/         \) ")
print(" (/           \) ")
print("  (\          /)              Kidnapped")
print("   (\       /)                 In The")
print("    (\     /)                  Jungle")
print("      ¦   ¦                  -----------")
print("      ¦   ¦                  -----------")
print("      ¦   ¦")
print("      ¦   ¦")
print("      ¦   ¦")
print("      ¦   ¦")
print()
print()

name = input("What is your name? > ")

if name == "samuel" or  name =="sam":
  print ("Good name!")
  play = input("Would you like to play? y/n --> ")
  
  if play == ("y"):
    print ()
  if play == ("n"):
    print ("Well done you automatically win because you're awesome!")
    time.sleep(2)
    print ("Your score is 1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000!")
    time.sleep(1)
    print ("Well done!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    exit()
if name == "tim" or name == "timothy":
  print ("Oh My Gosh! It's You!")
  time.sleep(2)
  print ("You automatically die!")
  time.sleep(2)
  print ("Congratulations! (sarcastically)")
  time.sleep(2)
  print ("Your score is -10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000!")
  exit()
if name != ("sam" or "samuel" or "tim" or "timothy" or "timo"):
  print ()
  print ("Welcome", name, "to Kidnapped in the Jungle! You are in a hotel in a jungle and someone has just been kidnapped. Your aim is to make your way through the jungle and save the person. However, on your path there will be many dangerous animals and in the final level you will face the kidnapper who is armed with a gun. Along your path you must choose your options wisely. Each level you get past you will receive 100 points and your total score will be given to you at the end of the game. Good Luck!")
  time.sleep(20)



def scenario10():
 print ()
 print ("##############################################")
 time.sleep(1)
 print ()
 print ("You untie the kidnapped person and he is free. Now you must escape without being seen. Do you:")
 time.sleep(4)
 print ("1. Go back the way you came")
 time.sleep(1)
 print ("2. use your weapon")
 time.sleep(1)
 print ("3. climb up the trees")
 time.sleep(1)
 scenario_10 = input("Enter Choice: ")
#RORY IS COOL
 if scenario_10 == ("1"):
   print ("You go back the way you came but the kidnapper sees you and shoots you!")
   time.sleep(4)
   print ("You are dead!")
   time.sleep(1)
   print ("Your score is 800.")
 if scenario_10 == ("2"):
   if weapon == ("gun"):
     print ("You shoot him and he dies. You take the kidnapped person back to the hotel!")
     time.sleep(4)
     print ("Congratulations! You have won!")
     time.sleep(1)
     print ("Your score is 1200!")
   if weapon == ("poison" or "knife"):
     print ("You walk up to the kidnapper with your", weapon, "but he notices you and shoots you!")
     time.sleep(4)
     print ("You are dead!")
     time.sleep(1)
     print ("Your score is 800.")
 if scenario_10 == ("3"):
   print ("You climb up the trees and use the vines to swing your way out of the kidnappers’s base. You take the kidnapped person back to the hotel.")
   time.sleep(5)
   print ("Congratulations you have won!")
   time.sleep(1)
   print ("Your score is 1200!")



def scenario9():
 print ()
 print ("##############################################")
 time.sleep(1)
 print ()
 print ("You reach the kidnapper’s base but he is standing in your way with a gun behind some trees. Do you:")
 time.sleep(5)
 print ("1. use your weapon")
 time.sleep(1)
 print ("2. look around for things that could help")
 time.sleep(1)
 print ("3. walk around his base to see if there is another way in")
 time.sleep(1)
 scenario_9 = input("Enter Choice: ")

 if scenario_9 == ("1"):
   if weapon == ("gun"):
     print ("You shoot him and he dies you untie the kidnapped person and take him back to the hotel. ")
     time.sleep(4)
     print ("Congratulations you have won!")
     time.sleep(1)
     print ("Your score is 1100!")
   if weapon == ("poison" or "knife"):
     print ("You walk up to him with your", weapon, "but he notices you and shoots you!")
     time.sleep(4)
     print ("You are dead!")
     time.sleep(1)
     print ("Your score is 700!")
 if scenario_9 == ("2"):
   print ("you look around and you see a stone,  a spear and a vine. Do You use the:")
   time.sleep(4)
   print ("1. stone")
   time.sleep(1)
   print ("2. spear")
   time.sleep(1)
   print ("3. vine")
   time.sleep(1)
   scenario_9_2 = input("Enter Choice: ")
   if scenario_9_2 == ("1"):
     print ("You pick up the stone and throw it at him. He turns around and you duck. You run around to the  other side of his base and he doesn't notice you!")
     time.sleep(6)
     scenario10()
   if scenario_9_2 == ("2"):
     print ("You throw the spear at the kidnapper but it is too blunt and doesn't pierce his skin. He turns around and you duck. You run around to the other side of his base and he doesn't notice.")
     time.sleep(7)
     scenario10()
   if scenario_9_2 == ("3"):
     print ("You try to swing over him but he notices you and shoots you.")
     time.sleep(3)
     print ("You are dead!")
     time.sleep(1)
     print ("Your score is 700.")
 if scenario_9 == ("3"):
   print ("You walk around his camp to the other side but he sees you and shoots you!")
   time.sleep(3)
   print ("You are dead!")
   time.sleep(1)
   print ("Your score is 700.") 



def scenario8():
 print ()
 print ("##############################################")
 time.sleep(1)
 print ()
 print ("You carry on walking and come across a river with stepping stone going acros it. However, when you look in to the water you see some Piranhas. Do You:")
 time.sleep(3)
 print ("1. Swim across")
 time.sleep(1)
 print ("2. go across the stepping stones")
 time.sleep(1)
 print ("3. look around for thing that could help")
 time.sleep(1)
 scenario_8 = int(input("Enter Choice -->"))

 if scenario_8 == 1:
   print ("Youy swim across and the piranhas rip you to peices!")
   time.sleep(2)
   print("You are dead!")
   time.sleep(1)
   print ("Your score was 600.")
 if scenario_8 == 2:
   print ("You try walking across the stepping stones but the piranhas jump up and drag you into the water. They then rip you to peices!")
   time.sleep(3)
   print ("You are dead!")
   time.sleep(1)
   print ("Your score was 600.")
 if scenario_8 == 3:
   print ("You see:")
   time.sleep(1)
   print ("1. A short but thick vine")
   time.sleep(1)
   print ("2. A long but thin vine")
   scenario_8_2 = int(input("Which one do you choose --> "))
   if scenario_8_2 == 1:
     print ("You take the vine and swing across the river, making it to the other side.")
     time.sleep(3)
     scenario9()
   if scenario_8_2 == 2:
     print ("You take the vine and swing across the river but it snaps. You fall into the river and the piranhas rip you to peices!")
     time.sleep(3)
     print ("You are dead!")
     time.sleep(1)
     print ("Your score was 600.")



def scenario7():
 print ()
 print ("##############################################")
 time.sleep(1)
 print ()
 print ("You hear a growl nearby and a tiger jumps out at you. do you:")
 time.sleep(2)
 print ("1. use your weapon")
 time.sleep(1)
 print ("2. runaway")
 time.sleep(1)
 print ("3. climb up the trees")
 time.sleep(1)
 scenario_7 = int(input("Enter choice: "))
 time.sleep(1)

 if scenario_7 == 1:
   if weapon == ("gun"):
     print ("You shoot the tiger and it dies.")
     time.sleep(2)
     scenario8()
   if weapon == ("knife"):
     print ("You try to stab the tiger but it bites your arm off and then your head!")
     time.sleep(2)
     print ("You are dead!")
     time.sleep(1)
     print ("Your score is 500")
   if weapon == ("poison"):
     print ("You throw the poison at it and it runs away.")
     time.sleep(2)
     scenario8()
 if scenario_7 == 2:
   print ("You try to run away but the tiger is too fast for you. It catches up with you and bites your head off.")
   time.sleep(3)
   print ("You are dead!")
   time.sleep(1)
   print ("Your score is 500")
 if scenario_7 == 3:
   print ("You climb up the trees and are out of reach of the tiger. It walks away and leaves you alone.")
   time.sleep(3)
   scenario8()
     
     



def scenario6():
 print ()
 print ("##############################################")
 time.sleep(1)
 print ()
 print ("You hear something rustling in the bushes. An anmimal walks out. It is a rhino! The rhino sees you and charges at you! Do you:")
 time.sleep(4)
 print ("1. use your weapon")
 time.sleep(1)
 print ("2. run away")
 time.sleep(1)
 print ("3. look around for hiding places.")
 time.sleep(1)
 scenario_6 = input("Enter Choice: ")

 if scenario_6 == ("1"):
   if weapon == ("gun"):
     print ("You shoot the rhino but its skin is too tough and you can't kill it. It charges into you and you die")
     time.sleep(5)
     print ("You are dead!")
     time.sleep(1)
     print ("Your score is 400.")
   if weapon == ("knife"):
     print ("You try to stab it but its skin is too thick! It charges into you and you die.")
     time.sleep(3)
     print ("You are dead!")
     time.sleep(1)
     print ("Your score is 400.")
   if weapon == ("poison"):
     print ("You throw the poison at its eyes and it stops charging at you. It is blind. It turns around and runs away.")
     time.sleep(4)
     scenario7()
 if scenario_6 == ("2"):
   print ("You run away but it is too fast for you and it tramples over you.")
   time.sleep(3)
   print ("You are dead!")
   time.sleep(1)
   print ("Your score is 400.")
 if scenario_6 == ("3"):
   print ("You look around for hiding places and you see:")
   time.sleep(3)
   print ("1. a tree")
   time.sleep(1)
   print ("2. a hole in the ground")
   time.sleep(1)
   print ("3. a bush")
   time.sleep(1)
   scenario_6_2 = input("Where do you hide? >> ")

   if scenario_6_2 == ("1"):
     print ("You try to climb up the tree but you are too slow and the rhino rams into you!")
     time.sleep(3)
     print ("You are dead!")
     time.sleep(1)
     print ("Your score is 400")
   if scenario_6_2 == ("2"):
     print ("You jump into the hole but the hole is too small and your head is sticking out. You are trampled over by the rhino!")
     time.sleep(4)
     print ("You are dead!")
     time.sleep(1)
     print ("Your score is 400.")
   if scenario_6_2 == ("3"):
     print ("You jump into the bush and the rhino runs past. Once it is out of sight you carry on walking.")
     time.sleep(4)
     scenario7()


   



def scenario5():
  print ()
  print ("##############################################")
  time.sleep(1)
  print ()
  print ("You carry on walking and you notice a poison dart frog. It jumps at you and you have a split second to make your decision. Do you:")
  time.sleep(4)
  print ("1. use your weapon")
  time.sleep(1)
  print ("2. squash it with your hand")
  time.sleep(1)
  print ("3. walk past")
  time.sleep(1)
  scenario_5 = input("Enter Choice: ")

  if scenario_5 == ("1"):
    print ("You were too slow to pull out your", weapon, "and were poisoned by the frog.")
    time.sleep(4)
    print ("You are dead!")
    time.sleep(1)
    print ("Your score is 400")
  if scenario_5 == ("2"):
    print ("You squash it with your hand and it dies but so do you as you are poisonned.")
    time.sleep(3)
    print ("You are dead!")
    time.sleep(1)
    print ("Your score is 400")
  if scenario_5 == ("3"):
    print ("You walk past it and it lands behind you. You run away and it is out of sight.")
    time.sleep(3)
    scenario8()



def scenario4():
  print ()
  print ("##############################################")
  time.sleep(1)
  print ()
  print ("After walking around the lake, you see a monkey in the trees. It comes down and scratches you on the head. Then you notice some other monkeys in the trees and they look angry. They quikly jump down off the trees and they are going to attack you. Do you:")
  time.sleep(8)
  print ("1. use your weapon on them")
  time.sleep(1)
  print ("2. run away")
  time.sleep(1)
  print ("3. curl into a ball on the floor")
  time.sleep(1)
  scenario_4 = input("Enter Choice: ")

  if scenario_4 == ("1"):
    if weapon == ("gun"):
      print ("You use your gun but you are too slow to reload. You are unable to shoot all of the monkeys and you are scratched to death.")
      time.sleep(4)
      print ("You are dead!")
      time.sleep(1)
      print ("Your score is 300")
    if weapon == ("knife"):
      print ("You use your knife and you kill them all.")
      time.sleep(2)
      scenario6()
    if weapon == ("poison"):
      print ("You use your poison on the monkeys but you eventually run out and you are scratched to death.")
      time.sleep(4)
      print ("You are dead!")
      time.sleep(1)
      print ("Your score is 300")
  if scenario_4 == ("2"):
    print ("You run away but the monkeys are too fast for you. They catch up with you and you scratched to death.")
    time.sleep(4)
    print ("You are dead!")
    time.sleep(1)
    print ("Your score is 300")
  if scenario_4 == ("3"):
    print ("You curl up into a ball and the monkeys no longer think you are a threat. They leave you alone.")
    time.sleep(4)
    scenario5()


def scenario3():
  print ()
  print ("##############################################")
  print ()
  time.sleep(1)
  print ("Whilst getting out of the boat you trip over and see something moving on the floor. It is a snake! Do you:")
  time.sleep(5)
  print ("1. Use your weapon and kill it.")
  time.sleep(1)
  print ("2. Stamp on it")
  time.sleep(1)
  print ("3. Run away")
  time.sleep(1)
  scenario_3 = input("Enter Choice: ")

  if scenario_3 == ("1"):
    print ("You use your", weapon, "and it dies.")
    time.sleep(2)
    scenario5()
  if scenario_3 == ("2"):
    print ("You stamp on it. It gets agitated and it bites you!")
    time.sleep(3)
    print ("You are dead!")
    time.sleep(1)
    print ("nice try!")
    time.sleep(1)
    print ("Your score is: 300")
  if scenario_3 == ("3"):
    print ("You run away and the snake slithers into the bushes.")
    time.sleep(3)
    scenario6()
  
    


def scenario2():
  print ()
  print ("##############################################")
  print ()
  print("You are walking and you come across a lake. Do you: ")
  time.sleep(3)
  print ("1. swim across")
  time.sleep(1)
  print ("2. walk around it")
  time.sleep(1)
  print ("3. look around for things that could help")
  time.sleep(1)
  scenario_2 = input("Enter Choice: ")

  if scenario_2 == ("1"):
    print ("You swim across the lake and a crocodile eats you whole!")
    time.sleep(3)
    print ("You are dead!")
    time.sleep(1)
    print ("nice try")
    time.sleep(1)
    print ("Your score is: 200")
  if scenario_2 == ("2"):
    print ("You walk around the lake but a pack of wolves see you and they tear you to peices!")
    time.sleep(3)
    print ("You are dead!")
    time.sleep(1)
    print ("nice try")
    time.sleep(1)
    print ("Your score is: 200")
  if scenario_2 == ("3"):
    print ("You look around and you see:")
    time.sleep(2)
    print ("1. A boat")
    time.sleep(1)
    print ("2. Some stilts")
    time.sleep(1)
    print ("3. A recently killed animal")
    time.sleep(1)
    scenario_2_2 = input("Which one will you choose? > ")
    
    if scenario_2_2 == ("1"):
      print ("You take the boat to the other side of the lake.")
      time.sleep(3)
      scenario3()
    if scenario_2_2 == ("2"):
      print ("You use the stilts to walk across the lake but you step on a crocodile and it bites the stilts. You then fll into the water and are eaten alive!")
      time.sleep(5)
      print ("You are dead!")
      time.sleep(1)
      print ("nice try")
      time.sleep(1)
      print ("Your score is: 200")
    if scenario_2_2 == ("3"):
      print ("You walk around the lake and see some wolves. You throw the carcass at them and they start eating it. You run around them and reach the other side of the lake.")
      time.sleep(5)
      scenario4()

carryon = True


while carryon:
  print ()
  print ()
  print ("#################################################")
  time.sleep(1)
  print ()
  print ()
  print ("You see a shed just outside the hotel and you go inside. You find some weapons. You must choose one of them. Your choices are : ")
  time.sleep(4)
  print ("1. a gun")
  time.sleep(1)
  print ("2. a knife")
  time.sleep(1)
  print ("3. a bottle with some poison in it")
  time.sleep(1)
  scenario_1 = input("Enter Choice: ")


  if scenario_1 == ("1"):
    weapon = ("gun")
  if scenario_1 == ("2"):
    weapon = ("knife")
  if scenario_1 == ("3"):
    weapon = ("poison")

  print ("Nice Choice!")  

  time.sleep(3)
  scenario2()

  time.sleep(2)
  ask = True
  

  while ask:
    print ()
    again = input("Would you like to play again? y/n >> ")  

    if again == ("y"):
      ask = False
    elif again == ("n"):
      ask = False
      carryon = False
      print()
      print ("Goodbye", name, "!")
    else:
      print ("That is not a valid option!")
      ask = True