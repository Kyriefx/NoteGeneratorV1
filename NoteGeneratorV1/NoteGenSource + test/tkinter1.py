from tkinter import *

window = Tk() #This creates the main application window

window.geometry('600x600') #Sets the default window size

#Sets the title for the window
window.title('Practice nigga')

#Crating a variable that contains a label widget
lbl1 = Label(window, text='Hello', font=("Arial Bold", 50)) 

lbl1.grid(column=0, row=0) #Label positioning

#Recieve input using entry class
txt = Entry(window, width=10)
txt.grid(column=0, row=1)

#Set Focus to entry wdiget
#focus means it'd be the first thing "clicked" upon opening
txt.focus()

#Disabling entry wdiget
txt2 = Entry(window, width=10, state='disabled')
txt2.grid(column=1, row=1)

#Adding a button 
#Create a variable and label it as a button
btn = Button(window, text='Click Me')
btn.grid(column=1, row=0)

#Creates a Second button but with background(bg) and foreground(fg) colors
btn2 = Button(window, text='Click Me Too', bg='orange', fg='red')
btn2.grid(column=2, row=0)

#Creating a third button that accepts a COMMAND
def clicked():
  btn3.configure(text='Button was clicked!!')
btn3 = Button(window, text='Click me 3!', bg='black', fg= 'white', command=clicked)
btn3.grid(column=3, row=0)


#This is the mainloop that keeps the windows open as it waits for human interaction ALWAYS KEEP THIS AT THE BOTTOM
window.mainloop() 



#Note that the font parameter can be passed to any widget to change its font not labels only.