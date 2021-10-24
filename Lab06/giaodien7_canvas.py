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
import random  # <-- thư viện ngẫu nhiên
xmove = 0
ymove = 0
while (xmove == 0):  # để tránh đi thẳng hoặc đứng yên
    xmove = random.randrange(6) -6 # <-- thì giá trị dịch chuyển x sẽ là 1 trong 3: -1 hoặc 0 hoặc 1
while (ymove == 0): # để tránh đi thẳng hoặc đứng yên
    ymove = random.randrange(6) -6 # <-- tương tự giá trị của y

def kiemtra(tamx, tamy, bkx, bky, width, height):
    ketqua = True
    if (tamx + bkx <= 1) or (tamx + bkx > width-1):
        ketqua = False # nghĩa là sai (vị trí x vượt quá khuôn Canvas)
    if (tamy + bky <= 1) or (tamy + bky > height-1):
        ketqua = False # nghĩa là sai (vị trí y vượt quá khuôn Canvas)
    return ketqua

import time
while (1==1):
    # kiểm tra vị trí bóng xem có vượt màn hình không
    if kiemtra(tamX, tamY, bankinh, bankinh, dai, cao) == False:  # thì phải tính lại vị trí quả bóng
        # nghĩa là chúng ta phải tính toán quả bóng nảy ra
        # Giả sử chọn 1 cách nảy bóng bằng vector vuông góc với vector chuyển động
        xmove, ymove = -ymove, xmove
        tamX = tamX + xmove
        tamY = tamY + ymove
    else:
        tamX = tamX + xmove
        tamY = tamY + ymove

    canvas.delete(bong)
    time.sleep(0.1)
    bong = canvas.create_oval(0,0, 2*bankinh,2 * bankinh)
    canvas.itemconfigure(bong, fill='red')
    canvas.coords(bong, tamX - bankinh, tamY - bankinh, tamX + bankinh, tamY + bankinh)
    canvas.update()

mainloop()
