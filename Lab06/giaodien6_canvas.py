from tkinter import *

dai = 400
cao = 400

canvas = Canvas(width=dai, height=cao, bg='white')

root = Tk()
canvas.grid(row = 0, column = 0)

# vẽ hình quả bóng
bankinh = 10
bong = canvas.create_oval(0,0, 2*bankinh,2 * bankinh)  # bán kính của quả bóng là 10
# tô màu đỏ
canvas.itemconfigure(bong, fill='red')
# đưa tọa độ thành:
tamX = dai /2
tamY = cao/2
canvas.coords(bong, tamX - bankinh, tamY - bankinh, tamX + bankinh, tamY + bankinh)

mainloop()
