import tkinter as tk
from tkinter import ttk
from auth import game

def main():
    root = tk.Tk()
    root.title('Игра "Затерянный мир"')
    root.geometry('800x600')

    # Создание экземпляра игры
    game_instance = game(root)

    root.mainloop()

if __name__ == "__main__":
    main()
