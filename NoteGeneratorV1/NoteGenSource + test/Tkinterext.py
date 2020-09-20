#Making a combo box
from tkinter import *
from tkinter.ttk import*

window = Tk() #creates the window

window.title('Practice Ext') #Sets title of window

selected = IntVar() 

window.geometry('600x600') #Setting the size of the window

#Combobox = a type of dialogue box containing a combination of controls, 
#such as sliders, text boxes, and drop-down lists.
#Create a variable for said combobox
combo = Combobox() #Combobox is created inside of window
combo['values']= (1,2,3,4,5, 'Text') #This sets the values inside of the combobox
combo.current(0) #Sets the selected item
combo.grid(column=0, row=0)

#Add a checkbutton widget
chk = Checkbutton(window, text='Choose')
chk_state = BooleanVar() #Accepts True or False or you can use IntVar (1,0s)
chk_state.set(False) #Sets the check state #False means the box will be unchecked

chk = Checkbutton(window, text='Choose', var=chk_state)
chk.grid(column=1, row=1)

#Get Radio button value (selected button)
def clicked():
	print(selected.get())

btn = Button(window, text='Submit', command=clicked)
btn.grid(column=5, row=5)

#Add Radio buttons Widgets
#Create the variable for your button
rad1 = Radiobutton(window, text='First', value=1, variable=selected)
#Note that you should set the value for every radio button with a different value, otherwise, they won’t work.
rad2 = Radiobutton(window, text='Second', value=2, variable=selected)
rad3 = Radiobutton(window, text='Third', value=3, variable=selected)
rad1.grid(column=2, row=0)
rad2.grid(column=3, row=0)
rad3.grid(column=4, row=0)

#Use the command= to perform a specific function, so if the user clicks on any of them it executes the code
def test():
	print('Hello World!')
rad4 = Radiobutton(window, text='Fourth', value=4, command=test, variable=selected) #The output appears in the command line
rad4.grid(column=5, row=0)

window.mainloop() #Loops the window, waits for user input