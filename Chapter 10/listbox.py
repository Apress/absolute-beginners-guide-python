from tkinter import *
from tkinter import messagebox


def dialog() :
        selectedItem = list.curselection()
        messagebox.showinfo( 'Message Box' , list.get(selectedItem) )

		
#create window
window = Tk()

#add title to titlebar of window
window.title( 'Window Title' )

#window size (width x height + position-x-coord + position-y-coord)
window.geometry("640x480+500+20")


#create a list box
list = Listbox(window)
list.insert(1, 'Item One')
list.insert(2, 'Item Two')
list.insert(3, 'Item Three')
list.insert(4, 'Item Four')


#create a button
myButton = Button(window, text="Click Me", command=dialog)


#add listbox to window
list.pack(padx=20, pady=20)


#add button to window
myButton.pack(padx=20)

window.mainloop()
