from tkinter import *
from tkinter.ttk import*
import random 
import time

def cmaj():
  cmaj = ['C','D','E','F','G','A','B']
  for notes in range(0,6):
    print(random.choice(cmaj))
    time.sleep(int(inter.get()))   
def dmaj():
	dmaj = ['D','E','F#','G','A','B','C#']
	for notes in range(0,6):
		print(random.choice(dmaj))
		time.sleep(int(inter.get()))
def emaj():
	emaj = ['E','F#','G#', 'A', 'B','C#','D#']
	for notes in range(0,6):
		print(random.choice(emaj))
		time.sleep(int(inter.get()))
def fmaj():
	fmaj = ['F','G','A','A#','B','C','D','E']
	for notes in range(0,6):
		print(random.choice(fmaj))
		time.sleep(int(inter.get()))
def gmaj():
	gmaj = ['G','A','B','C','D','E','F#']
	for notes in range (0,6):
		print(random.choice(gmaj))
		time.sleep(int(inter.get()))
def amaj():
	amaj = ['A','B','C#','D','E','F#','G#']
	for notes in range(0,6):
		print(random.choice(amaj))
		time.sleep(int(inter.get()))
def bmaj():
	bmaj = ['B','C#','D#','E',"F#",'G#','A#']
	for notes in range(0,6):
		print(random.choice(bmaj))
		time.sleep(int(inter.get()))

#Y IS UP/DOWN
#X IS LEFT/RIGHT

window = Tk()
window.geometry('600x600')
window.title('Pracitce Scales')

#Label widget
cas = Label(window, text='Choose a scale')
cas.place(relx=0.5, rely= 0.460, anchor=CENTER,)


#Creating a Combobox
scales = Combobox(values=['Cmaj','Dmaj', 'Emaj', 'Fmaj', 'Gmaj', 'Amaj', 'Bmaj'])
scales.current(0)
scales.place(relx=0.5, rely=0.5, anchor=CENTER,)

#Set interval time label
lbl = Label(window, text='Set interval time:')
lbl.place(relx=0.5, rely=0.550, anchor=CENTER,)


#Entry
inter = Entry(window, width=4)
inter.place(relx=0.775, rely=0.550, anchor=CENTER,)

#Start function
def Start():
	if scales.get() == 'Cmaj' and inter.get() == '':
		lbl3 = Label(window, text='Please set an interval')
		lbl3.place(relx=0.5, rely=0.650, anchor=S,)
	elif scales.get() == 'Cmaj':
		cmaj()
	elif scales.get() == 'Dmaj':
		dmaj()
	elif scales.get() == 'Emaj':
		emaj()
	elif scales.get() == 'Fmaj':
		fmaj()
	elif scales.get() == 'Gmaj':
		gmaj()
	elif scales.get() == 'Amaj':
		amaj()
	elif scales.get() == 'Bmaj':
		bmaj()
	else:
		lbl2 = Label(window, text='Please scale a scale.')
		lbl2.place(relx=0.5, rely=0.650, anchor=S,)

#Start button
start = Button(window, text='Start', command=Start)
start.place(relx=0.700, rely=0.480,)
window.mainloop()