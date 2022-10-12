from tkinter import *
from tkinter import messagebox


def dialog() :
        if box1Checked.get() == 1:
                messagebox.showinfo( 'Message Box' , "Red" )
        if box2Checked.get() == 1:
                messagebox.showinfo( 'Message Box' , "Green" )
        if box3Checked.get() == 1:
                messagebox.showinfo( 'Message Box' , "Blue" )
        
		
#create window
window = Tk()

#add title to titlebar of window
window.title( 'Window Title' )

#window size (width x height + position-x-coord + position-y-coord)
window.geometry("640x480+500+20")


#create variable to assign 'onvalue' if checked
box1Checked = IntVar()
box2Checked = IntVar()
box3Checked = IntVar()

#create checkboxes
box1 = Checkbutton(window, text="Red", variable=box1Checked, onvalue=1)
box2 = Checkbutton(window, text="Green", variable=box2Checked, onvalue=1)
box3 = Checkbutton(window, text="Blue", variable=box3Checked, onvalue=1)

#add checkboxes to window
box1.pack()
box2.pack()
box3.pack()


#create a button
myButton = Button(window, text="Click Me", command=dialog)

#add button to window
myButton.pack(padx=20, pady=20)

window.mainloop()
