from tkinter import *

#create window
window = Tk()

#add title to titlebar of window
window.title( 'Window Title' )

#window size (width x height + position-x-coord + position-y-coord)
window.geometry("250x100+500+20")

#create a label
textLabel = Label(window, text="Enter Name:")

#add label to grid
textLabel.grid( row = 1, column = 1, padx = 10, pady=10)

#create a text field
userInput = Entry( window )

#add text field to grid
userInput.grid( row = 1, column = 2, padx = 10, pady=10)


#create a button
myButton = Button(window, text="OK", command=exit)

#add button to grid
myButton.grid( row = 2, column = 2, padx = 10, pady=10)

window.mainloop()
