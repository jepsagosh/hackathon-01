import functions as f
import tkinter

class main_screen():
    def __init__(self):
        self.window = tkinter.Tk()
        self.window.config(bg='#fdffe6')
        self.window.title("УДОБНЫЙ КОФНИГУРАТОР")
        self.window.geometry('1280x720')

    def render_main_screen(self):
        f.menu(self.window,'Новый')
        self.window.mainloop()