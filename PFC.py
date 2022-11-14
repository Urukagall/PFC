import random

#on admet une fonction random qui renvoie un nombre aléatoire entre un nombres x et un autre y
#on admet une fonction input qui renvoie ce que le joueur rentre

#Début

#définir la fonction PFC
    #initialise playerWin en booléen et sur False
    #initialise iaWin en booléen et sur False
    #initialise la variable ia avec la valeur retourner par l'éxecution de la fonction random qui prendra en argument x=0 et y=2
    #initialise la variable joueur avec le retour de l'éxecution de la fonction input
    #si la variable joueur est égale à 0,1 ou 2 qui correspond dans l'ordre a pierre, feuille et ciseaux
        #alors la variable joueur est convertit en integer
        #si la variable ennemie est égale a la variable
            #alors retourne "egalter"
        #ou sinon la variable ennemie est égale a la variable joueur plus 1 (l'ennemie gagne avec un ciseaux ou une feuille)
            #alors retourne "l'ennemie gane"
        #ou sinon la variable joueur est égale a la variable ennemie plus 1 (le joueur gagne avec un ciseaux ou une feuille)
            #alors retourne "le joueur gane"
        #ou sinon la variable ennemie est égale à 0 et la variable joueur est égale à 2 (l'ennemie gagne avec une pierre)
            #alors retourne "l'ennemie gane"
        #ou sinon la variable joueur est égale à 0 et la variable ennemie est égale à 2 (le joueur gagne avec une pierre)
            #alors retourne "le joueur gane"

#Fin

#Execution de la fonction PFC

def convertPFC(choice):
    if choice == 0:
        return "pierre"
    elif choice == 1:
        return "feuille"
    elif choice == 2:
        return "ciseaux"

def PFC(nbPuntos):
    nbPuntosJoueur=0
    nbPuntosEnnemie=0
    while nbPuntosJoueur < nbPuntos and nbPuntosEnnemie < nbPuntos :
        ennemie = random.randint(0,2)
        joueur = input("0- pierre\n1- feuille\n2- ciseaux\n")
        while joueur != "0" and  joueur != "1" and  joueur != "2" :
            print("dommage réessaie")
            joueur = input("0- Pierre\n1- feuille\n3- ciseaux\n")
        joueur = int(joueur)
        if ennemie == joueur :
            print("égalter" + " l'ennemie a " + str(nbPuntosEnnemie) + " Puntos" + " le joueur a " + str(nbPuntosJoueur) + " Puntos")
        elif ennemie == joueur + 1 :
            nbPuntosEnnemie += 1
            print("l'ennemie gane avec " + convertPFC(ennemie) + " l'ennemie a " + str(nbPuntosEnnemie) + " Puntos" + " le joueur a " + str(nbPuntosJoueur) + " Puntos")
        elif joueur == ennemie + 1 :
            nbPuntosJoueur += 1
            print("le joueur gane avec " + convertPFC(joueur) + " l'ennemie a " + str(nbPuntosEnnemie) + " Puntos" + " le joueur a " + str(nbPuntosJoueur) + " Puntos")
        elif ennemie == 0 and joueur == 2 :
            nbPuntosEnnemie += 1
            print("l'ennemie gane avec " + convertPFC(ennemie) + " l'ennemie a " + str(nbPuntosEnnemie) + " Puntos" + " le joueur a " + str(nbPuntosJoueur) + " Puntos")
        elif ennemie == 2 and joueur == 0 :
            nbPuntosJoueur += 1
            print("le joueur gane avec " + convertPFC(joueur) + " l'ennemie a " + str(nbPuntosEnnemie) + " Puntos" + " le joueur a " + str(nbPuntosJoueur) + " Puntos")
    if nbPuntosEnnemie == 3:
        return "l'ennemie gane"
    elif nbPuntosJoueur == 3:
        return "le joueur gane"

print(PFC(3))