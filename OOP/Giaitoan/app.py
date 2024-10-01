# app.py

import tkinter as tk
from tkinter import Menu
from giaitoan import open_giaitoan_form, main_form

if __name__ == '__main__':
    win = tk.Tk()
    win.title("Main Application")

    # Create a menu bar
    menu_bar = Menu(win)
    win.config(menu=menu_bar)

    # Add File menu
    file_menu = Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="File", menu=file_menu)

    # Add "Giai toan" option to File menu
    file_menu.add_command(label="Giai toan", command= lambda : open_giaitoan_form(win))

    win.mainloop()
