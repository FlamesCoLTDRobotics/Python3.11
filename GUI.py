
import tkinter

# Create the main window 
root = tkinter.Tk()
root.title('GUI 1.0')

# Create the main container
mainframe = tkinter.Frame(root)
mainframe.pack(fill='both', expand=True)

# Create a text widget 
text_widget = tkinter.Text(mainframe)
text_widget.pack(fill='both', expand=True)
## disable the maximize button
root.resizable(0,0)
# Run the main loop
root.mainloop()