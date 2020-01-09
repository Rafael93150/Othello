"""
OTHELLO

TAVARES Rafael
FRIH Rayen

Jeu complet
"""

import copy
from os import system
import os
import platform
import json
from json import dumps, loads


##########################PARTIE1#################################


def indice_valide(plateau,indice):
    if indice <= (plateau["n"]-1) and indice >= 0: #vérifie que l'indice est compris entre 0 et n la longeur max du tableau
        return True
    return False


def case_valide (plateau, i, j):
    if indice_valide(plateau,i) and indice_valide(plateau,j):  #vérifie que l'indice i et j sont compris entre 0 et n la longeur max du tableau
        return True
    return False


def get_case(plateau,i,j):
    assert case_valide(plateau,i,j) #si la case est valide
    return plateau["cases"][plateau["n"]*i+j] #retourne la valeur de la case


def set_case(plateau,i,j,val):
    assert case_valide(plateau,i,j) and 0 <= val and val <= 2 # si la case est valide et que la valeur est compris entre 0 et 2
    plateau["cases"][plateau["n"]*i+j]=val #change la valeursur de la case en la valeur mit en paramètre
    return plateau


def creer_plateau(n):
    assert n==4 or n==6 or n==8 #n doit être égale a 4 et 6 et 8
    tab=[]
    i=0
    while i<n*n:
        tab.append(0) # on remplit le tableau de 0
        i=i+1
    plateau={"n":n,"cases":tab}
    set_case(plateau,n//2-1,n//2-1,2)# les coordonnées des pions centraux
    set_case(plateau,n//2-1,n//2,1)
    set_case(plateau,n//2,n//2-1,1)
    set_case(plateau,n//2,n//2,2)
    return plateau


def afficher_plateau(plateau):

    #Variables
    cpt_lig=0                   #Compteur de petites lignes
    plat=copy.deepcopy(plateau)
    n=plat["n"]
    etoiles_sep_lignes=n*8+1    #Nombre d'étoiles dans les séparations des grandes lignes
    nb_lignes=4*n               #Nombre total de petites lignes
    indice=0                    #Compteur de l'indice du plateau

    a=0
    while a<len(plat["cases"]):       #On remplace les 0,1,2 par des "N","B" et " " (vide)
        if plat["cases"][a]==1:
            plat["cases"][a]=("N")    #Remplace 1 par "N"
        if plat["cases"][a]==2:
            plat["cases"][a]=("B")    #Remplace 2 par "B"
        if plat["cases"][a]==0:
            plat["cases"][a]=(" ")    #Remplace 0 par " " (vide)
        a+=1

    while cpt_lig<nb_lignes+1:                         #Boucle qui change de petite ligne

        if cpt_lig%4==0:                               #Toutes les 4 petites lignes - Si le numéro de petite ligne est dans la table de 4
            etoile=0                                   #Compteur d'étoiles dans la séparation des grandes lignes
            while etoile<etoiles_sep_lignes:
                print("*",end="")                      #Boucle qui trace la ligne de séparation des grandes lignes
                etoile+=1
            print("")                                  #Revient à la ligne une fois la séparation tracée

        elif cpt_lig%4==2:                             #Si la ligne est située 2 lignes en dessous de la ligne de séparation des grandes lignes
            cpt=0
            while cpt<n:                               #Si la petite ligne correspond à la ligne qui contient les valeurs
                print("*  ",plat["cases"][indice],"  ",end="")   #Place les étoiles espacées permettant de séparer les colonnes ainsi que la valeur de la case
                cpt+=1
                indice+=1
            print("*")                       #Ajoute la derniere étoile de la ligne et revient à la ligne

        else:                                #Si la petite ligne ne correspond pas à la ligne du centre des grandes lignes
            cpt=0
            while cpt<n:
                print("*       ",end="")     #Place les étoiles espacées permettant de séparer les colonnes
                cpt+=1
            print("*")                       #Place la dernière étoile de chaque ligne

        cpt_lig+=1









##############################PARTIE 2##########################








def pion_adverse(joueur):
    assert joueur==1 or joueur==2   #Vérifie que le joueur est valide
    if joueur==1:
        return 2    #Renvoie 1 si le joueur vaut 2 et renvoie 2 si le joueur vaut 1
    else:
        return 1

def test_pion_adverse():
    assert pion_adverse(1)==2   #Vérifie que la fonction renvoie bien 2 quand le joueur vaut 1
    assert pion_adverse(2)==1   #Vérifie que la fonction renvoie bien 1 quand le joueur vaut 2




def prise_possible_direction(p, i, j, vertical, horizontal, joueur):
    if not(case_valide(p,i+vertical,j+horizontal)): #Vérifie que la case qui doit être retournée est valide
        return False                                #Renvoie faux si ce n'est pas le cas
    if get_case(p,i+vertical,j+horizontal)==0 or get_case(p,i+vertical,j+horizontal)==joueur:
        return False                                #Vérifie que le pion qui est censé être rourné vaut 2 si c'est au tour du joueur 1 ou l'inverse
    v=vertical
    h=horizontal
    while case_valide(p,i+vertical+v,j+horizontal+h):       #Vérifie jusqu'où peut-on aller placer notre pion
        if get_case(p,i+vertical+v,j+horizontal+h)==joueur: #Cas où la case contient un pion du joueur à qui appartient le tour
            return True
        if get_case(p,i+vertical+v,j+horizontal+h)==0:      #Cas où la case est vide
            return False
        else:
            vertical=vertical+v
            horizontal=horizontal+h
    return False

def test_prise_possible_direction(p):
    if p["n"]==4:
        assert prise_possible_direction(p,1,3,0,-1,2)       # retourne True
        assert not prise_possible_direction(p,1,3,0,-1,1)   # retourne False
        assert not prise_possible_direction(p,1,3,-1,-1,2)  # retourne False
        assert prise_possible_direction(p,1,0,0,1,1)        # retourne True
    if p["n"]==6:
        assert prise_possible_direction(p,2,4,0,-1,2)       # retourne True
        assert not prise_possible_direction(p,2,4,0,-1,1)   # retourne False
        assert not prise_possible_direction(p,2,4,-1,-1,2)  # retourne False
        assert prise_possible_direction(p,2,1,0,1,1)        # retourne True
    if p["n"]==8:
        assert prise_possible_direction(p,3,5,0,-1,2)       # retourne True
        assert not prise_possible_direction(p,3,5,0,-1,1)   # retourne False
        assert not prise_possible_direction(p,3,5,-1,-1,2)  # retourne False
        assert prise_possible_direction(p,3,2,0,1,1)        # retourne True




def mouvement_valide(plateau, i, j, joueur):
    if not(get_case(plateau,i,j)==0):   #Vérifie que la valeur de la case est 0
        return False
    v=-1
    while v<=1:
        h=-1
        while h<=1:
            if prise_possible_direction(plateau,i,j,v,h,joueur):    #Vérifie qu'il existe une prise possible de direction
                return True
            h=h+1
        v=v+1
    return False    #Renvoie faux si aucune direction n'est possible

def test_mouvement_valide(p):
    if p["n"]==4:
        assert mouvement_valide(p,1,3,2) # retourne True
        assert not mouvement_valide(p,0,0,1) # retourne False
    if p["n"]==6:
        assert mouvement_valide(p,2,4,2) # retourne True
        assert not mouvement_valide(p,0,0,1) # retourne False
    if p["n"]==8:
        assert mouvement_valide(p,3,5,2) # retourne True
        assert not mouvement_valide(p,0,0,1) # retourne False




def mouvement_direction(plateau, i, j, vertical, horizontal, joueur):
    if prise_possible_direction(plateau,i,j,vertical,horizontal,joueur):
        v=vertical
        h=horizontal
        while get_case(plateau,i+vertical,j+horizontal)==pion_adverse(joueur):
            set_case(plateau,i+vertical,j+horizontal,joueur)
            vertical=vertical+v
            horizontal=horizontal+h
    return plateau

def test_mouvement_direction(p):
    if p["n"]==4:
        p4_1=copy.deepcopy(p) # crée deux copies du plateau principal
        p4_2=copy.deepcopy(p)
        mouvement_direction(p4_1,0,3,-1,1,2) # ne modifie rien
        assert p4_1["cases"]==p["cases"]     # vérifie que le plateau n'a pas été modifié
        mouvement_direction(p4_2,1,3,0,-1,2) # met la valeur 2 dans la case (1,2)
        assert p4_2["cases"][1*4+3-1]==2     # vérifie que la case a bien été modifiée
    if p["n"]==6:
        p6_1=copy.deepcopy(p) # crée deux copies du plateau principal
        p6_2=copy.deepcopy(p)
        mouvement_direction(p6_1,1,4,-1,1,2) # ne modifie rien
        assert p6_1["cases"]==p["cases"]     # vérifie que le plateau n'a pas été modifié
        mouvement_direction(p6_2,2,4,0,-1,2) # met la valeur 2 dans la case (2,3)
        assert p6_2["cases"][2*6+4-1]==2     # vérifie que la case a bien été modifiée
    if p["n"]==8:
        p8_1=copy.deepcopy(p) # crée deux copies du plateau principal
        p8_2=copy.deepcopy(p)
        mouvement_direction(p8_1,2,5,-1,1,2) # ne modifie rien
        assert p8_1["cases"]==p["cases"]     # vérifie que le plateau n'a pas été modifié
        mouvement_direction(p8_2,3,5,0,-1,2) # met la valeur 2 dans la case (3,4)
        assert p8_2["cases"][3*8+5-1]==2     # vérifie que la case a bien été modifiée




def mouvement(plateau, i, j, joueur):
    if mouvement_valide(plateau, i, j, joueur): #Vérifie que le mouvement est valide
        set_case(plateau,i,j,joueur)            #Place le pion dans la case (i,j)
        v=-1
        while v<=1:
            h=-1
            while h<=1:
                mouvement_direction(plateau,i,j,v,h,joueur)
                h=h+1
            v=v+1
    return plateau

def test_mouvement(p):
    if p["n"]==4:
        p4_1=copy.deepcopy(p) # crée deux copies du plateau principal
        p4_2=copy.deepcopy(p)
        mouvement(p4_1,0,3,2)               # ne modifie rien
        assert p4_1["cases"]==p["cases"]    # vérifie que le plateau n'a pas été modifié
        mouvement(p4_2,1,3,2)               # met la valeur 2 dans la case (1,2) et la case (1,3)
        assert p4_2["cases"][1*4+3-1]==2 and p4_2["cases"][1*4+3]==2     # vérifie que les cases ont bien été modifiées
    if p["n"]==6:
        p6_1=copy.deepcopy(p) # crée deux copies du plateau principal
        p6_2=copy.deepcopy(p)
        mouvement(p6_1,1,4,2)               # ne modifie rien
        assert p6_1["cases"]==p["cases"]    # vérifie que le plateau n'a pas été modifié
        mouvement(p6_2,2,4,2)               # met la valeur 2 dans la case (2,3) et la case (2,4)
        assert p6_2["cases"][2*6+4-1]==2 and p6_2["cases"][2*6+4]==2    # vérifie que les cases ont bien été modifiées
    if p["n"]==8:
        p8_1=copy.deepcopy(p) # crée deux copies du plateau principal
        p8_2=copy.deepcopy(p)
        mouvement(p8_1,2,5,2)               # ne modifie rien
        assert p8_1["cases"]==p["cases"]    # vérifie que le plateau n'a pas été modifié
        mouvement(p8_2,3,5,2)               # met la valeur 2 dans la case (3,4) et la case (3,5)
        assert p8_2["cases"][3*8+5-1]==2 and p8_2["cases"][3*8+5]==2     # vérifie que les cases ont bien été modifiées




def joueur_peut_jouer(plateau,joueur):
    i=0
    while i<plateau['n']:
        j=0                     #Pour toutes les cases de plateau
        while j<plateau['n']:
            if mouvement_valide(plateau,i,j,joueur):    #Renvoie Vrai si un mouvement est possible dans l'ensemble du plateau
                return True
            j=j+1
        i=i+1
    return False

def test_joueur_peut_jouer(p):
    if p["n"]==4:
        assert joueur_peut_jouer(p,1)   # retourne True
        p4=copy.deepcopy(p) # On fait une copie du plateau pour la suite du test
        set_case(p4,1,1,1)  # On remplace les pions du joueur 2 par des pions du joueur 1
        set_case(p4,2,2,1)
        assert not joueur_peut_jouer(p4,1)    # retourne False
    if p["n"]==6:
        assert joueur_peut_jouer(p,1)   # retourne True
        p6=copy.deepcopy(p) # On fait une copie du plateau pour la suite du test
        set_case(p6,2,2,1)  # On remplace les pions du joueur 2 par des pions du joueur 1
        set_case(p6,3,3,1)
        assert not joueur_peut_jouer(p6,1)    # retourne False
    if p["n"]==8:
        assert joueur_peut_jouer(p,1)   # retourne True
        p8=copy.deepcopy(p) # On fait une copie du plateau pour la suite du test
        set_case(p8,3,3,1)  # On remplace les pions du joueur 2 par des pions du joueur 1
        set_case(p8,4,4,1)
        assert not joueur_peut_jouer(p8,1)    # retourne False




def fin_de_partie(plateau):
    if (joueur_peut_jouer(plateau,1)==False) and (joueur_peut_jouer(plateau,2)==False):
        return True #Renvoie Vrai si aucun des joueurs ne peut jouer
    return False

def test_fin_de_partie(p):
    if p["n"]==4:
        assert not fin_de_partie(p)   # retourne False
        p4=copy.deepcopy(p) # On fait une copie du plateau pour la suite du test
        set_case(p4,1,1,1)  # On remplace les pions du joueur 2 par des pions du joueur 1
        set_case(p4,2,2,1)
        assert fin_de_partie(p4)    # retourne True
    if p["n"]==6:
        assert not fin_de_partie(p)   # retourne False
        p6=copy.deepcopy(p) # On fait une copie du plateau pour la suite du test
        set_case(p6,2,2,1)  # On remplace les pions du joueur 2 par des pions du joueur 1
        set_case(p6,3,3,1)
        assert fin_de_partie(p6)    # retourne True
    if p["n"]==8:
        assert not fin_de_partie(p)   # retourne False
        p8=copy.deepcopy(p) # On fait une copie du plateau pour la suite du test
        set_case(p8,3,3,1)  # On remplace les pions du joueur 2 par des pions du joueur 1
        set_case(p8,4,4,1)
        assert fin_de_partie(p8)    # retourne True




def gagnant(plateau):
    j1=0
    j2=0    #Création d'un compteur de pion pour chaque joueur
    i=0
    while i<len(plateau['cases']):      #Fait un balayage de l'ensemble du plateau
        if plateau['cases'][i]==1:      #Si la case contient la valeur 1, ajoute 1 au score du joueur 1
            j1=j1+1
        elif plateau['cases'][i]==2:    #Si la case contient la valeur 2, ajoute 1 au score du joueur 2
            j2=j2+1
        i=i+1
    if j1==j2:      #Renvoie 0 si les scores des deux joueurs sont égaux
        return 0
    if j1>j2:       #Renvoie 1 si le score du premier joueur est superieur à celui du second
        return 1
    else:           #Renvoie 2 dans le cas contraire (si c'est le 2eme joueur qui a le plus de points)
        return 2

def test_gagnant(p):
    if p["n"]==4:
        assert gagnant(p)==0 # vérifie qu'il y a égalité (que la fonction renvoie 0)
        p4=copy.deepcopy(p)
        set_case(p4,1,1,1)   # On remplace les pions du joueur 2 par des pions du joueur 1
        set_case(p4,2,2,1)
        assert gagnant(p4)==1 # retourne 1
    if p["n"]==6:
        assert gagnant(p)==0 # vérifie qu'il y a égalité (que la fonction renvoie 0)
        p6=copy.deepcopy(p)
        set_case(p6,3,3,1)   # On remplace les pions du joueur 2 par des pions du joueur 1
        set_case(p6,2,2,1)
        assert gagnant(p6)==1 # retourne 1
    if p["n"]==8:
        assert gagnant(p)==0 # vérifie qu'il y a égalité (que la fonction renvoie 0)
        p8=copy.deepcopy(p)
        set_case(p8,3,3,1)   # On remplace les pions du joueur 2 par des pions du joueur 1
        set_case(p8,4,4,1)
        assert gagnant(p8)==1 # retourne 1











##########################PARTIE3################################










def creer_partie(n):
    joueur=1    #on initialise le joueur à 1 comme c'est lui qui commence à jouer
    partie={"joueur":joueur, "plateau":creer_plateau(n)}
    #crée un dictionnaire qui contient le joueur ainsi que le dictionnaire plateau crée par la fonction creer_plateau
    return partie   #renvoie le dictionnaire

def test_creer_partie():
    print("test de la fonction creer_partie()")
    #Vérifie pour chaque taille de plateau que la fonction creer partie renvoie un plateau qui a la bonne taille
    assert len(creer_partie(4)["plateau"]["cases"])==4*4
    assert len(creer_partie(6)["plateau"]["cases"])==6*6
    assert len(creer_partie(8)["plateau"]["cases"])==8*8
    assert "joueur" and "plateau" in creer_partie(4)
    assert "joueur" and "plateau" in creer_partie(6)
    assert "joueur" and "plateau" in creer_partie(8)




def saisie_valide(partie, s):
    if ((ord(s[0])>=97 and ord(s[0])<=(97+partie["plateau"]["n"]) and int(s[1])>0 and int(s[1])<= partie["plateau"]["n"]and mouvement_valide(partie["plateau"],ord(s[0])-97,int(s[1])-1,partie["joueur"])==True) or s=="M"):
        #renvoie Vrai lorsque ces 3 conditions sont respectées:
        # - le code ascii du premier caractere de s correspond à une lettre entre a, d (si n=4), f (si n=6), h (si n=8)
        # - le deuxieme caractere est un nombre entier entre 1 et n
        # - le mouvement est valide
        #ou alors si s correspond à "M"
        return True
    return False    #renvoie Faux dans le cas contraire

def test_saisie_valide():
    print("test de la fonction saisie_valide()")
    assert saisie_valide(creer_partie(4),"b1")
    assert saisie_valide(creer_partie(4),"c4")
    assert saisie_valide(creer_partie(4),"M")
    assert not saisie_valide(creer_partie(4),"a1")
    assert not saisie_valide(creer_partie(4),"d1")



def tour_jeu(partie):
    print("Au tour du joueur", partie["joueur"])                #indique à qui est le tour
    afficher_plateau(partie["plateau"])                         #affiche le plateau
    if joueur_peut_jouer(partie["plateau"],partie["joueur"]):   #vérifie que le joueur peut jouer
        s=input("Choisissez un mouvement ")                     #demande un mouvement et le stock dans la variable "s"
        while saisie_valide(partie,s)==False:                   #redemande un mouvement tant que la saisie n'est pas valide
            s=input("Mouvement invalide. Recommencez ")
        if s=="M":                                              #renvoie faux si la saisie vaut "M"
            return False
        i=ord(s[0])-97                                          #récupère les valeurs de i et j
        j=int(s[1])-1
        mouvement(partie["plateau"],i,j,partie["joueur"])       #modifie le plateau selon le mouvement
        return True                                             #renvoie Vrai

def test_tour_jeu(partie):
    print("test de la fonction tour_jeu()")
    tour_jeu(partie)
    afficher_plateau(partie["plateau"]) 




def effacer_terminal():
    if platform.system() == "Windows":  #si le systeme d'exploitation est windows,
        system('cls')                   #supprime la console windows
    elif platform.system() == "Linux":  #si le systeme d'exploitation est linux,
        system('clear')                 #supprime la console linux




def saisir_action(partie):
    print("Actions\n- 0: terminer le jeu\n- 1: commencer une nouvelle partie\n- 2: charger une partie\n- 3: sauvegarder la partie en cours (partie en cours)\n- 4: reprendre la partie en cours (partie en cours)\n")
    n=int(input("Quelle action souhaitez vous effectuer? Action numéro: "))
    if partie is None:          #s'il n'y a pas de partie en cours, demande une saisie comprise entre 0 et 2
        while n<0 or n>2:
            n=int(input("Choisissez une action comprise entre 0 et 2 inclus "))
    else:
        while n<0 or n>4:       #s'il n'y a pas de partie en cours, demande une saisie comprise entre 0 et 4
            n=int(input("Choisissez une action comprise entre 0 et 4 inclus "))
    effacer_terminal()
    return n                    #renvoie n

def test_saisir_action():
    print("test de la fonction saisir_action()")
    assert 0<=saisir_action(None)<=2
    assert 0<=saisir_action(creer_partie(4))<=4




def jouer(partie) :
    while tour_jeu(partie)==True and fin_de_partie(partie["plateau"])==False:   #vérifie que la partie est en cours
        if joueur_peut_jouer(partie["plateau"],pion_adverse(partie["joueur"]))==True:
            partie["joueur"]=pion_adverse(partie["joueur"])     #change le tour de jeu si le joueur adverse peut joueur
        effacer_terminal()
    if fin_de_partie(partie["plateau"])==True:      #vérifie que la partie est terminée
        effacer_terminal()                          #efface la console
        afficher_plateau(partie["plateau"])         #affiche le plateau
        if gagnant(partie["plateau"])==0:
            print("Egalité")                        #affiche "Egalité" si la fonction gagnant renvoie 0
        else:
            print("Le joueur",gagnant(partie["plateau"]),"a gagné")     #affiche le gagnant selon la valeur renvoyée par la fonction gagnant
            print("")   #saute une ligne (pour l'esthétique)
        return True     #renvoie Vrai
    else:
        effacer_terminal()
        return False    #renvoie Faux

def test_jouer():
    print("test de la fonction jouer()")
    jouer(creer_partie(4))




def saisir_taille_plateau():
    n=int(input("Choisissez une taille de plateau (4, 6 ou 8)"))    #demande la taille du plateau à l'utilisateur et la stocke
    while n!=4 and n!=6 and n!=8:   #redemande à l'utilisateur de saisir une taille valide si elle est différente de 4,6 ou 8
        n=int(input("Choisissez une taille de plateau (4, 6 ou 8)"))
    effacer_terminal()
    return n    #renvoie la taille du plateau

def test_saisir_taille_plateau():
    print("test de la fonction saisir_taille_plateau()")
    assert saisir_taille_plateau()==4 or 6 or 8




def sauvegarder_partie(partie):
    s=dumps(partie)                         #réalise la copie brute du dictionnaire "partie" et la stocke dans "s"
    f=open("sauvegarde_partie.json","w")    #ouvre le fichier "sauvegarde_partie.json" en tant qu'écriture
    f.write(s)                              #écrit dans le fichier la forme brute de "s"
    f.close                                 #ferme le fichier

def test_sauvegarder_partie():
    print("test de la fonction sauvegarder_partie()")
    sauvegarder_partie(creer_partie(4))





def charger_partie():
    if os.path.exists("sauvegarde_partie.json"):    #vérifie que le fichier existe
        f=open("sauvegarde_partie.json","r")        #ouvre le fichier "sauvegarde_partie.json" en tant que lecture
        sauv=f.read()                               #stocke le contenu du fichier dans la variable "sauv"
        f.close()                                   #ferme le fichier
        sauv=loads(sauv)                            #récupère le dictionnaire depuis la chaine de caracteres de la variable
        return sauv                                 #renvoie le dicionnaire
    else:
        return creer_partie(4)                      #si le fichier n'existe pas, crée une nouvelle partie

def test_charger_partie():
    print("test de la fonction charger_partie()")
    assert(charger_partie())==creer_partie(4)





def othello():
    saisie=saisir_action(None)  #prend la valeur de la saisie compris entre 0 et 2 (partie toujours pas commencé)
    if saisie==1:
        partie=creer_partie(saisir_taille_plateau())    #si la saisie vaut 1, crée une partie dont la taille va être saisie et la stocke dans la variable "partie"
    elif saisie==2:
        partie=charger_partie()     #si la saisie vaut 2, charge une partie si elle existe ou alors crée une partie
    elif saisie==0:
        return "fin"                #si la saisie vaut 0, quitte la fonction en renvoyant "fin"

    while saisie!=0:                #ne rentre pas dans la boucle si la saisie vaut 0
        jeu=jouer(partie)           #lance la fonction jeu et stocke la valeur booléenne renvoyée dans la variable "jeu"
        if jeu==False:
            effacer_terminal()
            saisie=saisir_action(partie)    #si jouer renvoie Faux, efface le terminal et appelle la fonction saisir_action
        elif jeu==True:
            saisie=saisir_action(partie)    #si jouer renvoie Vrai, appelle la fonction saisir_action mais n'efface pas le terminal

        if saisie==1:
            partie=creer_partie(saisir_taille_plateau())    #si la saisie vaut 1, crée une partie
        elif saisie==2:
            partie=charger_partie()                         #si la saisie vaut 2, charge la partie sauvegardée
        elif saisie==3:
            sauvegarder_partie(partie)                      #si la saisie vaut 3, sauvegarde la partie

def test_othello():
    print("test de la fonction othello()")
    othello()


"""programme principal"""


#######TESTS#######

test_creer_partie()
test_saisie_valide()
test_tour_jeu(creer_partie(4))
test_saisir_action()
test_jouer()
test_saisir_taille_plateau()

test_sauvegarder_partie()      #test_sauvegarder_partie() et test_charger_partie() fonctionnent ensemble
test_charger_partie()

test_othello()


#######JOUER#######

#othello()