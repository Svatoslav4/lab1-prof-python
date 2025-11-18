import tkinter as tk
from tkinter import colorchooser, simpledialog, Menu, Toplevel, Label, Button, Scale, HORIZONTAL, W, E


# --- 1. Клас для управління станом налаштувань ---
class Settings:
    """Зберігає налаштування для трьох фігур і їхнього тексту."""

    def __init__(self):
        # Налаштування фігур: [Колір, Розмір (коефіцієнт)]
        self.figure_settings = {
            "Rectangle": {"color": "red", "size": 1.0},
            "Circle": {"color": "blue", "size": 1.0},
            "Triangle": {"color": "green", "size": 1.0},
        }
        # Налаштування тексту: [Колір, Розмір шрифту]
        self.text_settings = {
            "Rectangle": {"color": "black", "size": 12},
            "Circle": {"color": "black", "size": 12},
            "Triangle": {"color": "black", "size": 12},
        }


# --- 2. Головний клас Додатка ---
class GeometryApp:
    def __init__(self, master):
        self.master = master
        master.title("Лабораторна 11: Геометричні Фігури")

        self.settings = Settings()
        self.figure_names = list(self.settings.figure_settings.keys())

        # Створення полотна
        self.canvas = tk.Canvas(master, bg="white", width=600, height=400)
        self.canvas.pack(pady=10, padx=10, expand=True, fill='both')

        # Ініціалізація меню
        self.setup_menu()

        # Початкове малювання
        self.draw_figures()

    # ----------------- Меню та Діалогові Вікна -----------------

    def setup_menu(self):
        """Створює головне меню та підпункти Налаштування."""
        menubar = Menu(self.master)
        self.master.config(menu=menubar)

        # Пункт Налаштування
        settings_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Налаштування", menu=settings_menu)

        # Підпункти
        settings_menu.add_command(label="Налаштування зображень", command=self.open_figure_settings)
        settings_menu.add_command(label="Налаштування тексту", command=self.open_text_settings)

    def open_figure_settings(self):
        """Створює діалогове вікно для налаштування кольору та розміру фігур."""
        FigureSettingsDialog(self.master, self.settings, self.draw_figures)

    def open_text_settings(self):
        """Створює діалогове вікно для налаштування кольору та розміру тексту."""
        TextSettingsDialog(self.master, self.settings, self.draw_figures)

    # ----------------- Функція Малювання -----------------

    def draw_figures(self):
        """Очищує полотно і перемальовує фігури відповідно до поточних налаштувань."""
        self.canvas.delete("all")

        w, h = self.canvas.winfo_width(), self.canvas.winfo_height()
        if w == 1 and h == 1:  # Запобігання помилці при першому запуску
            w, h = 600, 400

        x_step = w / 4
        y_center = h / 2

        # Базові розміри
        base_size = 50

        for i, name in enumerate(self.figure_names):
            fig_set = self.settings.figure_settings[name]
            text_set = self.settings.text_settings[name]

            x = x_step * (i + 1)
            size = base_size * fig_set["size"]
            color = fig_set["color"]

            # Малювання фігури
            if name == "Rectangle":
                self.canvas.create_rectangle(
                    x - size, y_center - size / 2,
                    x + size, y_center + size / 2,
                    fill=color, tags=name
                )
            elif name == "Circle":
                self.canvas.create_oval(
                    x - size, y_center - size,
                    x + size, y_center + size,
                    fill=color, tags=name
                )
            elif name == "Triangle":
                # Координати трикутника: (верхня точка, нижня ліва, нижня права)
                points = [x, y_center - size, x - size, y_center + size, x + size, y_center + size]
                self.canvas.create_polygon(points, fill=color, tags=name)

            # Малювання тексту
            font_size = text_set["size"]
            font_color = text_set["color"]
            self.canvas.create_text(
                x, y_center - size - 20,
                text=name,
                fill=font_color,
                font=("Arial", font_size, "bold"),
                tags=f"{name}_text"
            )


# --- 3. Клас Діалогового Вікна Налаштування Зображень ---
class FigureSettingsDialog(Toplevel):
    def __init__(self, master, settings, redraw_callback):
        super().__init__(master)
        self.title("Налаштування зображень")
        self.settings = settings
        self.redraw_callback = redraw_callback
        self.grab_set()  # Блокування головного вікна

        self.fig_frames = {}
        self.size_vars = {}

        self.create_widgets()

    def create_widgets(self):
        """Створює елементи керування для кожної фігури."""
        for i, name in enumerate(self.settings.figure_settings):
            frame = Label(self, text=name, borderwidth=2, relief="groove")
            frame.grid(row=i, column=0, columnspan=3, padx=5, pady=5, sticky=W + E)

            # Налаштування Кольору
            color_btn = Button(frame, text="Колір",
                               command=lambda n=name: self.choose_color(n))
            color_btn.pack(side=tk.LEFT, padx=5, pady=5)

            # Налаштування Розміру (повзунок)
            Label(frame, text="Розмір:").pack(side=tk.LEFT, padx=(10, 0))

            initial_size = self.settings.figure_settings[name]["size"] * 100

            size_scale = Scale(frame, from_=50, to=200, resolution=10,
                               orient=HORIZONTAL, label="%")
            size_scale.set(initial_size)
            size_scale.bind("<ButtonRelease-1>", lambda event, n=name: self.update_size(n, size_scale.get()))
            size_scale.pack(side=tk.LEFT, padx=5, pady=5)

        # Кнопка Застосувати та Закрити
        Button(self, text="Закрити", command=self.destroy).grid(row=len(self.settings.figure_settings),
                                                                column=0, columnspan=3, pady=10)

    def choose_color(self, name):
        """Відкриває діалог вибору кольору і оновлює налаштування."""
        color_code = colorchooser.askcolor(title=f"Виберіть колір для {name}")
        if color_code:
            self.settings.figure_settings[name]["color"] = color_code[1]
            self.redraw_callback()  # Перемалювати полотно

    def update_size(self, name, value):
        """Оновлює коефіцієнт розміру і перемальовує полотно."""
        self.settings.figure_settings[name]["size"] = value / 100.0
        self.redraw_callback()


# --- 4. Клас Діалогового Вікна Налаштування Тексту ---
class TextSettingsDialog(Toplevel):
    def __init__(self, master, settings, redraw_callback):
        super().__init__(master)
        self.title("Налаштування тексту")
        self.settings = settings
        self.redraw_callback = redraw_callback
        self.grab_set()

        self.create_widgets()

    def create_widgets(self):
        """Створює елементи керування для тексту кожної фігури."""
        for i, name in enumerate(self.settings.text_settings):
            frame = Label(self, text=name, borderwidth=2, relief="groove")
            frame.grid(row=i, column=0, columnspan=3, padx=5, pady=5, sticky=W + E)

            # Налаштування Кольору
            color_btn = Button(frame, text="Колір",
                               command=lambda n=name: self.choose_color(n))
            color_btn.pack(side=tk.LEFT, padx=5, pady=5)

            # Налаштування Розміру Шрифту (повзунок)
            Label(frame, text="Розмір шрифту:").pack(side=tk.LEFT, padx=(10, 0))

            initial_size = self.settings.text_settings[name]["size"]

            size_scale = Scale(frame, from_=8, to=36, resolution=1,
                               orient=HORIZONTAL, label="px")
            size_scale.set(initial_size)
            size_scale.bind("<ButtonRelease-1>", lambda event, n=name: self.update_size(n, size_scale.get()))
            size_scale.pack(side=tk.LEFT, padx=5, pady=5)

        # Кнопка Застосувати та Закрити
        Button(self, text="Закрити", command=self.destroy).grid(row=len(self.settings.text_settings),
                                                                column=0, columnspan=3, pady=10)

    def choose_color(self, name):
        """Відкриває діалог вибору кольору для тексту і оновлює налаштування."""
        color_code = colorchooser.askcolor(title=f"Виберіть колір тексту для {name}")
        if color_code:
            self.settings.text_settings[name]["color"] = color_code[1]
            self.redraw_callback()

    def update_size(self, name, value):
        """Оновлює розмір шрифту і перемальовує полотно."""
        self.settings.text_settings[name]["size"] = value
        self.redraw_callback()


# --- 5. Запуск Програми ---
if __name__ == "__main__":
    root = tk.Tk()
    app = GeometryApp(root)

    # Викликаємо draw_figures після того, як вікно буде промальовано (для коректного winfo_width/height)
    root.update_idletasks()
    app.draw_figures()

    root.mainloop()