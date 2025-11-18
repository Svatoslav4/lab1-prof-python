import tkinter as tk


def draw_circle():
    """Малює коло в центрі полотна."""
    # Отримуємо розміри полотна
    canvas_width = canvas.winfo_width()
    canvas_height = canvas.winfo_height()

    # Визначаємо координати центру та радіус
    center_x = canvas_width // 2
    center_y = canvas_height // 2
    radius = 30

    # Малюємо овал (коло)
    # Координати: (x1, y1) - верхній лівий кут, (x2, y2) - нижній правий кут bounding box
    canvas.create_oval(
        center_x - radius, center_y - radius,
        center_x + radius, center_y + radius,
        fill="blue", outline="darkblue"
    )


def clear_canvas():
    """Очищує все намальоване на полотні."""
    canvas.delete("all")


# Створення головного вікна
root = tk.Tk()
root.title("Canvas with Circle and Clear")

# Створення фрейму для кнопок
button_frame = tk.Frame(root)
button_frame.pack(side=tk.TOP, fill=tk.X)

# Створення кнопки "Draw Circle"
circle_button = tk.Button(button_frame, text="Draw Circle", command=draw_circle)
circle_button.pack(side=tk.LEFT, padx=5, pady=5)

# Створення кнопки "Clear Canvas"
clear_button = tk.Button(button_frame, text="Clear Canvas", command=clear_canvas)
clear_button.pack(side=tk.LEFT, padx=5, pady=5)

# Створення полотна (Canvas widget)
canvas = tk.Canvas(root, bg="white", width=400, height=300)
canvas.pack(expand=True, fill='both')

# Приклад початкового малювання (опціонально)
canvas.create_text(200, 150, text="Click 'Draw Circle' or 'Clear Canvas'", fill="gray")

# Запуск головного циклу подій
root.mainloop()