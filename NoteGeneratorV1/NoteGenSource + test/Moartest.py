from tkinter import *
from tkinter.ttk import*
import random 
import time
import threading

window = Tk()
window.geometry('600x600')
window.title('Pracitce Scales')

#Label widget
cas = Label(window, text='Choose a scale')
cas.place(relx=0.5, rely= 0.440, anchor=CENTER,)


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

#Duration entry
dury = Entry(window, width=4)
dury.place(relx=0.775, rely=0.600, anchor=CENTER,)

#Duration Label
durlbl = Label(window, text='Set a duration:')
durlbl.place(relx=0.5, rely=0.600, anchor=CENTER,)

#NewWin Function
def Cmaj():
	NewWin = Toplevel(window)
	NewWin.geometry('800x800')
	cmaj = ['C','D','E','F','G','A', 'B']
	t_end = time.time() + 60 * int(dury.get())
	while time.time() < t_end:
		for phrase in range(0,6):
			z = random.choice(cmaj)
			lbl5 = Label(NewWin, text=str(z))
			lbl5.pack()
			time.sleep(int(inter.get()))
def Dmaj():
	NewWin = Toplevel(window)
	NewWin.geometry('800x800')
	dmaj = ['D','E','F#','G','A','B', 'C#']
	t_end = time.time() + 60 * int(dury.get())
	while time.time() < t_end:
		for notes in range(0,6):
			z = random.choice(dmaj)
			lbl5 = Label(NewWin, text=str(z))
			lbl5.pack()
			time.sleep(int(inter.get()))
def Emaj():
	NewWin = Toplevel(window)
	NewWin.geometry('800x800')
	emaj = ['E', 'F#', 'G#','A','B','C#','D#']
	t_end = time.time() + 60 * int(dury.get())
	while time.time() < t_end:
		for notes in range(0,6):
			z = random.choice(emaj)
			lbl5 = Label(NewWin, text=str(z))
			lbl5.pack()
			time.sleep(int(inter.get()))
def Fmaj():
	NewWin = Toplevel(window)
	NewWin.geometry('800x800')
	fmaj = ['F','G','A','A#','B','C','D','E']
	t_end = time.time() + 60 * int(dury.get())
	while time.time() < t_end:
		for notes in range(0,6):
			z = random.choice(fmaj)
			lbl5 = Label(NewWin, text=str(z))
			lbl5.pack()
			time.sleep(int(inter.get()))
def Gmaj():
	NewWin = Toplevel(window)
	NewWin.geometry('800x800')
	gmaj = ['G','A','B','C','D','E','F#']
	t_end = time.time() + 60 * int(dury.get())
	while time.time() < t_end:
		for notes in range(0,6):
			z = random.choice(gmaj)
			lbl5 = Label(NewWin, text=str(z))
			lbl5.pack()
			time.sleep(int(inter.get()))
def Amaj():
	NewWin = Toplevel(window)
	NewWin.geometry('800x800')
	amaj = ['A','B','C#','D','E','F#','G#']
	t_end = time.time() + 60 * int(dury.get())
	while time.time() < t_end:
		for notes in range(0,6):
			z = random.choice(amaj)
			lbl5 = Label(NewWin, text=str(z))
			lbl5.pack()
			time.sleep(int(inter.get()))
def Bmaj():
	NewWin = Toplevel(window)
	NewWin.geometry('800x800')
	bmaj = ['B','C#','D#','E','F#','G#','A#',]
	t_end = time.time() + 60 * int(dury.get())
	while time.time() < t_end:
		for notes in range(0,6):
			z = random.choice(bmaj)
			lbl5 = Label(NewWin, text=str(z))
			lbl5.pack()
			time.sleep(int(inter.get()))



#threading the loops
t1 = threading.Thread(target=Cmaj)
t2 = threading.Thread(target=Dmaj) 
t3 = threading.Thread(target=Emaj)
t4 = threading.Thread(target=Fmaj)
t5 = threading.Thread(target=Gmaj)
t6 = threading.Thread(target=Amaj)
t7 = threading.Thread(target=Bmaj)

#Start function
def Start():
	if scales.get() == 'Cmaj' and inter.get() == '':
		lbl3 = Label(window, text='Please set an interval')
		lbl3.place(relx=0.5, rely=0.650, anchor=S,)
	elif dury.get() == '':
		setdur = Label(window, text='Please set a duration in minutes')
		setdur.pack()
	elif scales.get() == 'Cmaj':
		t1.start()
	elif scales.get() == 'Dmaj':
		t2.start()
	elif scales.get() == 'Emaj':
		t3.start()
	elif scales.get() == 'Fmaj':
		t4.start()
	elif scales.get() == 'Gmaj':
		t5.start()
	elif scales.get() == 'Amaj':
		t6.start()
	elif scales.get() == 'Bmaj':
		t7.start()
	else:
		lbl2 = Label(window, text='Please select a scale.')
		lbl2.place(relx=0.5, rely=0.650, anchor=S,)

#Start button
start = Button(window, text='Start', command=Start)
start.place(relx=0.700, rely=0.480,)
window.mainloop()