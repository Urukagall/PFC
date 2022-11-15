import random

#on admet une fonction random qui renvoie un nombre aléatoire entre un nombres x et un autre y
#on admet une fonction input qui renvoie ce que le joueur rentre

#Début

#definir la fonction convertPFC qui prend en argument le choix
    #si le choix est égale a 0
        #alors retourne "pierre"
    # ou sinon le choix est égale a 1
        #alors retourne "feuille"
    #ou sinon le choix est égale a 2
        #alors retourne "ciseaux"

#définir la fonction PFC aui prend en argument le nombre de puntos pour gagner
    #initialise la variable nbPuntosPlayer a 0
    #initialise la variable nbPuntosEnnemie a 0
    #tant que nbPuntosPlayer est inférieur a nbPuntos et nbPuntosEnnemie est inférieur a nbPuntos
        #initialise la variable ennemie avec la valeur retourner par l'éxecution de la fonction random qui prendra en argument x=0 et y=2
        #initialise la variable player avec le retour de l'éxecution de la fonction input
        #tant que player n'est pas égale a "0" "1" ou "2"
            #alors affiche "dommage réessaie" 
            #la variable player est égale au retour de l'éxecution de la fonction input
        #alors la variable joueur est convertit en integer
        #si la variable ennemie est égale a celle de joueur
            #alors affiche "égalter" et le nombre de puntos de chacun
        #ou sinon la variable ennemie est égale a la variable joueur plus 1 (l'ennemie gagne avec un ciseaux ou une feuille)
            #alors affiche "l'ennemie gane" et le nombre de puntos de chacun
        #ou sinon la variable joueur est égale a la variable ennemie plus 1 (le joueur gagne avec un ciseaux ou une feuille)
            #alors affiche "le joueur gane" et le nombre de puntos de chacun
        #ou sinon la variable ennemie est égale à 0 et la variable joueur est égale à 2 (l'ennemie gagne avec une pierre)
            #alors affiche "l'ennemie gane" et le nombre de puntos de chacun
        #ou sinon la variable joueur est égale à 0 et la variable ennemie est égale à 2 (le joueur gagne avec une pierre)
            #alors affiche "le joueur gane" et le nombre de puntos de chacun
    #si la variable nbPuntosEnnemie est égale a 3
        #alors affiche "l'ennemie gane"
    #ou sinon la variable nbPuntosPlayer est égale a 3
        #alors affiche "le joueur gane"

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
    nbPuntosPlayer=0
    nbPuntosEnnemie=0
    while nbPuntosPlayer < nbPuntos and nbPuntosEnnemie < nbPuntos :
        ennemie = random.randint(0,2)
        player = input("0- pierre\n1- feuille\n2- ciseaux\n")
        while player != "0" and  player != "1" and  player != "2" :
            print("dommage réessaie")
            player = input("0- Pierre\n1- feuille\n3- ciseaux\n")
        player = int(player)
        if ennemie == player :
            print("égalter" + " l'ennemie a " + str(nbPuntosEnnemie) + " Puntos" + " le joueur a " + str(nbPuntosPlayer) + " Puntos")
        elif ennemie == player + 1 :
            nbPuntosEnnemie += 1
            print("l'ennemie gane avec " + convertPFC(ennemie) + " l'ennemie a " + str(nbPuntosEnnemie) + " Puntos" + " le joueur a " + str(nbPuntosPlayer) + " Puntos")
        elif player == ennemie + 1 :
            nbPuntosPlayer += 1
            print("le joueur gane avec " + convertPFC(player) + " l'ennemie a " + str(nbPuntosEnnemie) + " Puntos" + " le joueur a " + str(nbPuntosPlayer) + " Puntos")
        elif ennemie == 0 and player == 2 :
            nbPuntosEnnemie += 1
            print("l'ennemie gane avec " + convertPFC(ennemie) + " l'ennemie a " + str(nbPuntosEnnemie) + " Puntos" + " le joueur a " + str(nbPuntosPlayer) + " Puntos")
        elif ennemie == 2 and player == 0 :
            nbPuntosPlayer += 1
            print("le joueur gane avec " + convertPFC(player) + " l'ennemie a " + str(nbPuntosEnnemie) + " Puntos" + " le joueur a " + str(nbPuntosPlayer) + " Puntos")
    if nbPuntosEnnemie == 3:
        print("l'ennemie gane")
    elif nbPuntosPlayer == 3:
        print("le joueur gane")

PFC(3)