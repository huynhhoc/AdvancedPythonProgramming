import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def solve_equation():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        if a == 0:
            raise ValueError("Hệ số 'a' không thể bằng 0.")
        x = -b / a
        result_var.set(f"x = {x}")
    except ValueError as e:
        messagebox.showerror("Lỗi nhập liệu", str(e))

def reset_fields():
    entry_a.delete(0, tk.END)
    entry_b.delete(0, tk.END)
    result_var.set("")

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Giải phương trình bậc nhất")

# Tạo LabelFrame để chứa các trường nhập liệu
frame = ttk.LabelFrame(root, text="Nhập giá trị cho a và b")
frame.grid(column=0, row=0, padx=10, pady=10)

# Tạo và đặt các nhãn và trường nhập liệu cho 'a' và 'b'
label_a = ttk.Label(frame, text="Nhập giá trị cho a:")
label_a.grid(column=0, row=0, padx=10, pady=5)
entry_a = ttk.Entry(frame)
entry_a.grid(column=1, row=0, padx=10, pady=5)

label_b = ttk.Label(frame, text="Nhập giá trị cho b:")
label_b.grid(column=0, row=1, padx=10, pady=5)
entry_b = ttk.Entry(frame)
entry_b.grid(column=1, row=1, padx=10, pady=5)

# Tạo và đặt nút để giải phương trình
solve_button = ttk.Button(frame, text="Giải", command=solve_equation)
solve_button.grid(column=0, row=2, columnspan=2, pady=10)

# Tạo và đặt nút reset
reset_button = ttk.Button(frame, text="Reset", command=reset_fields)
reset_button.grid(column=0, row=3, columnspan=2, pady=10)

# Tạo và đặt ô hiển thị kết quả
result_var = tk.StringVar()
result_label = ttk.Label(root, textvariable=result_var)
result_label.grid(column=0, row=1, padx=10, pady=10)

# Bắt đầu vòng lặp sự kiện chính
root.mainloop()
