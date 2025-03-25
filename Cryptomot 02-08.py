Version="2.08"

import tkinter as tk
from time import *
from tkinter import *

# Creéation des fonctions
def texte_aide (version) :
    ''' Renvoie le texte à afficher dans la fenetre aide, en fonction, de la
        version du programme'''
    fichier = open("assets/aide.txt",'r')
    lecture=fichier.read()
    lecture="Version : "+version+"\n"+lecture
    fichier.close
    return lecture

def AfficherAide ():
    '''Affiche la fenetre aide grace à la fonction 'texte_aide'
    '''
    FenetreAide=Toplevel(fenetre, height=680, width=1300)
    FenetreAide.title("Aide")
    FenetreAide.resizable(width=False, height=False)
    FenetreAide.configure(background="white")
    aide=texte_aide(Version)
    label_aide=Label(FenetreAide,text=texte_aide(Version),font="Arial 11",background="white", justify = "left").place(x=10,y=10)
    boutton_quitter_aide=Button(FenetreAide, text="Quitter", command=FenetreAide.destroy, height = 5, width = 20).place(x=605,y=550)

def de_cryptage_mot (mot,cle,mode=0) :
    ''' Prend un mot (phrase) et une clé et renvoie le mot crypté/décrypté avec la clé
        sous la forme /mot (dé)crypté/.
        mode==0 : cryptage // mode==1 : décryptage
        Renvoie 0 si un des deux parametres est vide.
        Renvoie 1 si une lettre du mot n'est pas acceptée.
        Renvoie 2 si une lettre de la clé n'est pas acceptée. '''
    liste_mot=[] ## liste d'entier correspondant aux lettres du mot
    liste_cle=[] ## liste d'entier correspondant aux lettres de la cle
    result="" ##Futur mot codé / décodé
    if len(mot)==0 or len(cle)==0 : ##retourne 0 si variable vide
        return 0
    else : ##si aucune variable vide
        for k in mot : ## k prend la valeur de la lettre à modifier dans le mot, une par une
            x=ord(k) ##x prend la valeur ASCII de la lettre k
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
            liste_mot.append(x)

        for k in cle : ## k prend la valeur de la lettre à modifier dans la cle, une par une
            x=ord(k) ##x prend la valeur ASCII de la lettre k
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
                return 2
            liste_cle.append(x)

        while len(liste_cle)<len(liste_mot): ##On agrandit la clé en la multipliant
            liste_cle=liste_cle+liste_cle

        if mode==0 :
            for k in range(len(liste_mot)):
                x=liste_mot[k]+liste_cle[k]##On additionne les lettres de la clé et du mot
                if x>64 : ## on la remet entre 1 et 64 (dans notre alphabet) si elle est au dessus
                    x=x-64
                # On ramène aux numéros de la table ASCII
                if x>0 and x<27 : ##Si c'est une minuscule, on lui donne une valeur de 97 à 122
                    x=x+96
                elif x>26 and x<53 : ##Si c'est une majuscule, on lui donne une valeur de 65 à 91
                    x=x+38
                elif x==64 : ##Si c'est un espace, on lui donne 32 comme valeur
                    x=32
                elif x ==63 : ## Si c'est un point, on lui donne 46
                    x=46
                elif x>52 and x<63 : ##Si c'est un nombre, on le ramenne entre 48 et 57
                    x=x-5
                x=chr(x) ##Puis on l'a remet en lettre
                result=result+x
        elif mode==1:
            for k in range(len(liste_mot)):
                x=liste_mot[k]-liste_cle[k]##On additionne les lettres de la clé et du mot
                if x<1 : ## on la remet entre 1 et 64 (dans notre alphabet) si elle est au dessus
                    x=x+64
                # On ramène aux numéros de la table ASCII
                if x>0 and x<27 : ##Si c'est une minuscule, on lui donne une valeur de 97 à 122
                    x=x+96
                elif x>26 and x<53 : ##Si c'est une majuscule, on lui donne une valeur de 65 à 91
                    x=x+38
                elif x==64 : ##Si c'est un espace, on lui donne 32 comme valeur
                    x=32
                elif x ==63 : ## Si c'est un point, on lui donne 46
                    x=46
                elif x>52 and x<63 : ##Si c'est un nombre, on le ramenne entre 48 et 57
                    x=x-5
                x=chr(x) ##Puis on l'a remet en lettre
                result=result+x
        result="/"+result+"/"
        return result

def fonction_boutton_coder () :
    '''Ecrit le mot codé dans la console et le marque dans la fenetre
    '''
    mot= mot_a_coder_rentre.get()
    cle= code_cle.get()
    entry_code_cle.delete(0, END)
    entry_mot_a_coder.delete(0, END)
    result=de_cryptage_mot(mot,cle,0)
    if type(result)== str : #Si il n'y a pas d'erreur
        print("mot codé : ",result)
        label_result = Label(fenetre, text=result, font = "Centaur 33", foreground ="blue", background="white", justify=CENTER, width="59").place(x=0, y=494)
        label_cad_ouvert = Label(fenetre, image = cad_ouvert, background = "white").place(x=1034, y=355)
        label_cad_ferme = Label(fenetre, image = cad_ferme, background = "white").place(x=200, y=355)
    else :
        if result==0 :
            label_erreure = Label(fenetre, text="ERREUR, Variable(s) vide(s)", font = "Arial 30", foreground ="red", background="white", anchor="center", width="59").place(x=0, y=500)
            label_cad_ouvert = Label(fenetre, image = cad_ouvert, background = "white").place(x=1034, y=355)
            label_cad_ferme = Label(fenetre, image = cad_ferme, background = "white").place(x=200, y=355)
        else :
            label_erreure = Label(fenetre, text="ERREUR, Caractère spécial", font = "Arial 30", foreground ="red", background="white", anchor="center", width="59").place(x=0, y=500)
            label_cad_ouvert = Label(fenetre, image = cad_ouvert, background = "white").place(x=1034, y=355)
            label_cad_ferme = Label(fenetre, image = cad_ferme, background = "white").place(x=200, y=355)
    return

def fonction_boutton_decoder () :
    '''Ecrit le mot décodé dans la console et le marque dans la fenetre
    '''
    mot= mot_a_decoder_rentre.get()
    cle= decode_cle.get()
    entry_decode_cle.delete(0, END)
    entry_mot_a_decoder.delete(0, END)
    result=de_cryptage_mot(mot,cle,1)
    if type(result)== str : #Si il n'y a pas d'erreur
        print("mot décodé : ",result)
        label_result = Label(fenetre, text=result, font = "Centaur 33", foreground ="blue", background="white", justify=CENTER, width="59").place(x=0, y=494)
        label_cad_ouvert = Label(fenetre, image = cad_ouvert, background = "white").place(x=1034, y=355)
        label_cad_ferme = Label(fenetre, image = cad_ferme, background = "white").place(x=200, y=355)
    else :
        if result==0 :
            label_erreure = Label(fenetre, text="ERREUR, Variable(s) vide(s)", font = "Arial 30", foreground ="red", background="white", anchor="center", width="59").place(x=0, y=500)
            label_cad_ouvert = Label(fenetre, image = cad_ouvert, background = "white").place(x=1034, y=355)
            label_cad_ferme = Label(fenetre, image = cad_ferme, background = "white").place(x=200, y=355)
        else :
            label_erreure = Label(fenetre, text="ERREUR, Caractère spécial", font = "Arial 30", foreground ="red", background="white", anchor="center", width="59").place(x=0, y=500)
            label_cad_ouvert = Label(fenetre, image = cad_ouvert, background = "white").place(x=1034, y=355)
            label_cad_ferme = Label(fenetre, image = cad_ferme, background = "white").place(x=200, y=355)
    return

def fonction_boutton_coder_doc () :
    mot= mot_a_coder_rentre.get()
    cle= code_cle.get()
    fichier = open("documents/"+mot+".txt",'r')
    liste_lignes=fichier.readlines()
    fichier.close
    result_a_ecrire=""
    for element in liste_lignes : ##Pour toutes les lignes
        retour=False
        if element[-1] == '\n' : ##Si il y a un retour à la ligne on le retire et on retient qu'il y en a 1
            element=element[0:-1]
            retour=True
        ligne_code=cryptage_mot(element,cle) ##On code la ligne
        ligne_code=ligne_code[1:-1] ##On retire les /
        if retour==True :
            result_a_ecrire=result_a_ecrire+ligne_code+"\n" ##On remet le retour à la ligne
        else :
            result_a_ecrire=result_a_ecrire+ligne_code
    chemin="documents/"+mot+"_crypte.txt"
    fichier=open(chemin,'w')
    fichier.write(result_a_ecrire)
    fichier.close
    entry_code_cle.delete(0, END)
    entry_mot_a_coder.delete(0, END)
    print("Fichier crypté !")
    label_result = Label(fenetre, text="Fichier crypté !", font = "Centaur 33", foreground ="blue", background="white", justify=CENTER, width="59").place(x=0, y=494)
    label_cad_ouvert = Label(fenetre, image = cad_ouvert, background = "white").place(x=1034, y=355)
    label_cad_ferme = Label(fenetre, image = cad_ferme, background = "white").place(x=200, y=355)

def fonction_boutton_decoder_doc () :
    mot= mot_a_decoder_rentre.get()
    cle= decode_cle.get()
    fichier = open("documents/"+mot+".txt",'r')
    liste_lignes=fichier.readlines()
    fichier.close
    result_a_ecrire=""
    for element in liste_lignes : ##Pour toutes les lignes
        retour=False
        if element[-1] == '\n' : ##Si il y a un retour à la ligne on le retire et on retient qu'il y en a 1
            element=element[0:-1]
            retour=True
        ligne_decode=decryptage_mot(element,cle) ##On code la ligne
        ligne_decode=ligne_decode[1:-1] ##On retire les /
        if retour==True :
            result_a_ecrire=result_a_ecrire+ligne_decode+"\n" ##On remet le retour à la ligne
        else :
            result_a_ecrire=result_a_ecrire+ligne_decode
    chemin="documents/"+mot+"_decrypte.txt"
    fichier=open(chemin,'w')
    fichier.write(result_a_ecrire)
    fichier.close
    entry_decode_cle.delete(0, END)
    entry_mot_a_decoder.delete(0, END)
    print("Fichier décrypté !")
    label_result = Label(fenetre, text="Fichier décrypté !", font = "Centaur 33", foreground ="blue", background="white", justify=CENTER, width="59").place(x=0, y=494)
    label_cad_ouvert = Label(fenetre, image = cad_ouvert, background = "white").place(x=1034, y=355)
    label_cad_ferme = Label(fenetre, image = cad_ferme, background = "white").place(x=200, y=355)

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
bouton_crypte = Button(text="CRYPTER", width = 24,command=fonction_boutton_coder)
bouton_crypte.place(x=200,y=658)

bouton_crypte_doc=Button(text="DOCUMENT",width=24,command=fonction_boutton_coder_doc).place(x=200,y=690)

boutton_decrypte = Button(text="DECRYPTER", width = 26,command=fonction_boutton_decoder)
boutton_decrypte.place(x=1034,y=658)

bouton_decrypte_doc=Button(text="DOCUMENT",width=26,command=fonction_boutton_decoder_doc).place(x=1034,y=690)

bouton_quitter = Button(fenetre, text="Quitter", command=fenetre.destroy, height = 5, width = 20)
bouton_quitter.place (x=605, y=600)

boutton_Aide= Button(fenetre, text="AIDE",width = 20,command=AfficherAide).place(x=605,y=690)

ligne = Canvas(fenetre, width = "2", height ="195", background = "black")
ligne.place(x=675,y=355)

icon_mid = PhotoImage(file="assets/login.png")
label_photo_mid=Label(fenetre, image = icon_mid, anchor="center", background="white").place(x=662, y=550)

icon = "assets/lock.ico"
fenetre.iconbitmap(icon)

#Affichage de la fenetre
fenetre.mainloop()