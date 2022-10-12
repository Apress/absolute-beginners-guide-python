from tkinter import *

#create window
window = Tk()

#add title to titlebar of window
window.title( 'Window Title' )

#window size (width x height + position-x-coord + position-y-coord)
window.geometry("640x480+500+20")

textLabel = Label(window, text="Enter Name:")

textLabel.pack()

window.mainloop()
