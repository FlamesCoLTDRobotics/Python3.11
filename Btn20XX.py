import tkinter  as tk 
  
# Function for increase number on button click 
def increaseNumber(): 
    global count 
    count = count + 1     # Increase the value of 'count' by 1 
    label.configure(text = str(count))   # Set text of Label as current value of 'count' variable  
    print(increaseNumber)  

     # Create window and set title  
window = tk.Tk()      
window.title("Increment Button")     

	# Create a label to show output      					
label = tk.Label(text="0", font=("Arial Bold", 15))       
label.grid(column=0, row=0)
print(label)

## show it as a 800x800 gui
window.geometry("800x800")
print(window.geometry)
window.resizable(0,0)
window.configure(bg="black")
print(window.configure)

# function for button click  
def clickFunction(): 
    global count
    count = count + 1
    label.configure(text = str(count))
    print(clickFunction)
