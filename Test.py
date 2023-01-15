from tkinter import *

# Create window
window = Tk()
window.title("Hello World!")
window.geometry('800x600')
window.resizable(width=False, height=False)

# Create label
lbl = Label(window, text="Hello World!")
lbl.pack()

# Run loop
window.mainloop()