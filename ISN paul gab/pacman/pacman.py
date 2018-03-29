from tkinter import *
from tkinter.font import families, Font

#! /usr/bin/env python
# -*- coding: Utf-8 -*

class Application:
    def __init__(self):
        self.fen = Tk() # la fenêtre de l'application
        self.fen.configure (bg="#438AA5")
        self.fen.title("Vive l'ISN")
        self.ftComic = Font (family = 'Comic Sans MS', size = -50,\
                underline = False, weight = "bold",slant="italic")
        self.ftComic2 = Font (family = "Comic Sans MS", size = -20,\
                underline = False, weight = "bold")
        self.ftComic3 = Font (family = "Comic Sans MS", size = -35,\
                underline = False, weight = "bold")

        # Les variables
        self.bouge=False
        self.cannevasImg6 = Canvas (self.fen, width =900, height =900 , bg = "green",highlightbackground="#438AA5")
        self.cannevasImg6.grid(row = 1, column = 1, columnspan =2,rowspan=7)

        self.photo_fond = PhotoImage (file="laby.png")

        self.image_fond = self.cannevasImg6.create_image( 450,450, image = self.photo_fond)

        self.photo_fant1 = PhotoImage (file="fant.png")

        self.fant1_X=112
        self.fant1_Y=112
        self.image_fant1 = self.cannevasImg6.create_image( 112,112, image = self.photo_fant1)



        self.main()
##        self.cannevasImg6.bind("<Button-1>",self.souris)         #UTILISE LES MOUVEMENTS DE LA SOURIS POUR DEPLACER LA RAQUETTE .
##
##        self.cannevasImg6.bind('<Motion>',self.motion)
##




        # On se donne la possibiliter de valider avec la touche entrée
##        self.fen.bind('<Return>', self.machin)


        # self.main()

    def Voyelle(self):
        self.Voy=True
    def Consonne(self):
        self.Cons=True


    def main (self):
        self.fant1_X+=1
        self.fant1_Y+=1

        self.cannevasImg6.coords(self.image_fant1, self.fant1_X, self.fant1_Y)

        if  True:
            self.fen.after(2,self.main)
        else:
            self.label2.configure (text="à vous de jouer")


app=Application()
app.fen.mainloop()
app.fen.destroy()  # fin de l'application