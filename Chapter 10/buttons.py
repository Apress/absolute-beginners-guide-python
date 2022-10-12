from tkinter import *	

#create window
window = Tk()

#add title to titlebar of window
window.title( 'Window Title' )

#window size (width x height + position-x-coord + position-y-coord)
window.geometry("640x480+500+20")


#create a button
myButton = Button(window, text="Exit", command=exit)

#add button to window
myButton.pack()



window.mainloop()
