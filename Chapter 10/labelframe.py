from tkinter import *

#create window
window = Tk()

#add title to titlebar of window
window.title( 'Window Title' )

#window size (width x height + position-x-coord + position-y-coord)
window.geometry("640x480+500+20")


#create labelframe group
group1 = LabelFrame(window, text="Contact Details", padx=5, pady=5)

#create widgets and add to group
textLabel = Label(group1, text="Name: ")
name = Entry(group1)


#add widgets to your window
group1.pack(padx=10, pady=10)
textLabel.pack(side=LEFT)
name.pack(side=RIGHT)

window.mainloop()
