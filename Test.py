#importing tkinter
from tkinter import *

#creating the main window
root = Tk()

#creating a label
label = Label(root, text="Calculator")

#packing the label
label.pack(side="top")

#creating a frame for entry
entryframe = Frame(root)

#creating a text entry box
entry = Entry(entryframe)

#packing the text entry box
entry.pack(side="left")

#creating a button
button = Button(entryframe, text="Calculate")

#packing the button
button.pack(side="left")

#packing the frame
entryframe.pack(side="top")

#creating the output frame
outputframe = Frame(root)

#creating a label to display output
output = Label(outputframe, text="Output")

#packing the label
output.pack(side="left")

#creating a button to clear the output
clearbutton = Button(outputframe, text="Clear")

#packing the button
clearbutton.pack(side="left")

#packing the frame
outputframe.pack(side="top")

#mainloop
root.mainloop()
