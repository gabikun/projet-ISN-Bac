from tkinter import *
from tkinter.font import families, Font

#! /usr/bin/env python
# -*- coding: Utf-8 -*


class Application:
    def __init__(self):
        self.fen = Tk() # la fenêtre de l'application
        self.fen.configure (bg="#000000")
        self.fen.title("c.c")
        self.ftComic = Font (family = 'Comic Sans MS', size = -50,\
                underline = False, weight = "bold",slant="italic")
        ftComic2 = Font (family = "Comic Sans MS", size = -20,\
                underline = False)


        # On rajoute ligne 2 colonne 2 une entrée (un input)
        self.entreeUn = Entry (self.fen, show='*')
        self.entreeUn.grid (row = 1, column = 2, padx = 10, pady = 10)
        self.entreeUn.configure (fg="blue",font = ftComic2)
        self.entreeUn.focus_set()


        # On rajoute ligne 6 colonne 1 un bouton Valider
        boutonValider = Button (self.fen, text=' Valider ',command=self.valider)
        boutonValider.grid (row = 2, column = 2, pady = 10)
        boutonValider.configure (fg="black", font = ftComic2)


        # On rajoute ligne 7 colonne 2 un bouton Quitter
        boutonQuitter = Button (self.fen, text=' Quitter ',command=self.fen.quit)
        boutonQuitter.grid (row = 3,  column = 3, padx = 5, pady = 5)
        boutonQuitter.configure (fg="black", font = ftComic2)

        # On se donne la possibiliter de valider avec la touche entrée
        self.fen.bind('<Return>', self.valider1)

        # On rajoute ligne 2 colonne 1  "collé" à droite (est)
        labelDeux = Label (self.fen, text="Année")
        labelDeux.configure (bg="black",fg="white",font = ftComic2)
        labelDeux.grid (row = 2, column = 1)


    def valider1 (self,evt) :
        self.valider()

    def valider (self) :
        mdp = int(self.entreeUn.get())
        if mdp=="123":
            x="bissextile.gif"
        else:
            x="nonbissextile.gif"


    def Verification(self):
        if Motdepasse.get() == 'python27':
            # le mot de passe est bon : on affiche une boîte de dialogue puis on ferme la fenêtre
            showinfo('Résultat','Mot de passe correct.\nAu revoir !')
            Mafenetre.destroy()
        else:
            # le mot de passe est incorrect : on affiche une boîte de dialogue
            showwarning('Résultat','Mot de passe incorrect. Veuillez recommencer !')
            Motdepasse.set('')




app=Application()
app.fen.mainloop()
app.fen.destroy()  # fin de l'application