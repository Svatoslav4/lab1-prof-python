import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox


def save_file():
    """Відкриває діалогове вікно для збереження файлу та записує вміст текстового поля."""
    # Відкриває діалогове вікно "Зберегти як"
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
    )

    if file_path:
        try:
            # Отримує весь текст із текстового поля
            text_to_save = text_area.get("1.0", tk.END)
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(text_to_save)
            messagebox.showinfo("Success", f"File saved successfully to:\n{file_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save file: {e}")


# Створення головного вікна
root = tk.Tk()
root.title("Simple Text Editor with Save")

# Створення меню
menubar = tk.Menu(root)
root.config(menu=menubar)

# Створення підменю File
file_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=file_menu)

# Додавання кнопки "Save" до підменю File
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# Створення текстового поля (Text widget)
text_area = tk.Text(root, wrap='word')  # wrap='word' для перенесення слів
text_area.pack(expand=True, fill='both')

# Додавання початкового тексту
text_area.insert(tk.END, "Enter your text here...")

# Запуск головного циклу подій
root.mainloop()