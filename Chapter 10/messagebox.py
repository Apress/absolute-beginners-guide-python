from tkinter import *
from tkinter import messagebox



def dialog() :
	response = messagebox.askquestion( 'Message Box' , 'Do you want to proceed?' )
	if response == 'yes' :
		messagebox.showinfo( 'Message Box', 'Proceeding...' )
	else :
		messagebox.showwarning( 'Message Box', 'Canceling...' )

		

#create window
window = Tk()

#add title to titlebar of window
window.title( 'Window Title' )

#window size (width x height + position-x-coord + position-y-coord)
window.geometry("640x480+500+20")



#create a button
myButton = Button(window, text="Click Me", command=dialog)

#add button to window
myButton.pack()



window.mainloop()
