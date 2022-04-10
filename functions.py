import tkinter
from tkinter import ttk
from tkinter.ttk import Combobox
from tkinter import Menu



def menu(where,what,message):
    minu = tkinter.Menu(where)
    minu.add_command(label = what)
    where.tkinter.config(minu = menu)



def print_some_text(where_to_render, message, a , b,c):
    text = tkinter.Label(where_to_render, text=message, font = ('Times New Roman', c))
    text.config(bg='#fdffe6')
    text.place(x = a, y = b)
    text.config(bg='#fdffe6')

def okno(where_to_render,widt, a1 , a2 ):
    pole = tkinter.Entry(where_to_render,width= widt)
    pole.place( x = a1,y = a2)



def But_Login(where_to_render,message, a3, a4):

    btn = tkinter.Button(where_to_render,text = message, command = where_to_render.quit())
    btn.place(x = a3, y = a4)


def Combo(where_to_render, a4, a5, massive):
    pass


class log_window():  # описание класса основного окна
    def __init__(self):
        self.window = tkinter.Tk()
        self.window.config(bg='#fdffe6')
        self.window.title("УДОБНЫЙ КОФНИГУРАТОР")
        self.window.geometry('1280x720')

    def clicked(self):
        self.window.mainloop()

    def render_log_screne(self):
        print_some_text(self.window, 'Удобный конфигуратор', 400, 0, 40)
        print_some_text(self.window, 'Введите логин и пароль:', 473.7, 214, 24)
        print_some_text(self.window, 'Логин:', 511, 266.4, 14)
        print_some_text(self.window, 'Пароль:', 505, 323, 14)
        okno(self.window, 20, 572.16, 266.4)
        okno(self.window, 20, 572.16, 324)
        But_Login(self.window, 'Авторизоваться', 580, 354,)
        self.window.mainloop()












