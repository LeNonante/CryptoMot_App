Version="1.26"

# CHOSES A FAIRE :

# DEFINITION FONCTIONS DE CRYPTAGE ET DECRYPTAGE
# A EST LE MOT A CODER / DECODER ET B EST LA CLE
import tkinter as tk
from time import *
from tkinter import *
a=""
b=""
mot_a_coder_rentre=""
mot_a_decoder_rentre=""
codecle=""
decodecle=""
result =""


def AfficherAide (): #Fonction creéant la fenetre aide
    FenetreAide=Toplevel(fenetre, height=680, width=1300)
    FenetreAide.title("Aide")
    FenetreAide.resizable(width=False, height=False)
    FenetreAide.configure(background="white")
    texte_aide="Version : "+Version+"\nPar MUSSET Aurélien\n\n\nExplications d'utilisation : - Ne pas tenir compte des points en début et fin du mot affiché, il servent à délimiter les mots pour ne pas oublier d'espaces au début ou à la fin\n - Ne pas confondre L minuscules et i majuscules et les zéros et les O\n - Utiliser seulement des lettres (majuscules et minuscules sans accents), des espaces, des chiffres et des points. (Donc aucun caractères spéciaux)\n"
    texte_aide=texte_aide+" - Si le mot codé/décodé est trop long, il peut y avoir des bug d'affichage\n - Le mot est disponible dans la console python pour le copier (et ne pas faire de faute)/le voir en entier\n - Ce cryptage est indécryptable à la main. A raison d'un calcul par seconde, un mot de 10 lettres prendrait 63^10 secondes afin de tester toutes les combinaisons possibles,\n   soit 3,12112242 * 10^10 années (plus de 30 milliards d'années)\n - Crypter / décrypter un document .txt (sans ligne vide) :\n      1) Mettre le doc dans le dossier 'documents'\n      2) Rentrer le nom du fichier (sans le .txt) dans la case 'mot à crypter / décrypter'\n      3) Rentrer la clé dans la case 'clé'\n      4) Cliquer sur le boutton 'DOCUMENT'\n      5) Un fichier 'NomDeVotreFichier_crypte.txt' ou 'NomDeVotreFichier_decrypte.txt' est créé dans le répertoire 'documents'"
    texte_aide=texte_aide+"\n\n\nNotes de mise à jour :\n - 1.15 : Passage de 1900 lignes de codes à 200 ; Plus de contraintes de taille de texte à coder\n - 1.16 : Ajout des messages d'erreur pour les variables vides et les caractères spéciaux\n - 1.17 : Ajout des boutons 'DOCUMENT' ; modification nom des variables\n - 1.18 : Ajout des fonctions 'cryptage_boutton', 'decryptage_boutton','cryptage_doc' et 'decryptage_doc'\n - 1.19 : Ajout fonctionnalité cryptage/ decryptage doc avec création d'un autre doc\n - 1.20 : Ajout message erreur caractère speciaux clé\n - 1.21 : Ajout des retour-à-la-ligne dans les caractères autorisés\n - 1.22 : Ajout messages 'Fichier crypté' et 'Fichier Décrypté'\n - 1.23 : Ajout des chiffres/points en caractères autorisés ; problème retour a la ligne\n - 1.24 : Changement de l'alphabet / Retour a la ligne retiré ; Tout est fonctionnel (sans les retours à la ligne)\n - 1.25 : Retours à la ligne rajoutés (chaque ligne étant codées indépendament et le document ne doit pas contenir de ligne vide) ; probleme, les fonctions 'cryptage_doc' et 'decryptage_doc' créent une ligne vide à la fin du document"
    texte_aide=texte_aide+"\n - 1.26 : Ajout du boutton 'mot de passe'"
    label_aide=Label(FenetreAide,text=texte_aide,font="Arial 11",background="white", justify = "left").place(x=10,y=10)
    boutton_quitter_aide=Button(FenetreAide, text="Quitter", command=FenetreAide.destroy, height = 5, width = 20).place(x=605,y=550)

def AffichetMotdepasse() : # foction qui cré la fenetre de mot de passe
    FenetreMdp=Toplevel(fenetre,height=680,width=1300)
    FenetreMdp.title("Mots de passe")
    FenetreMdp.resizable(width=False, height=False)
    FenetreMdp.configure(background="white")
    boutton_quitter_mdp=Button(FenetreMdp, text="Quitter", command=FenetreMdp.destroy, height = 5, width = 20).place(x=605,y=550)

    ligne_motdepasse = Canvas(FenetreMdp, width = "2", height ="500", background = "black")
    ligne_motdepasse.place(x=675,y=50)


def cryptage(a,b,c) : #Fonction pour crypter, appellé par fonction cryptage_bouton
        result=""
        nblettrea = len(a)
        nblettreb = len(b)
        y=0 # Place de la lettre a utiliser dans la clé

        if nblettrea!=0 and nblettreb!=0 : #Test variable(s) vide(s) pour message erreur
                for k in a :
                    x=ord(k) # x vaut la valeur de la lettre en table ASCII
                    if x==32 : #Si c'est un espace, on lui donne 64 comme valeur
                        x=64
                    elif x>64 and x<91 : # Si c'est une majuscule, on rammène de 27 à 52
                        x=x-38
                    elif x>96 and x<123 :#Si c'est une minuscule, on ramène de 1 à 26
                        x=x-96
                    elif x==46 : #Si c'est un point on lui donne 63
                        x=63
                    elif x>47 and x<58 : #Si c'est un chiffre on le met entre 53 et 62
                        x=x+5
                    else : #Erreur caractère special mot a coder
                        label_erreure = Label(fenetre, text="ERREUR, Caractère spécial", font = "Arial 30", foreground ="red", background="white", anchor="center", width="59").place(x=0, y=500)
                        label_cadouvert = Label(fenetre, image = cad_ouvert, background = "white").place(x=1034, y=355)
                        label_cadferme = Label(fenetre, image = cad_ferme, background = "white").place(x=200, y=355)
                        entry_code_cle.delete(0, END)
                        entry_mot_a_coder.delete(0, END)
                        return

                    if y >= nblettreb :
                        y=y-nblettreb
                    z=b[y] # z vaut la valeur de la lettre en table ascii
                    z=ord(z)
                    if z==32 : #Si c'est un espace, on lui donne 64 comme valeur
                        z=64
                    elif z>64 and z<91 : # Si c'est une majuscule, on rammène de 27 à 52
                        z=z-38
                    elif z>96 and z<123 :#Si c'est une minuscule, on ramène de 1 à 26
                        z=z-96
                    elif z==46 : #Si c'est un point on lui donne 63
                        z=63
                    elif z>47 and z<58 : #Si c'est un chiffre on le met entre 53 et 62
                        z=z+5
                    else : #Erreur caractère special clé
                        label_erreure = Label(fenetre, text="ERREUR, Caractère spécial", font = "Arial 30", foreground ="red", background="white", anchor="center", width="59").place(x=0, y=500)
                        label_cadouvert = Label(fenetre, image = cad_ouvert, background = "white").place(x=1034, y=355)
                        label_cadferme = Label(fenetre, image = cad_ferme, background = "white").place(x=200, y=355)
                        entry_code_cle.delete(0, END)
                        entry_mot_a_coder.delete(0, END)
                        return

                    zf=x+z  #zf est la valeur de la lettre après addition
                    if zf>64 : # on la remet entre 1 et 54 si lle est au dessus
                        zf=zf-64

                                # On ramène aux numéros de la table ASCII
                    if zf>0 and zf<27 : #Si c'est une minuscule, on lui donne une valeur de 97 à 122
                        zf=zf+96
                    elif zf>26 and zf<53 : #Si c'est une majuscule, on lui donne une valeur de 65 à 91
                        zf=zf+38
                    elif zf==64 : #Si c'est un espace, on lui donne 32 comme valeur
                        zf=32
                    elif zf ==63 : # Si c'est un point, on lui donne 46
                        zf=46
                    elif zf>52 and zf<63 : #Si c'est un nombre, on le ramenne entre 48 et 57
                        zf=zf-5
                    zf=chr(zf)

                    result=result+zf
                    y=y+1
                result="."+result+"."

                if c==1 :
                    label_result = Label(fenetre, text="Fichier cypté !", font = "Centaur 33", foreground ="blue", background="white", justify=CENTER, width="59").place(x=0, y=494)
                else :
                    print("mot codé : ",result)
                    label_result = Label(fenetre, text=result, font = "Centaur 33", foreground ="blue", background="white", justify=CENTER, width="59").place(x=0, y=494)
                label_cad_ouvert = Label(fenetre, image = cad_ouvert, background = "white").place(x=1034, y=355)
                label_cad_ferme = Label(fenetre, image = cad_ferme, background = "white").place(x=200, y=355)
                entry_code_cle.delete(0, END)
                entry_mot_a_coder.delete(0, END)
                return result
        else : #Message erreur varaible(s) vide(s)
            label_erreure = Label(fenetre, text="ERREUR, Variable(s) vide(s)", font = "Arial 30", foreground ="red", background="white", anchor="center", width="59").place(x=0, y=500)
            label_cad_ouvert = Label(fenetre, image = cad_ouvert, background = "white").place(x=1034, y=355)
            label_cad_ferme = Label(fenetre, image = cad_ferme, background = "white").place(x=200, y=355)

def decryptage (a,b,c) : #Fonction pour décrypter, appellée par decryptage_boutton
        result=""
        nblettrea = len(a)
        nblettreb = len(b)
        y=0 # Place de la lettre a utiliser dans la clé
        if nblettrea!=0 and nblettreb!=0 : #Test variable(s) vide(s) pour message erreur
            for k in a :
                x=ord(k) # x vaut la valeur de la lettre en table ASCII
                if x==32 : #Si c'est un espace, on lui donne 64 comme valeur
                    x=64
                elif x>64 and x<91 : # Si c'est une majuscule, on rammène de 27 à 52
                    x=x-38
                elif x>96 and x<123 :#Si c'est une minuscule, on ramène de 1 à 26
                    x=x-96
                elif x==46 : #Si c'est un point on lui donne 63
                    x=63
                elif x>47 and x<58 : #Si c'est un chiffre on le met entre 53 et 62
                    x=x+5
                else : #Erreur caractère special mot a décoder
                        label_erreure = Label(fenetre, text="ERREUR, Caractère spécial", font = "Arial 30", foreground ="red", background="white", anchor="center", width="59").place(x=0, y=500)
                        label_cad_ouvert = Label(fenetre, image = cad_ouvert, background = "white").place(x=1034, y=355)
                        label_cad_ferme = Label(fenetre, image = cad_ferme, background = "white").place(x=200, y=355)
                        entry_decode_cle.delete(0, END)
                        entry_mot_a_decoder.delete(0, END)
                        return

                if y >= nblettreb :
                    y=y-nblettreb

                z=b[y] # z vaut la valeur de la lettre en table ascii
                z=ord(z)
                if z==32 : #Si c'est un espace, on lui donne 64 comme valeur
                    z=64
                elif z>64 and z<91 : # Si c'est une majuscule, on rammène de 27 à 52
                    z=z-38
                elif z>96 and z<123 :#Si c'est une minuscule, on ramène de 1 à 26
                    z=z-96
                elif z==46 : #Si c'est un point on lui donne 63
                    z=63
                elif z>47 and z<58 : #Si c'est un chiffre on le met entre 53 et 62
                    z=z+5
                else : #Erreur caractère special clé
                        label_erreure = Label(fenetre, text="ERREUR, Caractère spécial", font = "Arial 30", foreground ="red", background="white", anchor="center", width="59").place(x=0, y=500)
                        label_cad_ouvert = Label(fenetre, image = cad_ouvert, background = "white").place(x=1034, y=355)
                        label_cad_ferme = Label(fenetre, image = cad_ferme, background = "white").place(x=200, y=355)
                        entry_decode_cle.delete(0, END)
                        entry_mot_a_decoder.delete(0, END)
                        return

                zf=x-z  #zf est la valeur de la lettre après soustraction
                if zf<1 : # on la remet entre 1 et 53 si lle en dessous
                    zf=zf+64

                            # On ramène aux numéros de la table ASCII
                if zf>0 and zf<27 : #Si c'est une minuscule, on lui donne une valeur de 97 à 122
                    zf=zf+96
                elif zf>26 and zf<53 : #Si c'est une majuscule, on lui donne une valeur de 65 à 91
                    zf=zf+38
                elif zf==64 : #Si c'est un espace, on lui donne 32 comme valeur
                    zf=32
                elif zf ==63 : # Si c'est un point, on lui donne 46
                    zf=46
                elif zf>52 and zf<63 : #Si c'est un nombre, on le ramenne entre 48 et 57
                    zf=zf-5

                zf=chr(zf)
                result=result+zf
                y=y+1

            result="."+result+"."

            if c==1 : #Si c'est un document
                label_result = Label(fenetre, text="Fichier décrypté !", font = "Centaur 33", foreground ="blue", background="white", justify=CENTER, width="59").place(x=0, y=494)
            else :
                print("mot décodé : ",result)
                label_result = Label(fenetre, text=result, font = "Centaur 33", foreground ="blue", background="white", justify=CENTER, width="59").place(x=0, y=494)
            label_cad_ouvert = Label(fenetre, image = cad_ouvert, background = "white").place(x=1034, y=355)
            label_cad_ferme = Label(fenetre, image = cad_ferme, background = "white").place(x=200, y=355)

            entry_decode_cle.delete(0, END)
            entry_mot_a_decoder.delete(0, END)
            return result
        else :#Message erreur varaible(s) vide(s)
            label_erreure = Label(fenetre, text="ERREUR, Variable(s) vide(s)", font = "Arial 30", foreground ="red", background="white", anchor="center", width="59").place(x=0, y=500)
            label_cad_ouvert = Label(fenetre, image = cad_ouvert, background = "white").place(x=1034, y=355)
            label_cad_ferme = Label(fenetre, image = cad_ferme, background = "white").place(x=200, y=355)



def cryptage_doc () :
    a=mot_a_coder_rentre.get()
    chemin="documents/"+a+".txt"
    fichier = open(chemin,'r')
    lecture=fichier.readlines()
    fichier.close
    b=code_cle.get()
    Liste_Ligne_a_ecrire=[]
    result_a_ecrire=""
    for element in lecture :
        if element[-1] == '\n' :
            element=element[0:-1]
        ligne_code=cryptage(element,b,1)
        ligne_code=ligne_code[1:-1]
        result_a_ecrire=result_a_ecrire+ligne_code+"\n"
    chemin="documents/"+a+"_crypte.txt"
    fichier=open(chemin,'w')
    fichier.write(result_a_ecrire)

def decryptage_doc () :
    a=mot_a_decoder_rentre.get()
    chemin="documents/"+a+".txt"
    fichier = open(chemin,'r')
    lecture=fichier.readlines()
    b=decode_cle.get()
    fichier.close
    Liste_Ligne_a_ecrire=[]
    result_a_ecrire=""
    for element in lecture :
        if element[-1] == '\n' :
            element=element[0:-1]
        ligne_decode=decryptage(element,b,1)
        ligne_decode=ligne_decode[1:-1]
        result_a_ecrire=result_a_ecrire+ligne_decode+"\n"
    chemin="documents/"+a+"_decrypte.txt"
    fichier=open(chemin,'w')
    fichier.write(result_a_ecrire)


def cryptage_boutton() :
    a=mot_a_coder_rentre.get()
    b=code_cle.get()
    cryptage(a,b,0)

def decryptage_boutton():
    a=mot_a_decoder_rentre.get()
    b=decode_cle.get()
    decryptage(a,b,0)

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

bouton_crypte = Button(text="CRYPTER", width = 24, command=cryptage_boutton)
bouton_crypte.place(x=200,y=658)

bouton_crypte_doc=Button(text="DOCUMENT",width=24,command=cryptage_doc).place(x=200,y=690)

boutton_decrypte = Button(text="DECRYPTER", width = 26, command=decryptage_boutton)
boutton_decrypte.place(x=1034,y=658)

bouton_decrypte_doc=Button(text="DOCUMENT",width=26,command=decryptage_doc).place(x=1034,y=690)

bouton_quitter = Button(fenetre, text="Quitter", command=fenetre.destroy, height = 5, width = 20)
bouton_quitter.place (x=605, y=600)

boutton_motdepasse=Button(fenetre,text="Mot de passe",command=AffichetMotdepasse,width=20).place(x=605,y=570)

boutton_Aide= Button(fenetre, text="AIDE",command=AfficherAide,width = 20).place(x=605,y=690)

ligne = Canvas(fenetre, width = "2", height ="195", background = "black")
ligne.place(x=675,y=355)

icon_mid = PhotoImage(file="assets/login.png")
label_photo_mid=Label(fenetre, image = icon_mid, anchor="center", background="white").place(x=662, y=525)

icon = "assets/lock.ico"
fenetre.iconbitmap(icon)
fenetre.mainloop()

