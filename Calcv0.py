import tkinter as tk

root = tk.Tk() 
root.title("Hello world!") 
root.geometry('800x600') 
root.resizable(width=False, height=False)   #maximize button disabled 

# Create a label widget of width 25 columns and 2 lines (use wraplength to limit text per line): 
lbl = tk.Label(master=root,text="Hello world!", wraplength=25*25)   # set wrapping for long strings/words - wrap every 25 characters by default in this case  
lbl.pack()   # pack the widgets so it displays on the main window

# Create a quit button
quit_button = tk.Button(root, text="Quit", command=root.destroy)
quit_button.pack()

root.mainloop()
