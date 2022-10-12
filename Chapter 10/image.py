from tkinter import *

#create window
window = Tk()

#add title to titlebar of window
window.title( 'Window Title' )

#window size (width x height + position-x-coord + position-y-coord)
window.geometry("640x480+500+20")

myCanvas = Canvas(window, bg="blue", height=300, width=300)

#load image
img = PhotoImage(file="rocket.png")

#resize to a 6th of the original size
img = PhotoImage.subsample(img, x=6, y=6)

#paste image on canvas at co-ords (x=20, y=60)
myCanvas.create_image(20,60, anchor=NW, image=img) 

myCanvas.pack()
window.mainloop()
