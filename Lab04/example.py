import tkinter as tk
from tkinter import ttk, Menu, messagebox

def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operation = operation_var.get()

        if operation == "Add":
            result = num1 + num2
        elif operation == "Subtract":
            result = num1 - num2
        elif operation == "Multiply":
            result = num1 * num2
        elif operation == "Divide":
            if num2 != 0:
                result = num1 / num2
            else:
                messagebox.showerror("Error", "Cannot divide by zero")
                return
        else:
            result = "Unknown operation"
        
        if show_result.get():
            messagebox.showinfo("Result", f"The result is: {result}")
        
        result_var.set(result)
    except ValueError:
        messagebox.showerror("Error", "Invalid input")

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Create menu bar
menu_bar = Menu(root)
root.config(menu=menu_bar)

# Add a menu
file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Exit", command=root.quit)

# Entry widgets for numbers
ttk.Label(root, text="Number 1:").grid(column=0, row=0, padx=10, pady=10)
entry1 = ttk.Entry(root)
entry1.grid(column=1, row=0, padx=10, pady=10)

ttk.Label(root, text="Number 2:").grid(column=0, row=1, padx=10, pady=10)
entry2 = ttk.Entry(root)
entry2.grid(column=1, row=1, padx=10, pady=10)

# Radio buttons for operations
operation_var = tk.StringVar()
operation_var.set("Add")

ttk.Label(root, text="Operation:").grid(column=0, row=2, padx=10, pady=10)
ttk.Radiobutton(root, text="Add", variable=operation_var, value="Add").grid(column=1, row=2, padx=10, pady=5)
ttk.Radiobutton(root, text="Subtract", variable=operation_var, value="Subtract").grid(column=1, row=3, padx=10, pady=5)
ttk.Radiobutton(root, text="Multiply", variable=operation_var, value="Multiply").grid(column=1, row=4, padx=10, pady=5)
ttk.Radiobutton(root, text="Divide", variable=operation_var, value="Divide").grid(column=1, row=5, padx=10, pady=5)

# Checkbox for showing result in a messagebox
show_result = tk.BooleanVar()
ttk.Checkbutton(root, text="Show result in popup", variable=show_result).grid(column=0, row=6, columnspan=2, pady=10)

# Result label
result_var = tk.StringVar()
ttk.Label(root, text="Result:").grid(column=0, row=7, padx=10, pady=10)
result_label = ttk.Label(root, textvariable=result_var)
result_label.grid(column=1, row=7, padx=10, pady=10)

# Calculate button
calculate_button = ttk.Button(root, text="Calculate", command=calculate)
calculate_button.grid(column=0, row=8, columnspan=2, pady=10)

# Run the application
root.mainloop()
