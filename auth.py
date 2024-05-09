import os
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import tkinter as tk
from game_window import GameWindow  # Импортируем класс GameWindow из файла game_window.py

def dismiss(win):
    win.grab_release()
    win.destroy()

def openfile():
    try:
        text = open(r'C:\py\test.txt', 'r+')
        return text
    except FileNotFoundError:
        try:
            os.mkdir(r'C:\py')
            text = open(r'C:\py\test.txt', 'w')
            text.close()
            text = open(r'C:\py\test.txt', 'r+')
            return text
        except FileNotFoundError:
            text = open(r'C:\py\test.txt', 'r+')
            return text

class game:
    def __init__(self, main):
        s = ttk.Style()
        s.configure('my.TButton', font='Arial 20 bold')
        a = ttk.Style()
        a.configure('my1.TButton', font='Arial 22')

        self.count = 0
        self.main = main
        self.account = {}
        self.first_click = True
        self.login = ttk.Entry(width=20, justify='center', font='Arial 20 bold')
        self.password = ttk.Entry(width=20, justify='center', font='Arial 20 bold', show='*')
        self.txtl = Label(text='Логин', font='Arial 30 bold')
        self.txtp = Label(text='Пароль', font='Arial 30 bold')
        self.txt = Label(text='Для игры введите ваш логин и пароль', font='Arial 36 bold')
        self.blur = ttk.Button(text='😌', style='my1.TButton', command=lambda: self.bluring(self.password, self.blur))
        self.button_reg = ttk.Button(text='Зарегистрироваться', style='my.TButton', command=lambda: self.regist())
        self.button_avt = ttk.Button(text='Авторизоваться', style='my.TButton', command=lambda: self.authorization())

        self.txt.place(x=90, y=50)
        self.txtl.place(x=300, y=180)
        self.txtp.place(x=300, y=270)
        self.login.place(x=480, y=185, height=40)
        self.password.place(x=480, y=275, height=40)
        self.blur.place(x=744, y=275, width=42, height=42)
        self.button_avt.place(x=260, y=390)
        self.button_reg.place(x=530, y=390)
        self.game_window = None

    def bluring(self, pas, but):
        if self.count % 2 == 0:
            pas.config(show='')
            but.config(text='🧐')
        else:
            pas.config(show='*')
            but.config(text='😌')
        self.count += 1

    def authorization(self):
        s_l = self.login.get()
        s_p = self.password.get()

        if len(s_l) == 0 or len(s_p) == 0:
            messagebox.showwarning(title='Ошибка', message='Поле заполнения пусто')

        else:
            file = openfile()
            a = file.readline()[:-1].split(' ')

            while True:
                if a != ['']:
                    self.account[a[0]] = a[1]
                    a = file.readline()[:-1].split(' ')
                else:
                    break

            f_reg = False
            f_p = True
            for i in self.account.items():
                l, p = i
                if s_l == l and s_p == p:
                    f_reg = True
                    break
                elif s_l == l and s_p != p:
                    f_p = False

            if f_reg:
                self.main.withdraw()  # Скрыть окно авторизации
                self.open_game_window()


            elif not f_p:
                messagebox.showwarning(title='Ошибка', message='Неверный пароль')
            else:
                messagebox.showwarning(title='Ошибка', message='Такого аккаунта не существует')

    def open_game_window(self):
        if self.game_window is None:
            self.game_window = GameWindow(self.main)
            self.game_window.root.protocol("WM_DELETE_WINDOW",
                                           self.on_game_window_close)  # Обработчик закрытия окна игры
        else:
            self.game_window.show()

    def on_game_window_close(self):
        self.main.deiconify()  # Восстановить видимость окна авторизации
        self.game_window.hide()  # Скрыть окно игры

    def regist(self):
        win = Toplevel()
        win.geometry('1080x520+430+250')
        win.title('Регистрация')
        win.resizable(False, False)
        win.protocol('WM_DELETE_WINDOW', lambda: dismiss(win))
        win.grab_set()

        login = ttk.Entry(win, width=20, justify='center', font='Arial 20 bold')
        password = ttk.Entry(win, width=20, justify='center', font='Arial 20 bold', show='*')
        txtl = Label(win, text='Логин', font='Arial 30 bold')
        txtp = Label(win, text='Пароль', font='Arial 30 bold')
        txt = Label(win, text='Введите желаемые логин и пароль', font='Arial 36 bold')
        blur = ttk.Button(win, text='😌', style='my1.TButton', command=lambda: self.bluring(password, blur))
        button_reg = ttk.Button(win, text='Зарегистрироваться', style='my.TButton', command=lambda: registrate())

        txt.place(x=120, y=50)
        txtl.place(x=300, y=180)
        txtp.place(x=300, y=270)
        login.place(x=470, y=185, height=40)
        password.place(x=470, y=275, height=40)
        blur.place(x=735, y=275, width=42, height=42)
        button_reg.place(x=405, y=390)

        def registrate():
            s_l = login.get()
            s_p = password.get()

            if len(s_l) == 0 or len(s_p) == 0:
                messagebox.showwarning(title='Ошибка', message='Поле заполнения пусто')
            else:
                file = openfile()
                a = file.readline()[:-1].split(' ')

                while True:
                    if a != ['']:
                        self.account[a[0]] = a[1]
                        a = file.readline()[:-1].split(' ')
                    else:
                        break

                f_reg = False

                for i in self.account.items():
                    l, p = i
                    if s_l == l:
                        f_reg = True

                if not f_reg:
                    file = openfile()
                    file.seek(0, os.SEEK_END)
                    file.write(f'{s_l} {s_p}\n')
                    file.close()

                    for widget in win.winfo_children():
                        widget.destroy()

                    Label(win, text='Вы успешно зарегистрировались', font='Arial 36 bold').place(x=140, y=200)
                    win.after(2000, lambda: (win.destroy(), win.grab_release()))
                else:
                    messagebox.showwarning(title='Ошибка', message='Такой аккаунт уже существует')

    def play(self):
        BRD_ROWS = BRD_COLS = 8
        CELL_SZ = 100

        canvas = Canvas(self.main, width=CELL_SZ * BRD_ROWS, height=CELL_SZ * BRD_COLS)

        cell_colors = ['white', 'black']
        ci = 0  # color index

        for row in range(BRD_ROWS):
            for col in range(BRD_COLS):
                x1, y1 = col * CELL_SZ, row * CELL_SZ
                x2, y2 = col * CELL_SZ + CELL_SZ, row * CELL_SZ + CELL_SZ
                canvas.create_rectangle((x1, y1), (x2, y2), fill=cell_colors[ci])

                ci = not ci

            ci = not ci
        self.main.geometry('800x800+560+100')
        canvas.pack()

    def open_game_window(self):
        game_window = tk.Toplevel()
        app = GameWindow(game_window)
        game_window.wait_window()  # Показать окно с игрой и дождаться его закрытия

root = Tk()
root.title('Авторизация')
root.geometry('1080x520+430+250')
root.resizable(False, False)

game(root)



root.mainloop()
