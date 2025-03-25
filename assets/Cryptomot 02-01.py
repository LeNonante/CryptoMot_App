Version="2.01"
# A FAIRE
## afficher aide
## boutons
##
##

import tkinter as tk
from time import *
from tkinter import *

# Creer la fonction Texte_aide qui renvoie tout le texte à afficher dans la fenetre aide
def texte_aide (version) :
    fichier = open("assets/aide.txt",'r')
    lecture=fichier.read()
    lecture="Version : "+version+"\n"+lecture
    fichier.close
    return lecture


def AfficherAide (): #Fonction creéant la fenetre aide
    FenetreAide=Toplevel(fenetre, height=680, width=1300)
    FenetreAide.title("Aide")
    FenetreAide.resizable(width=False, height=False)
    FenetreAide.configure(background="white")
    aide=texte_aide(Version)
    label_aide=Label(FenetreAide,text=texte_aide(Version),font="Arial 11",background="white", justify = "left").place(x=10,y=10)
    boutton_quitter_aide=Button(FenetreAide, text="Quitter", command=FenetreAide.destroy, height = 5, width = 20).place(x=605,y=550)

#Creer les fonctions cyptage_mot / decryptage_mot /// elle retournent les valeurs fianles des mots ou un int (0,1... en fonction de l'erreur)
def cryptage_mot (mot,cle) :
    nb_lettre_mot = len(mot)
    nb_lettre_cle = len(cle)
    result="" ##Futur mot codé / décodé
    y=0 ##Place de la lettre du code à prendre en compte
    if nb_lettre_cle==0 or nb_lettre_mot==0 : ##retourne 0 si variable vide
        return 0
    else : ##si aucune variable vide
        for k in mot : ## k prend la valeur de la lettre à modifier dans le mot, une par une
            x=ord(k) ##x prend la valeur ASCII de la lettre 4

            #On donne à x la valeur de NOTRE alphabet
            if x==32 : ##Si c'est un espace, on lui donne 64 comme valeur
                x=64
            elif x>64 and x<91 : ##Si c'est une majuscule, on rammène de 27 à 52
                x=x-38
            elif x>96 and x<123 :##Si c'est une minuscule, on ramène de 1 à 26
                x=x-96
            elif x==46 : ##Si c'est un point on lui donne 63
                x=63
            elif x>47 and x<58 : ##Si c'est un chiffre on le met entre 53 et 62
                x=x+5
            else : ##Erreur caractère special mot a coder
                return 1

            #On s'occupe de la clé
            if y >= nb_lettre_cle :
                y=y-nb_lettre_cle
            z=cle[y] ## z vaut la valeur de la lettre a etudier de la cle en table ascii
            z=ord(z)
            if z==32 : ##Si c'est un espace, on lui donne 64 comme valeur
                z=64
            elif z>64 and z<91 : ## Si c'est une majuscule, on rammène de 27 à 52
                z=z-38
            elif z>96 and z<123 :##Si c'est une minuscule, on ramène de 1 à 26
                z=z-96
            elif z==46 : ##Si c'est un point on lui donne 63
                z=63
            elif z>47 and z<58 : ##Si c'est un chiffre on le met entre 53 et 62
                z=z+5
            else : ##Erreur caractère special clé
                return 2

            #On additionne les lettres de la clé et du mot
            zf=x+z  ##zf est la valeur de la lettre après addition
            if zf>64 : ## on la remet entre 1 et 64 (dans notre alphabet) si elle est au dessus
                zf=zf-64

            # On ramène aux numéros de la table ASCII
            if zf>0 and zf<27 : ##Si c'est une minuscule, on lui donne une valeur de 97 à 122
                zf=zf+96
            elif zf>26 and zf<53 : ##Si c'est une majuscule, on lui donne une valeur de 65 à 91
                zf=zf+38
            elif zf==64 : ##Si c'est un espace, on lui donne 32 comme valeur
                zf=32
            elif zf ==63 : ## Si c'est un point, on lui donne 46
                zf=46
            elif zf>52 and zf<63 : ##Si c'est un nombre, on le ramenne entre 48 et 57
                zf=zf-5
            zf=chr(zf) ##Puis on l'a remet en lettre

            result=result+zf
            y=y+1
        result="/"+result+"/"
        return result

def decryptage_mot (mot,cle) :
    nb_lettre_mot = len(mot)
    nb_lettre_cle = len(cle)
    result="" ##Futur mot codé / décodé
    y=0 ##Place de la lettre du code à prendre en compte
    if nb_lettre_cle==0 or nb_lettre_mot==0 : ##retourne 0 si variable vide
        return 0
    else : ##si aucune variable vide
        for k in mot : ## k prend la valeur de la lettre à modifier dans le mot, une par une
            x=ord(k) ##x prend la valeur ASCII de la lettre 4

            #On donne à x la valeur de NOTRE alphabet
            if x==32 : ##Si c'est un espace, on lui donne 64 comme valeur
                x=64
            elif x>64 and x<91 : ##Si c'est une majuscule, on rammène de 27 à 52
                x=x-38
            elif x>96 and x<123 :##Si c'est une minuscule, on ramène de 1 à 26
                x=x-96
            elif x==46 : ##Si c'est un point on lui donne 63
                x=63
            elif x>47 and x<58 : ##Si c'est un chiffre on le met entre 53 et 62
                x=x+5
            else : ##Erreur caractère special mot a coder
                return 1

            #On s'occupe de la clé
            if y >= nb_lettre_cle :
                y=y-nb_lettre_cle
            z=cle[y] ## z vaut la valeur de la lettre a etudier de la cle en table ascii
            z=ord(z)
            if z==32 : ##Si c'est un espace, on lui donne 64 comme valeur
                z=64
            elif z>64 and z<91 : ## Si c'est une majuscule, on rammène de 27 à 52
                z=z-38
            elif z>96 and z<123 :##Si c'est une minuscule, on ramène de 1 à 26
                z=z-96
            elif z==46 : ##Si c'est un point on lui donne 63
                z=63
            elif z>47 and z<58 : ##Si c'est un chiffre on le met entre 53 et 62
                z=z+5
            else : ##Erreur caractère special clé
                return 2

            #On additionne les lettres de la clé et du mot
            zf=x-z  ##zf est la valeur de la lettre après addition
            if zf<1 : ## on la remet entre 1 et 64 (dans notre alphabet) si elle est au dessus
                zf=zf+64

            # On ramène aux numéros de la table ASCII
            if zf>0 and zf<27 : ##Si c'est une minuscule, on lui donne une valeur de 97 à 122
                zf=zf+96
            elif zf>26 and zf<53 : ##Si c'est une majuscule, on lui donne une valeur de 65 à 91
                zf=zf+38
            elif zf==64 : ##Si c'est un espace, on lui donne 32 comme valeur
                zf=32
            elif zf ==63 : ## Si c'est un point, on lui donne 46
                zf=46
            elif zf>52 and zf<63 : ##Si c'est un nombre, on le ramenne entre 48 et 57
                zf=zf-5
            zf=chr(zf) ##Puis on l'a remet en lettre

            result=result+zf
            y=y+1
        result="/"+result+"/"
        return result


#*******************************************************************************
#1. CONFIGURATION DE LA FENTERE GRAPHIQUE
fenetre = Tk()
fenetre.title("Cryptomot")
fenetre.geometry("1350x730")
fenetre.configure(background="white")

#2. AJOUT DES ELEMENTS
image_logo = PhotoImage(file="assets/Logocryptomot2.png")
titre = Label(fenetre, image=image_logo, background="white",)
titre.place(x=434,y=0)
label_mot_crypte = Label(fenetre, text= "Mot a crypter : ", background="white")
label_mot_crypte.place(x=200,y=608)
mot_a_coder_rentre = StringVar()
entry_mot_a_coder = Entry(fenetre, textvariable=mot_a_coder_rentre, width=15)
entry_mot_a_coder.place(x=285,y=608)
label_mot_decrypte = Label(fenetre, text= "Mot a décrypter : ", background="white")
label_mot_decrypte.place(x=1034,y=608)
mot_a_decoder_rentre = StringVar()
entry_mot_a_decoder = Entry(fenetre, textvariable=mot_a_decoder_rentre, width=15)
entry_mot_a_decoder.place(x=1132,y=608)
label_cle_1 = Label(fenetre, text= "Clé : ", background="white")
label_cle_1.place(x=200,y=628)
code_cle = StringVar()
entry_code_cle = Entry(fenetre, textvariable=code_cle, width=15)
entry_code_cle.place(x=285,y=628)
label_cle_2 = Label(fenetre, text= "Clé : ", background="white")
label_cle_2.place(x=1034,y=628)
decode_cle = StringVar()
entry_decode_cle = Entry(fenetre, textvariable=decode_cle, width=15)
entry_decode_cle.place(x=1132,y=628)

#3. AJOUT DES IMAGES DE CADENAS

cad_ferme = PhotoImage(file ="assets/CadFermé.png")
label_cad_ferme = Label(fenetre, image = cad_ferme, background = "white").place(x=200, y=355)

cad_ouvert= PhotoImage(file ="assets/CadOuvert.png")
label_cad_ouvert = Label(fenetre, image = cad_ouvert, background = "white").place(x=1034, y=355)

#4. CREATION BOUTONS

bouton_crypte = Button(text="CRYPTER", width = 24,)
bouton_crypte.place(x=200,y=658)

bouton_crypte_doc=Button(text="DOCUMENT",width=24,).place(x=200,y=690)

boutton_decrypte = Button(text="DECRYPTER", width = 26,)
boutton_decrypte.place(x=1034,y=658)

bouton_decrypte_doc=Button(text="DOCUMENT",width=26,).place(x=1034,y=690)

bouton_quitter = Button(fenetre, text="Quitter", command=fenetre.destroy, height = 5, width = 20)
bouton_quitter.place (x=605, y=600)

boutton_motdepasse=Button(fenetre,text="Mot de passe",width=20).place(x=605,y=570)

boutton_Aide= Button(fenetre, text="AIDE",width = 20,command=AfficherAide).place(x=605,y=690)

ligne = Canvas(fenetre, width = "2", height ="195", background = "black")
ligne.place(x=675,y=355)

icon_mid = PhotoImage(file="assets/login.png")
label_photo_mid=Label(fenetre, image = icon_mid, anchor="center", background="white").place(x=662, y=525)

icon = "assets/lock.ico"
fenetre.iconbitmap(icon)
fenetre.mainloop()