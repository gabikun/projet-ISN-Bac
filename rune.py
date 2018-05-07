from PIL import Image, ImageTk
from tkinter import *
from tkinter.font import families, Font
from subprocess import *


#! /usr/bin/env python
# -*- coding: Utf-8 -*

class Application:
    def __init__(self):
        self.fen = Tk()
        self.fen.configure (bg="grey")
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
        self.vide = PhotoImage (file="vide.png")

        #evenements
        self.fen.bind('<Escape>',self.quitter)
        self.fen.bind('<Up>',self.up)
        self.fen.bind('<Down>',self.down)
        self.fen.bind('<Right>',self.right)
        self.fen.bind('<Left>',self.left)


        #canvas du fond
        self.canevasFond = Canvas (self.fen, width =self.photo_fond.width() , height =self.photo_fond.height() , bg = "green" , highlightbackground = "#545454")
        self.canevasFond.grid(row = 1, column = 1, columnspan = 5, rowspan = 5)

        #image de fond
        self.image_fond = self.canevasFond.create_image((self.photo_fond.width()+4)//2,(self.photo_fond.height()+4)//2,image = self.photo_fond)


        #sortie du parchemin
        self.canevasSortie = Canvas (self.fen, width =self.vide.width() , height =self.vide.height() , bg = "#545454" , highlightbackground = "#545454")
        self.canevasSortie.grid (row = 3, column = 6, columnspan = 1, rowspan = 1)

        #image de fond
        self.image_sortie = self.canevasSortie.create_image((self.vide.width()+4)//2,(self.vide.height()+4)//2,image = self.vide)


        #bouton Quitter
        boutonQuitter = Button (self.fen, text=' Quitter ',command=self.fen.quit)
        boutonQuitter.grid (row = 7,  column = 1, columnspan = 2, sticky="SW", padx = 10 , pady = 10)
        boutonQuitter.configure (fg="blue", font = self.ftComic2)

        #bouton Menu
        boutonMenu = Button (self.fen, text=' Menu ',command=self.menu)
        boutonMenu.grid (row = 7,  column = 5, columnspan = 2, sticky="SE", padx = 10 , pady = 10)
        boutonMenu.configure (fg="blue", font = self.ftComic2)

        #label Etat sur le jeu
        self.labelgagner = Label(self.fen, text='Sortez le parchemin')
        self.labelgagner.grid(row=6, column = 1 , columnspan =6, rowspan = 1)
        self.labelgagner.configure(bg='grey', fg='blue', font=self.ftComic2)



        #positons des objets
        self.tab_runes =[
        [0,2,1,1,1],
        [1,1,1,1,1],
        [1,1,1,1,1],
        [1,1,1,1,1],
        [1,1,1,1,1]]

        #fonctions
        self.dessin()

        #quitter le jeu
    def quitter(self, event):
        self.fen.quit()


        #déplacements
    def up(self, event):
        self.getvide()
        if self.coordL==4:
            pass
        else:
            self.tab_runes[self.coordL][self.coordC]=self.tab_runes[self.obj_basL][self.obj_basC]
            self.tab_runes[self.obj_basL][self.obj_basC]=0
        self.dessin()

    def down(self, event):
        self.getvide()
        if self.coordL==0:
            pass
        else:
            self.tab_runes[self.coordL][self.coordC]=self.tab_runes[self.obj_hautL][self.obj_hautC]
            self.tab_runes[self.obj_hautL][self.obj_hautC]=0
        self.dessin()

    def left(self, event):
        self.getvide()
        if self.coordC==4:
            pass
        else:
            self.tab_runes[self.coordL][self.coordC]=self.tab_runes[self.obj_droiteL][self.obj_droiteC]
            self.tab_runes[self.obj_droiteL][self.obj_droiteC]=0
        self.dessin()

    def right(self, event):
        self.getvide()
        if self.coordC==0:
            pass
        else:
            self.tab_runes[self.coordL][self.coordC]=self.tab_runes[self.obj_gaucheL][self.obj_gaucheC]
            self.tab_runes[self.obj_gaucheL][self.obj_gaucheC]=0
        self.dessin()


    #coordonnées relative au vide
    def getvide(self):
        for i in range(5):
            for j in range(5):
                if self.tab_runes[j][i]==0:
                    self.coordL=j
                    self.coordC=i

                    self.obj_hautL=j-1
                    self.obj_hautC=i

                    self.obj_basL=j+1
                    self.obj_basC=i

                    self.obj_droiteL=j
                    self.obj_droiteC=i+1

                    self.obj_gaucheL=j
                    self.obj_gaucheC=i-1


    #affichage des objets
    def dessin(self):
        for i in range(5):
            for j in range(5):
                if self.tab_runes[j][i]==1:
                    self.img_pierre = self.canevasFond.create_image((i*50)+27,(j*50)+27, image=self.pierre)
                if self.tab_runes[j][i]==2:
                    self.img_parchemin = self.canevasFond.create_image((i*50)+27,(j*50)+27, image=self.parchemin)
                if self.tab_runes[j][i]==0:
                    self.img_vide = self.canevasFond.create_image((i*50)+27,(j*50)+27, image=self.vide)
        if self.tab_runes[2][4]==2:
            self.tab_runes[2][4]=0
            self.img_vide = self.canevasFond.create_image((4*50)+27,(2*50)+27, image=self.vide)
            self.canevasSortie.create_image((self.vide.width()+4)//2,(self.vide.height()+4)//2,image = self.parchemin)
            self.gagner()


    #quand le parchemin sort de la salle
    def gagner(self):
        self.labelgagner.config(text='Gagné', fg='red')
        self.fen.bind('<Escape>',self.bloquer)
        self.fen.bind('<Up>',self.bloquer)
        self.fen.bind('<Down>',self.bloquer)
        self.fen.bind('<Right>',self.bloquer)
        self.fen.bind('<Left>',self.bloquer)


    #empecher les flèches de déplacer les objets
    def bloquer(self,event):
        pass


    #retour au menu principal
    def menu(self):
        subprocess



app=Application()
app.fen.mainloop()
app.fen.destroy() # fin de l'application
