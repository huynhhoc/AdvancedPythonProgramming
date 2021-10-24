from tkinter import *

def b1_event(event):
    import time
    canvas.delete(ALL)
    # vẽ hình quả bóng
    bankinh = 10
    bong = canvas.create_oval(0,0, 2*bankinh,2 * bankinh)  # bán kính của quả bóng là 10
    # tô màu đỏ
    canvas.itemconfigure(bong, fill='red')
    # đưa tọa độ thành:
    tamX = dai /2
    tamY = cao/2
    vitrix_bong = event.x
    vitriy_bong = event.y
    canvas.coords(bong, vitrix_bong - bankinh, vitriy_bong - bankinh,
                                        vitrix_bong + bankinh, vitriy_bong + bankinh)
    import random  # <-- thư viện ngẫu nhiên
    xmove = 0
    ymove = 0
    while (xmove == 0):  # để tránh đi thẳng hoặc đứng yên
        xmove = random.randrange(6) -6 # <-- thì giá trị dịch chuyển x sẽ là 1 trong 3: -1 hoặc 0 hoặc 1
    while (ymove == 0): # để tránh đi thẳng hoặc đứng yên
        ymove = random.randrange(6) -6 # <-- tương tự giá trị của y    
    while (1==1):
        # kiểm tra vị trí bóng xem có vượt màn hình không
        if kiemtra(vitrix_bong, vitriy_bong, bankinh, bankinh, dai, cao) == False:  # thì phải tính lại vị trí quả bóng
            # nghĩa là chúng ta phải tính toán quả bóng nảy ra
            # Giả sử chọn 1 cách nảy bóng bằng vector vuông góc với vector chuyển động
            xmove, ymove = -ymove, xmove
            vitrix_bong = vitrix_bong + xmove
            vitriy_bong = vitriy_bong + ymove
        else:
            vitrix_bong = vitrix_bong + xmove
            vitriy_bong = vitriy_bong + ymove

        canvas.delete(bong)
        time.sleep(0.1)
        bong = canvas.create_oval(0,0, 2*bankinh,2 * bankinh)
        canvas.itemconfigure(bong, fill='red')
        canvas.coords(bong, vitrix_bong - bankinh, vitriy_bong - bankinh,
                                            vitrix_bong + bankinh, vitriy_bong + bankinh)
        canvas.update()

root = Tk()
dai = 400
cao = 400
canvas = Canvas(width=dai, height=cao, bg='white')

# kích chuột ở canvas thì sẽ xử lý hàm b1_event
canvas.bind('<ButtonPress-1>', b1_event)   # gắn hàm kích chuột vào canvas, nghĩa là khi

canvas.grid(row = 0, column = 0)

def kiemtra(tamx, tamy, bkx, bky, width, height):
    ketqua = True
    if (tamx + bkx <= 1) or (tamx + bkx > width-1):
        ketqua = False # nghĩa là sai (vị trí x vượt quá khuôn Canvas)
    if (tamy + bky <= 1) or (tamy + bky > height-1):
        ketqua = False # nghĩa là sai (vị trí y vượt quá khuôn Canvas)
    return ketqua


mainloop()
