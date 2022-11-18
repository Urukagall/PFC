import random 

def VerifAlign(tableau): 
    for x in range (3):
        if tableau[x][0] == "X" and tableau[x][1] == "X" and tableau[x][2] == "X" : #vérifie si la colonne d'indice x est remplie de X
            return 1, 0,True
        elif tableau[x][0] == "O" and tableau[x][1] == "O" and tableau[x][2] == "O" : #vérifie si la colonne d'indice x est remplie de O
            return 0, 1,True
        if tableau[0][x] == "X" and tableau[1][x] == "X" and tableau[2][x] == "X" : #vérifie si la ligne d'indice x est remplie de X
            return 1, 0,True
        elif tableau[0][x] == "O" and tableau[1][x] == "O" and tableau[2][x] == "O" : #vérifie si la ligne d'indice x est remplie de O
            return 0, 1,True
    if tableau[0][0] == "X" and tableau[1][1] == "X" and tableau[2][2] == "X" : #vérifie si la diagonale de haut droite a bas gauche remplie de X
        return 1, 0,True
    elif tableau[0][0] == "O" and tableau[1][1] == "O" and tableau[2][2] == "O" : #vérifie si la diagonale de haut droite a bas gauche remplie de O
        return 0, 1,True
    if tableau[0][2] == "X" and tableau[1][1] == "X" and tableau[2][0] == "X" : #vérifie si la diagonale de haut gauche a bas droite remplie de X
        return 1, 0,True
    elif tableau[0][2] == "O" and tableau[1][1] == "O" and tableau[2][0] == "O" : #vérifie si la diagonale de haut gauche a bas droite remplie de O
        return 0, 1,True
    if tableau[0].count(" ") == 0 and tableau[1].count(" ") == 0 and tableau[2].count(" ") == 0  : #vérifie si il y a une égaliter
        return 0, 0,True
    return 0,0,False

def Morpion():
    nbPuntosEnnemie = 0
    nbPuntosPlayer = 0
    choicePlayer = ["",""]
    choiceEnnemie = ["",""]
    gameFinish = False
    tableau=[[" "," "," "],[" "," "," "],[" "," "," "]]
    while nbPuntosEnnemie < 3 and nbPuntosPlayer < 3 : #while tant que l'un des deux camp n'as pas assez de points (3)
        while not(gameFinish): #while tant que la partie en cours n'est pas fini
            print("",tableau[0],"\n",tableau[1],"\n",tableau[2]) #affiche le morpion
            choicePlayer[0] = input("Met ta coordonées y\n") #demande la coordonnées y au joueur
            choicePlayer[1] = input("Met ta coordonées x\n") #demande la coordonnées x au joueur
            while tableau[int(choicePlayer[0])][int(choicePlayer[1])] != " ": #while tant que le choix du joueur n'est pas une case vide
                choicePlayer[0] = input("Met ta coordonées y\n")
                choicePlayer[1] = input("Met ta coordonées x\n")
            tableau[int(choicePlayer[0])][int(choicePlayer[1])] = "O" #remplie le tableau avec le choix du joueur
            liste = VerifAlign(tableau)
            if liste[2] == False : #si la partie n'est pas finie
                choiceEnnemie[0] = random.randint(0,2) #nombre aléatoire pour la coordonée y
                choiceEnnemie[1] = random.randint(0,2) #nombre aléatoire pour la coordonée x
                while tableau[int(choiceEnnemie[0])][int(choiceEnnemie[1])] != " ": #while tant que le choix de l'ennemie n'est pas une case vide
                    choiceEnnemie[0] = random.randint(0,2)
                    choiceEnnemie[1] = random.randint(0,2)
                tableau[int(choiceEnnemie[0])][int(choiceEnnemie[1])] = "X" #remplie le tableau avec le choix du l'ennemie
            liste = VerifAlign(tableau)
            nbPuntosEnnemie += liste[0]
            nbPuntosPlayer += liste[1]
            gameFinish = liste[2]
        print("",tableau[0],"\n",tableau[1],"\n",tableau[2]) #affiche le morpion
        if liste[0] == 1 : #si l'ennemie a gagner cette manche
            print("L'ennemie a gagner avec ", nbPuntosEnnemie , " puntos contre ", nbPuntosPlayer , " puntos pour le joueur")
        elif liste[1] == 1 : #si le joueur a gagner cette manche
            print("Le joueur a gagner avec ", nbPuntosPlayer , " puntos contre ", nbPuntosEnnemie , " puntos pour l'ennemie")
        else : #sinon une égaliter
            print("égalter")
        tableau=[[" "," "," "],[" "," "," "],[" "," "," "]]
        gameFinish = False
    if nbPuntosEnnemie == 3 : #si l'ennemie a gagner la partie
        print("L'ennemie gane")
    elif nbPuntosPlayer == 3 : #si le joueur a gagner la partie
        print("Le joueur gane")




Morpion()

#Début

#importation de la bibliothèque random

#definition de la fonction VerifAlign qui prend en paramètre la vaiable tableau
    #créer une boucle de longueur 3 et qui incremente x de 1 a chaque tour
        #si la liste tableau  a l'indice x et 0 est égale a "X" et que tableau a l'indice x et 1 est égale a "X" et que tableau a l'indice x et 2 est égale a "X"
            #alors retourne 1, 0, True
        #ou sinon la liste tableau  a l'indice x et 0 est égale a "O" et que tableau a l'indice x et 1 est égale a "O" et que tableau a l'indice x et 2 est égale a "O"
            #alors retourne 0, 1, True
        #ou sinon la liste tableau  a l'indice 0 et x est égale a "X" et que tableau a l'indice 1 et x est égale a "X" et que tableau a l'indice 2 et x est égale a "X"
            #alors retourne 1, 0, True
        #ou sinon la liste tableau  a l'indice 0 et x est égale a "O" et que tableau a l'indice 1 et x est égale a "O" et que tableau a l'indice 2 et x est égale a "O"
            #alors retourne 0, 1, True
    #si la liste tableau  a l'indice 0 et 0 est égale a "X" et que tableau a l'indice 1 et 1 est égale a "X" et que tableau a l'indice 2 et 2 est égale a "X"
        #alors retourne 1, 0, True
    #ou sinon la liste tableau  a l'indice 0 et 0 est égale a "O" et que tableau a l'indice 1 et 1 est égale a "O" et que tableau a l'indice 2 et 2 est égale a "O"
        #alors retourne 0, 1, True   
    #si la liste tableau  a l'indice 0 et 2 est égale a "X" et que tableau a l'indice 1 et 1 est égale a "X" et que tableau a l'indice 2 et 0 est égale a "X"
        #alors retourne 1, 0, True
    #ou sinon la liste tableau  a l'indice 0 et 2 est égale a "O" et que tableau a l'indice 1 et 1 est égale a "O" et que tableau a l'indice 2 et 0 est égale a "O"
        #alors retourne 0, 1, True  
    #si le nombre de " " dans la liste tableau a l'indice 0 est égale a 0 et que le nombre de " " dans tableau a l'indice 1 est égale a 0 et que le nombre de " " dans tableau a l'indice 2 est égale a 0
        #alors retourne 0, 0, True
    #retorune 0, 0, False


#Initialisation de la fonction Morpion
    #Initialisation de nbPuntosEnnemie à 0
    #Initialisation de nbPuntosPlayer à 0
    #Initialisation de la liste choicePlayer à ["",""]
    #Initialisation de la liste choiceEnnemie à ["",""]
    #Initialisation de gameFinish à False
    #Initialisation de la liste (tableau) pour le morpion à [[" "," "," "],[" "," "," "],[" "," "," "]]
    #Tant que nbPuntosEnnemie est inférieur à 3 et que nbPuntosPlayer est inférieur à 3
        #Alors tant que gameFinish est égal à False
            #Alors afficher le tableau ligne par ligne
            #Input la coordonnée du joueur "y" dans la liste choicePlayer à l'indice 0
            #Input la coordonnée du joueur "x" dans la liste choicePlayer à l'indice 1
            #Tant que la case choisie par le joueur n'est pas égal à " "
                #Alors, Input la coordonnée du joueur "y" dans la liste choicePlayer à l'indice 0
                #Alors, Input la coordonnée du joueur "x" dans la liste choicePlayer à l'indice 1
            #Inserer dans le tableau le caractère "O" aux indices correspondants insérer par le joueur
            #Création de la variable "liste" qui vérifie si des mêmes symboles sont alignés avec la fonction VerifAlign
            #Si la l'indice 2 de la liste est égal à False
                #Alors Input la coordonnée "y" du bot via une fonction random entre 0 et 2
                #Alors Input la coordonnée "x" du bot via une fonction random entre 0 et 2
                #Tant que la case choisie par le bot n'est pas égal à " "
                    #Alors Input la coordonnée "y" du bot via une fonction random entre 0 et 2
                    #Alors Input la coordonnée "x" du bot via une fonction random entre 0 et 2
                 #Inserer dans le tableau le caractère "X" aux indices correspondants insérer par le bot
            #la liste liste est égale au retour de la fonction VerifAlign avec en paramètre la liste tableau
            #la variable nbPuntosEnnemie est égale a elle même plus la liste liste a l'indice 0
            #la variable nbPuntosPlayer est égale a elle même plus la liste liste a l'indice 1
            #le booléen gameFinish est égale a la liste liste a l'indice 2
        #affiche la liste tableau ligne par ligne
        #si la liste liste a l'indice 0 est égale a 1
            #alors affiche que l'ennemie gagne avec le nombre de point de chaque camp
        #ou sinon la liste liste a l'indice 1 est égale a 1
            #alors affiche que le joueur gagne avec le nombre de point de chaque camp
        #sinon 
            #affiche "égaliter"
        #la liste tableau est égale a  [[" "," "," "],[" "," "," "],[" "," "," "]]
        #le booléen gameFinish est égale a False
    #si nbPuntosEnnemie est égale a 3
        #alors affiche "L'ennemie gagne"
    #ou sinon nbPuntosPlayer est égale a 3
        #alors affiche "Le joueur gagne"


#Appelle la fonction Morpion

#fin

