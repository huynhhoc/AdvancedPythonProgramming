from tkinter import *
root = Tk()
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

button_frame = Frame()
buttons = [0]*26   # tạo 26 button

for i in range(26):
    buttons[i] = Button(button_frame, text=alphabet[i])
    buttons[i].grid(row=0, column=i)
    
ok_button = Button(text='Ok', font=('Verdana', 24))

button_frame.grid(row=0, column=0)
ok_button.grid(row=1, column=0)

mainloop()
