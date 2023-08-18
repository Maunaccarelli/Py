import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext, font

def open_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        with open(file_path, 'r') as file:
            text.delete('1.0', tk.END)
            text.insert(tk.END, file.read())

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt")
    if file_path:
        with open(file_path, 'w') as file:
            file.write(text.get('1.0', tk.END))
            messagebox.showinfo("Guardado", "El archivo se ha guardado exitosamente.")

def clear_text():
    text.delete('1.0', tk.END)

def change_font():
    font_name = font_var.get()
    text.configure(font=(font_name, font_size_var.get()))

root = tk.Tk()
root.title("Editor de Texto con Fuentes")

text = scrolledtext.ScrolledText(root, wrap=tk.WORD, undo=True)
text.pack(fill=tk.BOTH, expand=True)

menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Archivo", menu=file_menu)
file_menu.add_command(label="Abrir archivo", command=open_file)
file_menu.add_command(label="Guardar archivo", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Salir", command=root.quit)

edit_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Editar", menu=edit_menu)
edit_menu.add_command(label="Deshacer", command=text.edit_undo)
edit_menu.add_command(label="Rehacer", command=text.edit_redo)
edit_menu.add_separator()
edit_menu.add_command(label="Limpiar", command=clear_text)

font_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Fuente", menu=font_menu)
font_var = tk.StringVar(value="Arial")
font_menu.add_radiobutton(label="Arial", variable=font_var, command=change_font)
font_menu.add_radiobutton(label="Courier New", variable=font_var, command=change_font)
font_menu.add_radiobutton(label="Times New Roman", variable=font_var, command=change_font)

font_size_var = tk.IntVar(value=12)
font_size_menu = tk.Menu(font_menu, tearoff=0)
font_menu.add_cascade(label="Tamaño de Fuente", menu=font_size_menu)
font_size_menu.add_radiobutton(label="10", variable=font_size_var, command=change_font)
font_size_menu.add_radiobutton(label="12", variable=font_size_var, command=change_font)
font_size_menu.add_radiobutton(label="14", variable=font_size_var, command=change_font)

root.mainloop()