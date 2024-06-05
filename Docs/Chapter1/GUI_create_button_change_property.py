import tkinter as tk
from tkinter import ttk

def click_me():
    a_label.configure (foreground='red') 
    a_label.configure(text='A Red Label')
    action.configure(text="** I have been Clicked! **")

if __name__ == '__main__':
    win = tk.Tk()
    win.title("Python GUI")
    a_label = ttk.Label(win, text="A Label")
    a_label.grid(column=0, row=0)
    
    action = ttk.Button(win, text="Click Me!", command=click_me)
    action.grid(column=1, row=0)

    win.mainloop()
    
    

