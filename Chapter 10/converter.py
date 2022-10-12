from tkinter import *
from tkinter.ttk import *

def convert():
    if conversions.current() == 0:
        n = float(userInput.get()) * 0.39
        textLabel = Label(window, text=n)
        textLabel.grid( row = 3, column = 4, padx = 10, pady=5)
    elif conversions.current() == 1:
        n = float(userInput.get()) * 2.54
        textLabel = Label(window, text=n)
        textLabel.grid( row = 3, column = 4, padx = 10, pady=5)
    elif conversions.current() == 2:
        n = float(userInput.get()) * 0.62
        textLabel = Label(window, text=n)
        textLabel.grid( row = 3, column = 4, padx = 10, pady=5)
    elif conversions.current() == 3:
        n = float(userInput.get()) * 1.60
        textLabel = Label(window, text=n)
        textLabel.grid( row = 3, column = 4, padx = 10, pady=5)
        
#create window
window = Tk()

#add title to titlebar of window
window.title( 'Unit Converter' )

#window size (width x height + position-x-coord + position-y-coord)
window.geometry("525x180+500+20")

#load image and add to imgLbl label
img = PhotoImage(file="logo.png")
imgLbl = Label(window, image=img)

#add image to grid
imgLbl.grid( row = 1, column = 1, padx = 10, pady=10, columnspan=2, rowspan=3)

#create a label
textLabel = Label(window, text="Convert:")

#add label to grid
textLabel.grid( row = 1, column = 3, padx = 10, pady=10)

#create drop down menu
conversions = Combobox(window, values=[
                                    "Cm to Inch", 
                                    "Inch to Cm",
                                    "Km to Miles",
                                    "Miles to Km"])

#set combobox default selection
conversions.current(0)

#add combo box to grid
conversions.grid( row = 1, column = 4, padx = 10, pady=10)

#create a text field
userInput = Entry( window )

#add text field to grid
userInput.grid( row = 2, column = 4, padx = 10, pady=10)

#add label for result
textLabel = Label(window, text="")

#add result label to grid
textLabel.grid( row = 3, column = 4, padx = 10, pady=5)

#create a button
myButton = Button(window, text="OK", command=convert)

#add button to grid
myButton.grid( row = 2, column = 6, padx = 10, pady=10)

window.mainloop()
