# giaitoan.py

import tkinter as tk
from tkinter import ttk
from mathematic import Mathematic

mathematic = Mathematic()

def perform_operation(operation):
    global a
    global b
    global ketqua
    try:
        a_val = float(a.get())
        b_val = float(b.get())
        result = mathematic.execute(a_val, b_val, operation)
        ketqua.set(result)
    except ValueError as ve:
        ketqua.set("Error: " + str(ve))

def main_form():
    win = tk.Tk()
    win.title("Example")
    return win
def open_giaitoan_form(win):
    global a
    global b
    global ketqua
    
    tabControl = ttk.Notebook(win)
    tab1 = ttk.Frame(tabControl)
    tabControl.add(tab1, text="Nhom 1")
    tab2 = ttk.Frame(tabControl)
    tabControl.add(tab2, text="Nhom 2")

    tabControl.pack(expand=1, fill='both')

    frame = ttk.LabelFrame(tab1, text=" Tham so ")
    frame.grid(column=0, row=0, padx=10, pady=10)

    # Label a and b
    ttk.Label(frame, text="He so a: ").grid(column=0, row=0, padx=5, pady=5)
    ttk.Label(frame, text="He so b: ").grid(column=0, row=1, padx=5, pady=5)

    # Entry
    
    a = tk.StringVar()
    texta = ttk.Entry(frame, textvariable=a)
    texta.grid(column=1, row=0)

    # Entry b
    b = tk.StringVar()
    textb = ttk.Entry(frame, textvariable=b)
    textb.grid(column=1, row=1)

    fraction = tk.LabelFrame(tab1, text="Phep toan")
    fraction.grid(column=2, row=0, padx=10, pady=10)
    cong = ttk.Button(fraction, text="+", command= lambda: perform_operation('add'))
    tru = ttk.Button(fraction, text="-", command=lambda: perform_operation('subtract'))
    cong.grid(column=0, row=0, padx=5, pady=5)
    tru.grid(column=0, row=1, padx=5, pady=5)
    
    ketqua = tk.StringVar()
    ketqua_lb = ttk.Label(tab1, textvariable=ketqua)
    ketqua_lb.grid(column=0, row=3)

if __name__ == '__main__':
    win = main_form()
    open_giaitoan_form(win)
    win.mainloop()
