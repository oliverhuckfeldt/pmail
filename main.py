#!/usr/bin/env python
from tkinter import *
import tkinter.messagebox as messagebox


class Mailer:
    def __init__(self):
        pass

    def send(self):
        messagebox.showinfo('Info', 'Message send!')


class Window(Frame):
    def __init__(self, app):
        Frame.__init__(self, app, pady=10, padx=10)
        self.app = app

    def build(self):
        topbar = Frame(self)
        footer = Frame(self)

        Label(topbar, text='Adresse').pack(side=LEFT)
        Entry(topbar).pack(side=LEFT, expand=1, fill=X)
        topbar.pack(fill=BOTH, expand=0)

        Text(self).pack(fill=BOTH, expand=1)
        self.pack(fill=BOTH, expand=1)

        Button(footer, text='Senden', command=self.app.mailer.send).pack(side=LEFT)
        footer.pack(fill=BOTH, expand=0)


class App(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.window = Window(self)
        self.mailer = Mailer()
        self.init()

    def init(self):
        self.title('Pmail')
        self.geometry('800x600')
        self.window.build()

    def run(self):
        self.mainloop()


if __name__ == '__main__':
    app = App()
    app.run()
