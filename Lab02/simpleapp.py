import tkinter as tk
from tkinter import filedialog, messagebox

def new_file():
    if messagebox.askokcancel("New", "Do you want to save the current file?"):
        save_file()
    text_area.delete(1.0, tk.END)

def open_file():
    file_path = filedialog.askopenfilename(defaultextension=".txt",
                                           filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        text_area.delete(1.0, tk.END)
        with open(file_path, "r") as file:
            text_area.insert(tk.END, file.read())

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                             filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, "w") as file:
            file.write(text_area.get(1.0, tk.END))

# Create the main application window
root = tk.Tk()
root.title("Simple Text Editor")
root.geometry("600x400")

# Add a Text widget
text_area = tk.Text(root, wrap='word')
text_area.pack(expand=1, fill='both')

# Create a menu bar
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# Add File menu to the menu bar
file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# Add Edit menu to the menu bar
edit_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command=lambda: text_area.event_generate("<<Cut>>"))
edit_menu.add_command(label="Copy", command=lambda: text_area.event_generate("<<Copy>>"))
edit_menu.add_command(label="Paste", command=lambda: text_area.event_generate("<<Paste>>"))

# Run the application
root.mainloop()
