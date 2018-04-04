from PIL import Image, ImageTk
from tkinter import *
from tkinter.font import families, Font

#! /usr/bin/env python
# -*- coding: Utf-8 -*

class Application:
    def __init__(self):
        self.fen = Tk()
        self.fen.configure (bg="#438AA5")
        self.fen.title("rune")
        self.fen.resizable(width=False, height=False)
        self.ftComic = Font (family = 'Comic Sans MS', size = -50,\
                underline = False, weight = "bold",slant="italic")
        self.ftComic2 = Font (family = "Comic Sans MS", size = -20,\
                underline = False)

        self.photo_fond = PhotoImage (file="sallefond.png")

        self.cannevasFond = Canvas (self.fen, width =self.photo_fond.width() , height =self.photo_fond.height() ,  bg = "green")
        self.cannevasFond.grid(row = 1, column = 1, columnspan = 5, rowspan = 5)
        self.cannevasFond.configure (border=5)

        self.image_fond = self.cannevasFond.create_image((self.photo_fond.width()+14)//2,(self.photo_fond.height()+14)//2,image = self.photo_fond)




app=Application()
app.fen.mainloop()
app.fen.destroy() # fin de l'application
