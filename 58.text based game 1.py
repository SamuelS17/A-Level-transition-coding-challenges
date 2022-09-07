#I may have used a starter pack with this one

import time
import random

def showInstructions():
  print('''
RPG Game
Just Escape the house!
It's as simple as that!
Oh but watch out for the monsters and giant octopi!
And you may need a couple of items to get through the door.
========
Commands:
  go [direction]
  get [item]
''')

def showStatus():
  print('---------------------------')
  print('You are in the ' + currentRoom)
  print('Inventory : ' + str(inventory))
  if "item" in rooms[currentRoom]:
    print('You see a ' + rooms[currentRoom]['item'])
  print("---------------------------")

inventory = []

rooms = {

            'Hall' : { 
                  'south' : 'Kitchen',
                  'east' : 'Dining Room',
                  'north' : 'Garden',
                  'item' : 'key'
                },

            'Kitchen' : {
                  'north' : 'Hall',
                  'east' : 'Study',
                  'west' : 'Freezer room'
                },


            'Dining Room' : {
                  'west' : 'Hall',
                  'south' : 'Study',
                  'east' : 'Toilet'
                },
                
            'Study' : {
                  'north' : 'Dining Room',
                  'west' : 'Kitchen',
                  'south' : 'Bedroom',
                  'item' : 'note'
                },
            'Toilet' : {
                  'west' : 'Dining Room',
                  'item' : 'giant octopus'
                },
            'Bedroom' : {
                  'north' : 'Study',
                  'south' : 'Exit'
                },
            'Garden' : {
                  'south' : 'Hall',
                  'west' : 'Monster cage',
                  'item' : 'hedge trimmer'
                },
            'Monster cage' : {
                  'east' : 'Garden',
                  'item' : 'monster'
                },
            'Exit' : {
                'north' : 'Bedroom'
                },
            'Freezer room' : {
                'east' : 'Kitchen'
            }
            
            
         }

currentRoom = 'Hall'

showInstructions()

while True:

  showStatus()

  move = ''
  while move == '':  
    move = input('>')
    
  move = move.lower().split()

  if move[0] == 'go':
    if move[1] in rooms[currentRoom]:
      currentRoom = rooms[currentRoom][move[1]]
    else:
        print('You can\'t go that way!')

  if move[0] == 'get' :
    if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
      inventory += [move[1]]
      print(move[1] + ' got!')
      del rooms[currentRoom]['item']
    else:
      print('Can\'t get ' + move[1] + '!')
  if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
    print("Oh No! You entered a monster's caged and Bob the monster has ripped your head clean off... GAME OVER!")
    break
  if 'item' in rooms[currentRoom] and 'giant octopus' in rooms[currentRoom]['item']:
    print('You went in to the toilets and sat down on the toilet. A giant octopus appears and suckers your but off... GAME OVER!')
    break
  if currentRoom == 'exit' and 'key' in inventory and 'note' in inventory:
    print('You made it to the exit and escaped the house... YOU WIN!')
    break
  if currentRoom == 'exit' and 'key' in inventory:
    print('Unfortunately for you, this door has a passcode as well as a normal key lock. Perhaps you should try to find it.')
  elif currentRoom == 'exit' and 'note' in inventory:
    print('Unfortunately for you, this door has a key lock as well as a passcode. Perhaps you should try to find the key.')
  elif currentRoom == 'exit':
    print('The door is locked! Maybe find an item that will help you out.')
  
  if currentRoom == 'Freezer room':
    print ("It's freezing in here and OH NO! the door has locked behind you! You are going to die a slow and painfully cold death")
    dying_noise = ['ahhhhhhh!', 'It is so painful!', 'let me out of here!', 'I have frost bite', 'I never even wanted to come to this stupid house in the first place!', 'I want my mummy!']
    countdown = 10
    while currentRoom == 'Freezer room' and countdown >0:
      time.sleep(1)
      dying_num = random.randint(0,5)
      print(dying_noise[dying_num])
      countdown -= 1
    print ("You froze to death! ... game over!")
    break