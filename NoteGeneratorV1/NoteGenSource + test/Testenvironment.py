from tkinter import *
from tkinter.ttk import *

#.pack This geometry manager organizes widgets in blocks before placing them in the parent widget.


test = Tk()
test.geometry('400x400')
txt = Entry(test, width=10)
txt.pack()
txt.focus()

#.get() uses the input from the user
#.strip() to negate extra spaces in text
def Enter():
	if txt.get().strip().lower() == 'print':
		lbl = Label(test, text='Hello World!')
		lbl.pack()
	else:
		lbl2 = Label(test, text='None')
		lbl2.pack()

btn = Button(test, text='Submit', command=Enter)
btn.pack()
comboExample = Combobox(values=["January", 'February', 'March']) 
                                    
                            
comboExample.pack()
comboExample.current(1)

test.mainloop()



