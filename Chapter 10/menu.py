from tkinter import *

#create window
window = Tk()

#create menubar
menubar = Menu(window)

#create menu
filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=filemenu)

#create menu commands
filemenu.add_command(label="New")

#add menu to window
window.config(menu=menubar)


window.mainloop()
