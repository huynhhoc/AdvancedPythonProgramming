from tkinter import *

def calculate():
    temp = int(entry.get())
    temp = 9/5*temp+32
    output_label.configure(text = 'Tính ra độ C: {:.1f}'.format(temp))  # thay đổi nội dung
    entry.delete(0,END)  # xóa entry từ vị trí đầu (0) đến cuối

root = Tk()
# Label là 1 nhãn
message_label = Label(text='Nhập nhiệt độ F', font=('Verdana', 16), bg='blue', fg='white')
output_label = Label(font=('Verdana', 16))  # <-- label này khi tạo chưa có text
# Entry là 1 chỗ để nhập liệu (TextBox)
entry = Entry(font=('Verdana', 16), width=4)
# Button
calc_button = Button(text='Tính toán', font=('Verdana', 16), command=calculate)

### bố trí thành 2 dòng
message_label.grid(row=0, column=0)
entry.grid(row=0, column=1)
calc_button.grid(row=0, column=2)
output_label.grid(row=1, column=0, columnspan=3)

mainloop()
