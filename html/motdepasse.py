 from tkinter import *
from tkinter.font import families, Font

#! /usr/bin/env python
# -*- coding: Utf-8 -*


class Application:
    def __init__(self):
        self.fen = Tk()                                                             # la fenêtre de l'application
        self.fen.configure (bg="#000000")                                           # couleur de fond
        self.fen.title("c.c")                                                       # titre
        self.ftComic = Font (family = 'Comic Sans MS', size = -50,\
                underline = False, weight = "bold",slant="italic")
        self.ftComic2 = Font (family = "Comic Sans MS", size = -20,\
                underline = False)


        # On rajoute un input
        self.entreeUn = Entry (self.fen, show='*')                                  # création input + cache les caractères
        self.entreeUn.grid (row = 1, column = 2, padx = 10, pady = 10)              # position
        self.entreeUn.configure (bg ='bisque', fg='maroon',font = self.ftComic2)    # config
        self.entreeUn.focus_set()                                                   # met le focus de la souris dans le champ de saisie


        # On rajoute un bouton Valider
        boutonValider = Button (self.fen, text=' Valider ',command=self.valider)    # création boutton
        boutonValider.grid (row = 2, column = 2, pady = 10)                         # position
        boutonValider.configure (fg="black", font = self.ftComic2)                  # config


        # On rajoute un bouton Quitter
        boutonQuitter = Button (self.fen, text=' Quitter ',command=self.fen.quit)   # création boutton
        boutonQuitter.grid (row = 3,  column = 3, padx = 5, pady = 5)               # position
        boutonQuitter.configure (fg="black", font = self.ftComic2)                  # config

        # Valider avec la touche entrée et quitter avec la touche échape
        self.fen.bind('<Return>', self.valider1)                                    # le bouton "Entrer" fait comme le bouton Valider
        self.fen.bind('<Escape>', self.quitter)                                     # le bouton "échape" fait comme le bouton Quitter

        # On créer un label pour le mot de passe
        self.resultatmdp = Label (self.fen, text="Trouvez la clé")                  # création texte
        self.resultatmdp.grid(row = 3, column = 2)                                  # position
        self.resultatmdp.configure(bg="black", fg="white", font = self.ftComic2)    # config


    def quitter (self,evt):
        self.fen.quit()                                                             # quitter

    def valider1 (self,evt) :
        self.valider()                                                              # lance la fonciton valider

    def valider (self):
        mdp = str(self.entreeUn.get())                                              # prend le texte dans l'input et met la chaine de caractère dans mdp
        if mdp == 'baba':                                                           # vérification condition
            print ("bon mdp")
            self.resultatmdp.config (text="Bonne clé", fg="green")                  # changement du label

        else:
            print ("mauvais mdp")
            self.resultatmdp.config (text="Mauvaise clé", fg="red")                 # changement du label




app=Application()
app.fen.mainloop()
app.fen.destroy()  # fin de l'application
