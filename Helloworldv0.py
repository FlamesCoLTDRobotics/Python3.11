import tkinter as tk 
  
# Create a window 
window = tk.Tk() 
  ### stop the maximize button from being enabled
window.resizable(0,0)
# Set window title 
window.title('Hello World') 
  
# Set window size 
window.geometry("200x100")    # Width x Height 
  
# Create a label widget to show the text 'Hello World' on the window 
label = tk.Label(window, text = "Hello World")    # Parameters: (Window, Text)  
  
# Put the label into the window by using grid function of TK class 
label.grid(column = 0, row = 0)    # Parameters: (Column, Row)    									      # Column and Row starts from 0 here.   	                                            # So this will place label at 0th column and 0th row in the window.    	                       # You can increase value of column and row to place it at different position in window.      

   # Run an infinite loop to display the contents of the window continuously until user closes it manually or program ends automatically due to some error or exception occurs within it's scope.       

window.mainloop()