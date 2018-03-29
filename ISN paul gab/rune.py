from tkinter import *
from tkinter.font import families, Font

#! /usr/bin/env python
# -*- coding: Utf-8 -*

class Application:
    def __init__(self):
        self.fen = Tk()
        self.fen.configure (bg="#438AA5")
        self.fen.title("rune")
        self.ftComic = Font (family = 'Comic Sans MS', size = -50,\
                underline = False, weight = "bold",slant="italic")
        self.ftComic2 = Font (family = "Comic Sans MS", size = -20,\
                underline = False)

        self.cannevasImg6 = Canvas (self.fen, width =100, height =100 , bg = "black",highlightbackground="#438AA5")
        self.cannevasImg6.grid(row = 1, column = 1)

app=Application()
app.fen.mainloop()
app.fen.destroy() # fin de l'application