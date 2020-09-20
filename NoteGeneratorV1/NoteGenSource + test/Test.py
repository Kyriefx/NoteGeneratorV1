from tkinter import *
from tkinter.ttk import *
import random
import time
import threading



new = Tk()
new.geometry('600x600')

#Our loop that selects a random note every x seconds
def example():
  phrases = ['Boy', 'Girl','chicken', 'cow']
  for sumn in range(0,6):
    z = random.choice(phrases)
    lbl = Label(new, text=str(z))
    lbl.pack()
    time.sleep(3)

#Threading the loop 
t1 = threading.Thread(target=example)

#Creating the thread function to pass as a button command
def thr1():
  t1.start()

    
 
#Notice how the command passed is the thread function and not the example()
nbtn = Button(new, text='Say Hi', command=thr1)
nbtn.pack()
new.mainloop()

