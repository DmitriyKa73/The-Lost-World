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

        self.button_frame = tk.Frame(root)
        self.button_frame.pack(expand=True)  # Растягиваем фрейм по обе стороны

        style = ttk.Style()
        style.configure("Game.TButton", font=("Arial", 20), width=15, padding=10)

        self.start_button = ttk.Button(self.button_frame, text="Начать игру", style="Game.TButton", command=self.start_game)
        self.start_button.pack(pady=10)  # Увеличиваем отступ

        self.about_button = ttk.Button(self.button_frame, text="О проекте", style="Game.TButton", command=self.show_about)
        self.about_button.pack(pady=10)  # Увеличиваем отступ

        self.quit_button = ttk.Button(self.button_frame, text="Выйти из игры", style="Game.TButton", command=self.quit_game)
        self.quit_button.pack(pady=10)  # Увеличиваем отступ

    def center_window(self):
        window_width = self.root.winfo_reqwidth()
        window_height = self.root.winfo_reqheight()
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = int((screen_width - 800) / 2)
        y = int((screen_height - 600) / 2)
        self.root.geometry(f"800x600+{x}+{y}")

    def show(self):
        self.root.deiconify()

    def hide(self):
        self.root.withdraw()

    def start_game(self):
        pass

    def show_about(self):
        pass

    def quit_game(self):
        self.root.destroy()


def main():
    root = tk.Tk()
    app = GameWindow(root)
    root.mainloop()

if __name__ == "__main__":
    main()

