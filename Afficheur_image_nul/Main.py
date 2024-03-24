from tkinter import *
from PIL import Image
from PIL import ImageTk
import webbrowser
import AffichageImage 
# Fonctions contenant ce que font les deux boutons

# bouton1

def lien():
    webbrowser.open_new("https://twitter.com/esprinct")

# bouton2

def lien2():
    AffichageImage.affichageimage()

# bouton3
def lien3():
    webbrowser.open_new("https://github.com/Esprinct/Afficheur_image_nul")

# Création de la fenetre
    
fenetre = Tk()
fenetre.title("fenetre")
fenetre.geometry("720x480")
fenetre.minsize(480, 360)
fenetre.config(background='#41B77F')

#Affichage de la boite
boite = Frame(fenetre, bg ='gray', bd=1, relief=SUNKEN)
boite.pack(expand=YES)

# Création du Texte
# Affichage du Titre
label_title = Label(boite, text="Bonjour", font =("Helvetica", 15), bg =('gray'))
label_title.pack(expand=YES)

# Affichage du Sous-titre
label_subtitle = Label(boite, text="Souhaitez-vous accéder à la CULTURE?", font =("Helvetica", 12), bg =('grey'))
label_subtitle.pack(expand=YES)

# Affichage du Bouton 1
boutton= Button(boite, text="Oui, je souhaite plus de culture.", font =("Yada Yada Yada", 15), bg =('white'),command=lien)
boutton.pack(pady=25, fill=X)

#Affivhage du Bouton2
boutton2= Button(boite, text="Oui, je veux ENCORE plus de culture", font =("Yada Yada Yada", 15), bg =('white'),command=lien2)
boutton2.pack(pady=25, fill=X)

#Affivhage du Bouton3
boutton3= Button(boite, text="test pour push git", font =("Yada Yada Yada", 15), bg =('white'),command=lien3)
boutton3.pack(pady=25, fill=X)

fenetre.mainloop()