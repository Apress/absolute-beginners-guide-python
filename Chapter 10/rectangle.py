from tkinter import *

#create window
window = Tk()

#add title to titlebar of window
window.title( 'Window Title' )

#window size (width x height + position-x-coord + position-y-coord)
window.geometry("640x480+500+20")

myCanvas = Canvas(window, bg="blue", height=300, width=300)

rect = myCanvas.create_rectangle(100, 100, 25, 50, fill="yellow")



myCanvas.pack()
window.mainloop()
