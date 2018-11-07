import random
import time

def intro():
  print('\nYou get to the old dark forest. It\'s getting dark and the storm is starting.\nThere is no house on sight.\n')
  time.sleep(2)
  print('You have only two options.\n')
  time.sleep(1)
  print('Hide in a big cave or move along and try to get to some warm house to survive the night.\n')
  time.sleep(1)
  
def choice():
  option = ''
  print('What would you do?\n')
  time.sleep(1)
  print('1. Try to hide in a cave.\n')
  time.sleep(1)
  print('2. Or move along.\n')
  time.sleep(1)
  while option != '1' and option != '2':
    option = input('Type "1" or "2": ')
    print()
  return option

def checkChoice(optionNum):
  if optionNum == '1':
    caveOption = random.randint(1, 2)
    time.sleep(1)
    if caveOption == 1:
      print('You\'ve found a great treasure, amazing silver sword forged by first Witchers.\nNow you will be invincible!!!')
    else:
      print('The cave was full of Alghuls. They attacked you immediately and unfortunately, kill you.')
  else:
    caveOption = random.randint(1, 2)
    time.sleep(1)
    if caveOption == 1:
      print('You safely get through the forest and reach the village where you finally can rest.')
    else:
      print('Horde of werevolves attack you! You\'ve fight bravely but there was too many of them. They killed you and ate your heart.')

def again():
  playAgain = input('\nWould you like to play again?\nType "yes" if you would: ')
  return playAgain


playAgain = input('Hello, would you like to play in a "Witcher\'s Realm" game?\nType "yes" if you would: ')

while playAgain == 'yes' or playAgain == 'y':
  intro()
  checkChoice(choice())
  playAgain = again()
  
print('Alright, see you next time!!!\n')
time.sleep(2)
exit()

  

