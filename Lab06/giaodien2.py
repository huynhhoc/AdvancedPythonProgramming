from tkinter import *

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def callback(x):
    global num_clicks
    num_clicks = num_clicks +1
    label.configure(text='Phím {} được nhấn. Tổng số click chuột {}'.
                    format(alphabet[x], num_clicks))

num_clicks = 0  # <-- ban đầu là chưa kích chuột
label = Label()
label.grid(row=1, column=0, columnspan=26)
buttons = [0]*26 # create a list to hold 26 buttons
for i in range(26):
    buttons[i] = Button(text=alphabet[i], command = lambda x=i: callback(x))
    buttons[i].grid(row=0, column=i)

mainloop()
