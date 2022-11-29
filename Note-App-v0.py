# write a text editor
print("Welcome to GPT-X")
print("Enter your notes below")
import tkinter as tk
## write a 800x800 window
window = tk.Tk()
window.resizable(0,0)
window.title('Notepad v0.1x')
window.geometry("800x800")
label = tk.Label(window, text = "Enter your notes below")
label.grid(column = 0, row = 0)
window.mainloop()
# write a text editor
print("Welcome to GPT-X")
print("Enter your notes below")
# write a save button
def save():
    print("Saved!")
    ## make a algorthim for a save button
    def savefiledialog ():
        import tkinter as tk
        from tkinter import filedialog
        root = tk.Tk()
        root.withdraw()
        file_path = filedialog.asksaveasfilename()
        print(file_path)
        return file_path
    savefiledialog()
    ## draw the save button on the right side of the screen
    import tkinter as tk
    window = tk.Tk()
    window.resizable(0,0)
    window.title('Notepad v0.1x')
    window.geometry("800x800")
    label = tk.Label(window, text = "Enter your notes below")
    label.grid(column = 0, row = 0)
    button = tk.Button(window, text = "Save", command = save)
    button.grid(column = 1, row = 0)
    window.mainloop()
    ## write a gui that gets input
    def get_input():
        import tkinter as tk
        window = tk.Tk()
        window.resizable(0,0)
        window.title('Notepad v0.1x')
        window.geometry("800x800")
        label = tk.Label(window, text = "Enter your notes below")
        label.grid(column = 0, row = 0)
        button = tk.Button(window, text = "Save", command = save)
        button.grid(column = 1, row = 0)
        entry = tk.Entry(window)
        entry.grid(column = 0, row = 1)
        window.mainloop()
        return entry.get()
    ## write a gui that gets input
    def get_input():
        import tkinter as tk
        window = tk.Tk()
        window.resizable(0,0)
        window.title('Notepad v0.1x')
        window.geometry("800x800")
        label = tk.Label(window, text = "Enter your notes below")
        label.grid(column = 0, row = 0)
        button = tk.Button(window, text = "Save", command = save)
        button.grid(column = 1, row = 0)
        entry = tk.Entry(window)
        entry.grid(column = 0, row = 1)
        window.mainloop()
        return entry.get()