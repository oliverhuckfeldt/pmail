#!/usr/bin/env python
from tkinter import Tk, Frame


class App(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.win = Frame()
        self.build()

    def build(self):
        pass

    def run(self):
        self.mainloop()


app = App()
app.run()
