from tkinter import *
from tkinter.font import families, Font
import time

#! /usr/bin/env python
# -*- coding: Utf-8 -*

class Application:
    def __init__(self):
        self.fen = Tk() # la fenêtre de l'application
        self.fen.configure (bg="#438AA5")
        self.fen.title("Prog Paul et Gabi")
        self.ftComic = Font (family = 'Comic Sans MS', size = -50,\
                underline = False, weight = "bold",slant="italic")
        self.ftComic2 = Font (family = "Comic Sans MS", size = -20,\
                underline = False, weight = "bold")
        self.ftComic3 = Font (family = "Comic Sans MS", size = -35,\
                underline = False, weight = "bold")

        # Les variables
        #self.chaine=''

        self.k=0
        # les labels
        labelUn = Label (self.fen, text="MOT LE PLUS LONG")
        labelUn.configure (bg="#438AA5",fg="red", font = self.ftComic)
        labelUn.grid (row = 1,column = 1, padx = 10,pady = 20, columnspan =2)

        self.label2 = Label (self.fen, text="On commence?")
        self.label2.configure (bg="#438AA5",fg="red", font = self.ftComic3)
        self.label2.grid (row = 2,column = 1, padx = 10,pady = 20, columnspan =2)

        self.label3 = Label (self.fen, text="*********")
        self.label3.configure (bg="#438AA5",fg="red", font = self.ftComic3)
        self.label3.grid (row = 4,column = 1, padx = 10,pady = 20, columnspan =2)

        # On rajoute ligne 7 colonne 2 un bouton Quitter
        boutonQuitter = Button (self.fen, text=' Quitter ',command=self.fen.quit)
        boutonQuitter.grid (row = 7,  column = 2, padx = 10, pady = 10)
        boutonQuitter.configure (fg="blue", font = self.ftComic2)

        boutonInitialiser = Button (self.fen, text=' Top Départ ', command=self.depart)
        boutonInitialiser.grid (row = 7, column = 1, pady = 10)
        boutonInitialiser.configure (fg="blue", font = self.ftComic2)

        boutonV = Button (self.fen, text=' Voyelle ',command=self.Voyelle)
        boutonV.grid (row = 3,  column = 1, padx = 10, pady = 10)
        boutonV.configure (fg="blue", font = self.ftComic2)

        boutonC = Button (self.fen, text=' Consonne ', command=self.Consonne)
        boutonC.grid (row = 3, column = 2, pady = 10)
        boutonC.configure (fg="blue", font = self.ftComic2)



        # Création du cannevas et son image (232x245) dans le init
        self.photo = PhotoImage (file="C:\Users\Utilisateur\Desktop\Nouveau dossier (5)")
        self.cannevasImg6 = Canvas (self.fen, width =self.photo.width(), height = self.photo.height(), bg = "green")
        self.image = self.cannevasImg6.create_image( self.photo.width()//2,self.photo.height()//2, image = self.photo)
        self.cannevasImg6.grid(row = 4, column = 1, columnspan =2)

        # modif du cannevas et son image (232x245)
##        self.photo = PhotoImage (file="IMAGES//TRUC//annee.gif")
##        self.cannevasImg6.itemconfigure(self.image,image = self.photo)

        # On se donne la possibiliter de valider avec la touche entrée
##        self.fen.bind('<Return>', self.machin)


        # self.main()

##    def machin(self,evt):
##        self.photo = PhotoImage (file="IMAGES//TRUC//annee.gif")
##        self.cannevasImg6.itemconfigure(self.image,image = self.photo)


    def Voyelle(self):
        self.Voy=True
    def Consonne(self):
        self.Cons=True

    def depart (self):
        self.Voy=False
        self.Cons=False
        self.chaine=''
        self.label2.configure (text="Voyelle ou consonnes?")
        self.NbCoup=9
        self.label3.configure (text="")
        self.main()



    def main (self):
        import random
        CONSONNES = 'BBCCDDDFFGGHHJKLLLLLMMMNNNNNNPPQRRRRRRSSSSSSTTTTTTVVWXZ'
        voyelles = 'EEEEEEEEEEEEEEEAAAAAAAAAIIIIIIIIOOOOOOUUUUUUY'
        if self.Cons:
            self.chaine+=CONSONNES[random.randint(0,len(CONSONNES)-1)]
            self.Cons=False
            self.NbCoup-=1
        elif self.Voy:
            self.chaine+=voyelles[random.randint(0,len(voyelles)-1)]
            self.Voy=False
            self.NbCoup-=1

        self.label3.configure (text=self.chaine)

        if  self.NbCoup>0:
            self.fen.after(2,self.main)
        else:
            self.label2.configure (text="à vous de jouer")
            self.t0=time.clock()
            self.suite()


    def suite(self):
        if (time.clock()-self.t0)<10:
            self.label2.configure (text=int(10-(time.clock()-self.t0)+1))
            self.fen.after(2,self.suite)
        else:
            self.label2.configure (text="STOP")
            self.label3.configure (text="")

app=Application()
app.fen.mainloop()
app.fen.destroy()  # fin de l'application