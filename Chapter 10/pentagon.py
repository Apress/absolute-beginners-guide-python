from tkinter import *

#create window
window = Tk()

#add title to titlebar of window
window.title( 'Window Title' )

#window size (width x height + position-x-coord + position-y-coord)
window.geometry("640x480+500+20")

myCanvas = Canvas(window, bg="blue", height=300, width=300)

pent = myCanvas.create_polygon(100,150, 52,185, 71,240, 129,240, 148,185, fill="lime green")


myCanvas.pack()
window.mainloop()
