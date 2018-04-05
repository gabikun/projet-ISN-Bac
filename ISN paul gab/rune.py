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

        #images
        self.photo_fond = PhotoImage (file="sallefond.png")
        self.parchemin = PhotoImage (file="parchemin.png")
        self.pierre = PhotoImage (file="pierre.png")

        #evenements
        self.fen.bind('<Button-1>', self.ClicSouris)
        self.fen.bind('<Motion>', self.motion)

        #canvas du fond
        self.cannevasFond = Canvas (self.fen, width =self.photo_fond.width() , height =self.photo_fond.height() ,  bg = "green")
        self.cannevasFond.grid(row = 1, column = 1, columnspan = 5, rowspan = 5)

        #bouton Quitter
        boutonQuitter = Button (self.fen, text=' Quitter ',command=self.fen.quit)
        boutonQuitter.grid (row = 6,  column = 7, padx = 10, pady = 10, sticky="SE")
        boutonQuitter.configure (fg="blue", font = self.ftComic2)

        #image de fond
        self.image_fond = self.cannevasFond.create_image((self.photo_fond.width()+5)//2,(self.photo_fond.height()+5)//2,image = self.photo_fond)

        #positons des objets
        self.tab_runes = [[0,2,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]]

        #tableau des pierres
        self.tab_pierre= [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

        #fonctions
        self.dessin()


    def dessin(self):
        num_pierre=0
        for i in range(5):
            for j in range(5):
                if self.tab_runes[i][j]==1:
                    self.tab_pierre[num_pierre] = self.cannevasFond.create_image((i*50)+27,(j*50)+27, image=self.pierre)
                if self.tab_runes[i][j]==2:
                    self.img_parchemin = self.cannevasFond.create_image((i*50)+27,(j*50)+27, image=self.parchemin)


    def motion(self,event):
        self.sourisX=event.x
        self.sourisY=event.y


    def ClicSouris(self,event):
        print("clic souris en x=",self.sourisX,"  et en y=",self.sourisY)
##        for i in range(9):
##            if 291<=self.sourisY<=340 and 15+77*i<=self.sourisX<=67+77*i:
##                self.cannevasImg6.delete(self.ImageCarte[i])





app=Application()
app.fen.mainloop()
app.fen.destroy() # fin de l'application
