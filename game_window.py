import tkinter as tk
from tkinter import ttk

class GameWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Игра")
        self.root.geometry("800x600")
        self.center_window()

        self.label = tk.Label(root, text="Добро пожаловать в игру!", font=("Arial", 30))
        self.label.pack(pady=20)

        self.start_button = ttk.Button(root, text="Начать игру", style="Game.TButton", command=self.start_game)
        self.start_button.pack(pady=20, padx=40)

        self.about_button = ttk.Button(root, text="О проекте", style="Game.TButton", command=self.show_about)
        self.about_button.pack(pady=20, padx=40)

        self.quit_button = ttk.Button(root, text="Выйти из игры", style="Game.TButton", command=self.quit_game)
        self.quit_button.pack(pady=20, padx=40)

    def center_window(self):
        window_width = self.root.winfo_reqwidth()
        window_height = self.root.winfo_reqheight()
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = int((screen_width - 800) / 2)  # Установим ширину окна в 800
        y = int((screen_height - 600) / 2)  # Установим высоту окна в 600
        self.root.geometry(f"800x600+{x}+{y}")  # Установим размеры окна и его положение

    def show(self):
        self.root.deiconify()  # Показать окно игры

    def hide(self):
        self.root.withdraw()  # Скрыть окно игры
    def start_game(self):
        # Логика для начала игры
        pass

    def show_about(self):
        # Логика для показа информации о проекте
        pass

    def quit_game(self):
        self.root.destroy()


def main():
    root = tk.Tk()
    app = GameWindow(root)
    root.mainloop()

if __name__ == "__main__":
    main()
