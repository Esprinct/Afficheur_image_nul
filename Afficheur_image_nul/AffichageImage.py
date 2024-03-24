from tkinter import *
from PIL import Image
from PIL import ImageTk

def affichageimage():
    fenetre2 = Toplevel()
    fenetre2.title("fenetre")
    fenetre2.geometry("1076x1080")
    fenetre2.minsize(480, 360)
    fenetre2.config(background='white')
    #Label de l'image
    label_title = Label(fenetre2, text="SARKOSY EN 3D AVEC UNE CHAINE EN OR QUI BRILLE", font =("Helvetica", 25), bg =('white'))
    label_title.pack(expand=YES)
    #image de culture
    hauteur = 635
    Largeur = 411
    nude = ImageTk.PhotoImage(Image.open("Afficheur_image_nul\\image.png"))
    #canvas
    canvas = Canvas(fenetre2,width=hauteur, height= Largeur)
    canvas.create_image(hauteur/2,Largeur/2, image=nude)
    canvas.pack(expand='YES')


    fenetre2.mainloop()