import random
import time



def cmaj():
  cmaj = ['C','D','E','F','G','A','B']
  pause = float(input('Enter an interval in seconds:'))
  for notes in range(0,6):
    print(random.choice(cmaj))
    time.sleep(pause)    
def dmaj():
  dmaj = ['D','E','F#','G','A','B','C#']
  pause = float(input('Enter an interval in seconds:'))
  for notes in range(0,6):
    print(random.choice(dmaj))
    time.sleep(pause)
def emaj():
  emaj = ['E','F#','G#', 'A','B','C#','D#']
  pause = float(input('Enter an interval in seconds:'))
  for notes in range(0,6):
    print(random.choice(emaj))
    time.sleep(pause)
def fmaj():
  fmaj = ['F','G','A','B♭','C','D','E']
  pause = float(input('Enter an interval in seconds:'))
  for notes in range(0,6):
    print(random.choice(fmaj))
    time.sleep(pause)
def gmaj():
  gmaj = ['G','A','B','C','D','E','F#']
  pause = float(input('Enter an interval in seconds:'))
  for notes in range(0,6):
    print(random.choice(gmaj))
    time.sleep(pause)
def amaj():
  amaj = ['A', 'B','C#','D','E','F#','G#']
  pause = float(input('Enter an interval in seconds:'))
  for notes in range(0,6):
    print(random.choice(amaj))
    time.sleep(pause)
def bmaj():
  bmaj = ['B','C#','D#','E','F#','G#','A#']
  pause = float(input('Enter an interval in seconds:'))
  for notes in range(0,12):
    print(random.choice(bmaj))
    time.sleep(pause)
  
choice = input("Choose a scale:\n").lower()
if choice == 'amaj':
  amaj() 
elif choice == 'bmaj':
  bmaj()
elif choice == 'cmaj':
  cmaj()
elif choice == 'dmaj':
  dmaj()
elif choice == 'emaj':
  emaj()
elif choice == 'fmaj':
  fmaj()
elif choice == 'gmaj':
  gmaj()