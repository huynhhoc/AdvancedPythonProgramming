from tkinter import *

def callback(r,c):
    global player
    
    if player == 'X' and states[r][c] == 0 and stop_game==False:
        b[r][c].configure(text = 'X')
        states[r][c] = 'X'
        player = 'O'
    if player == 'O' and states[r][c] == 0 and stop_game==False:
        b[r][c].configure(text = 'O')
        states[r][c] = '0'
        player = 'X'

    kiemtra_chienthang()

def kiemtra_chienthang():
    global stop_game
    for i in range(3):  # nếu 1 trong các dòng có cùng giá trị
        if states[i][0]==states[i][1]==states[i][2]!=0:
            b[i][0].configure(bg='grey')
            b[i][1].configure(bg='grey')
            b[i][2].configure(bg='grey')
            stop_game = True
            
    for i in range(3): # nếu 1 trong các cột có cùng giá trị
        if states[0][i]==states[1][i]==states[2][i]!=0:
            b[0][i].configure(bg='grey')
            b[1][i].configure(bg='grey')
            b[2][i].configure(bg='grey')
            stop_game = True

    if states[0][0]==states[1][1]==states[2][2]!=0:  # kiểm tra đường chéo chính \
        b[0][0].configure(bg='grey')
        b[1][1].configure(bg='grey')
        b[2][2].configure(bg='grey')
        stop_game = True

    if states[2][0]==states[1][1]==states[0][2]!=0: # kiểm tra đường chéo ngược lại /
        b[2][0].configure(bg='grey')
        b[1][1].configure(bg='grey')
        b[0][2].configure(bg='grey')
        stop_game = True

root = Tk()

b = [[0,0,0],
        [0,0,0],
        [0,0,0]]

states = [[0,0,0], [0,0,0],  [0,0,0]]  # đây là trạng thái

for i in range(3):
    for j in range(3):
        b[i][j] = Button(font=('Verdana', 56), width=3, bg='yellow',
                                    command = lambda r=i,c=j: callback(r,c))
        b[i][j].grid(row = i, column = j)

player = 'X'
stop_game = False   # ban đầu là false
mainloop()  #  <--- đây là lệnh để bắt đầu chạy
