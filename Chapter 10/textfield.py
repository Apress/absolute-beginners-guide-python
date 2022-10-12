from tkinter import *
from tkinter import messagebox


def dialog() :
        messagebox.showinfo( 'Message Box' , userInput.get() )

		
#create window
window = Tk()

#add title to titlebar of window
window.title( 'Window Title' )

#window size (width x height + position-x-coord + position-y-coord)
window.geometry("640x480+500+20")


#create a text field
userInput = Entry( window )


#create a button
myButton = Button(window, text="Click Me", command=dialog)

#add button to window
myButton.pack(padx=20, pady=20)


#add text field to window
userInput.pack()


window.mainloop()
