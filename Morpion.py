import random 
from tkinter import *

def VerifAlign(board): 
    for x in range (3):
        if board[x][0] == "X" and board[x][1] == "X" and board[x][2] == "X" : #vérifie si la colonne d'indice x est remplie de X
            return 1, 0,True
        elif board[x][0] == "O" and board[x][1] == "O" and board[x][2] == "O" : #vérifie si la colonne d'indice x est remplie de O
            return 0, 1,True
        if board[0][x] == "X" and board[1][x] == "X" and board[2][x] == "X" : #vérifie si la ligne d'indice x est remplie de X
            return 1, 0,True
        elif board[0][x] == "O" and board[1][x] == "O" and board[2][x] == "O" : #vérifie si la ligne d'indice x est remplie de O
            return 0, 1,True
    if board[0][0] == "X" and board[1][1] == "X" and board[2][2] == "X" : #vérifie si la diagonale de haut droite a bas gauche remplie de X
        return 1, 0,True
    elif board[0][0] == "O" and board[1][1] == "O" and board[2][2] == "O" : #vérifie si la diagonale de haut droite a bas gauche remplie de O
        return 0, 1,True
    if board[0][2] == "X" and board[1][1] == "X" and board[2][0] == "X" : #vérifie si la diagonale de haut gauche a bas droite remplie de X
        return 1, 0,True
    elif board[0][2] == "O" and board[1][1] == "O" and board[2][0] == "O" : #vérifie si la diagonale de haut gauche a bas droite remplie de O
        return 0, 1,True
    if board[0].count(" ") == 0 and board[1].count(" ") == 0 and board[2].count(" ") == 0  : #vérifie si il y a une égaliter
        return 0, 0,True
    return 0,0,False

def Display(board,boardHint):
    print("",board[0],"          ",boardHint[0],"\n",board[1],"          ",boardHint[1],"\n",board[2],"          ",boardHint[2]) #affiche le morpion

def Assign(choice,board,player):
    if choice <= 3 and choice > 0 and board[2][int(choice-1)] == " ": #complète la première ligne par le symbole correspondant
        board[2][int(choice-1)] = player
    elif choice <= 6 and choice > 3 and board[1][int(choice-4)] == " ": #complète la deuxième ligne par le symbole correspondant
        board[1][int(choice-4)] = player
    elif choice <= 9 and choice > 6 and board[0][int(choice-7)] == " ": #complète la troisième ligne par le symbole correspondant
        board[0][int(choice-7)] = player
    else:
        return False
    return True

def IA(board):
    IACanPlay = True
    nbOColumn = [0,0,0]
    nbXColumn = [0,0,0]
    nbEmptyColumn = [0,0,0]
    EmptyIndexColumn = [0,0,0]
    EmptyIndexDiagonal0 = 0
    EmptyIndexDiagonal1_1 = 0
    EmptyIndexDiagonal1_2 = 0
    nbODiagonal0 = 0
    nbODiagonal1 = 0
    nbXDiagonal0 = 0
    nbXDiagonal1 = 0
    nbEmptyDiagonal0 = 0
    nbEmptyDiagonal1 = 0
    choiceEnnemie = ["",""]
    for i in range (3):
        if board[i].count("X") == 2 and board[i].count(" ") == 1 and IACanPlay == True: #Vérifie si l'IA peut gagner en ligne horizontale
            board[i][board[i].index(" ")] = "X"
            IACanPlay = False
    for i in range (3):
        if board[i].count("O") == 2 and board[i].count(" ") == 1 and IACanPlay == True: #vérifie si l'IA peut bloquer le joueur en ligne horizontale
            board[i][board[i].index(" ")] = "X"
            IACanPlay = False

    for i in range (3):
        for j in range (3):
            if board[i][j] == "O":
                nbOColumn[j] += 1
            if board[i][j] == "X":
                nbXColumn[j] += 1
            if board[i][j] == " ":
                nbEmptyColumn[j] += 1
                EmptyIndexColumn[j] = i
    for i in range (3):
        if nbXColumn[i] == 2 and nbEmptyColumn[i] == 1 and IACanPlay == True: #Vérifie si l'IA peut gagner en ligne verticale
            board[EmptyIndexColumn[i]][i] = "X" 
            IACanPlay = False
    for i in range (3):       
        if nbOColumn[i] == 2 and nbEmptyColumn[i] == 1 and IACanPlay == True: #vérifie si l'IA peut bloquer le joueur en ligne verticale
            board[EmptyIndexColumn[i]][i] = "X" 
            IACanPlay = False
    diago = 2

    for i in range (3):
        if board[i][i] == "O":
            nbODiagonal0 += 1
        if board[i][i] == "X":
            nbXDiagonal0 += 1
        if board[i][i] == " ":
            nbEmptyDiagonal0 += 1
            EmptyIndexDiagonal0 = i
        if board[i][diago] == "O":
            nbODiagonal1 += 1
        if board[i][diago] == "X":
            nbXDiagonal1 += 1
        if board[i][diago] == " ":
            nbEmptyDiagonal1 += 1
            EmptyIndexDiagonal1_1 = i
            EmptyIndexDiagonal1_2 = diago
        diago -= 1
    if nbXDiagonal0 == 2 and nbEmptyDiagonal0 == 1 and IACanPlay == True: #Vérifie si l'IA peut gagner en ligne diagonale
        board[EmptyIndexDiagonal0][EmptyIndexDiagonal0] = "X"
        IACanPlay = False
    elif nbXDiagonal1 == 2 and nbEmptyDiagonal1 == 1 and IACanPlay == True:
        board[EmptyIndexDiagonal1_1][EmptyIndexDiagonal1_2] = "X"
        IACanPlay = False
    if nbODiagonal0 == 2 and nbEmptyDiagonal0 == 1 and IACanPlay == True: #vérifie si l'IA peut bloquer le joueur en ligne verticale
        board[EmptyIndexDiagonal0][EmptyIndexDiagonal0] = "X"
        IACanPlay = False
    elif nbODiagonal1 == 2 and nbEmptyDiagonal1 == 1 and IACanPlay == True:
        board[EmptyIndexDiagonal1_1][EmptyIndexDiagonal1_2] = "X"
        IACanPlay = False
    #Quelques vérification pour que le joueur ne puisse pas brain l'IA
    if (board[1][0] == "O" or board[0][1] == "O") and (board[1][0] == " " or board[0][1] == " ") and board[0][0] == " " and (board[2][2] == " " or board[2][2] == "O") and IACanPlay == True:
        board[0][0] = "X"
        IACanPlay = False
    if (board[1][2] == "O" or board[2][1] == "O") and (board[1][2] == " " or board[2][1] == " ") and board[2][2] == " " and (board[0][0] == " " or board[0][0] == "O") and IACanPlay == True:
        board[2][2] = "X"
        IACanPlay = False
    if board[1][1] == " " and IACanPlay == True:
        board[1][1] = "X"
        IACanPlay = False
    elif board[1][1] == "O" and board[0][0] == " " and IACanPlay == True:
        board[0][0] = "X"
        IACanPlay = False
    elif board[1][1] == "O" and board[2][2] == "O" and board[0][0] == "X" and board[0][2] == " " and IACanPlay == True:
        board[0][2] = "X"
        IACanPlay = False
    if board[0][0] == "O" and board[2][2] == "O" and board[1][1] == "X" and board[1][0] == " " and IACanPlay == True:
        board[1][0] = "X"
        IACanPlay = False
    elif board[0][2] == "O" and board[2][0] == "O" and board[1][1] == "X" and board[1][0] == " " and IACanPlay == True:
        board[1][0] = "X"
        IACanPlay = False
    if IACanPlay == True:
        choiceEnnemie = random.randint(1,9) #nombre aléatoire pour la coordonée 
        while Assign(choiceEnnemie,board,"X") == False: #while tant que le choix de l'ennemie n'est pas une case vide
            choiceEnnemie = random.randint(1,9)
        IACanPlay == False
        

        

def Morpion():
    nbPuntosEnnemie = 0
    nbPuntosPlayer = 0
    choicePlayer = 0
    gameFinish = False
    board=[[" "," "," "],[" "," "," "],[" "," "," "]]
    boardHint=[["7","8","9"],["4","5","6"],["1","2","3"]]
    while nbPuntosEnnemie < 3 and nbPuntosPlayer < 3 : #while tant que l'un des deux camp n'as pas assez de points (3)
        while not(gameFinish): #while tant que la partie en cours n'est pas fini
            Display(board,boardHint) #affiche le morpion
            choicePlayer = int(input("Met ta coordonées comme présent dans le tableau de droite, (la case devra être vide)\n")) #demande la coordonnées au joueur
            while Assign(choicePlayer,board,"O") == False: #while tant que le choix du joueur n'est pas une case vide
                choicePlayer = int(input("Met ta coordonées comme présent dans le tableau de droite, (la case devra être vide)\n"))
            liste = VerifAlign(board)
            if liste[2] == False : #si la partie n'est pas finie
                IA(board)
            liste = VerifAlign(board)
            nbPuntosEnnemie += liste[0]
            nbPuntosPlayer += liste[1]
            gameFinish = liste[2]
        Display(board,boardHint) #affiche le morpion
        if liste[0] == 1 : #si l'ennemie a gagner cette manche
            print("L'ennemie a gagner avec ", nbPuntosEnnemie , " puntos contre ", nbPuntosPlayer , " puntos pour le joueur")
        elif liste[1] == 1 : #si le joueur a gagner cette manche
            print("Le joueur a gagner avec ", nbPuntosPlayer , " puntos contre ", nbPuntosEnnemie , " puntos pour l'ennemie")
        else : #sinon une égaliter
            print("égalter")
        board=[[" "," "," "],[" "," "," "],[" "," "," "]]
        gameFinish = False
    if nbPuntosEnnemie == 3 : #si l'ennemie a gagner la partie
        print("L'ennemie gane")
    elif nbPuntosPlayer == 3 : #si le joueur a gagner la partie
        print("Le joueur gane")

Morpion()

#Début

#importation de la bibliothèque random
#importation de la bibliothèque Tkinter

#Definition de la fonction VerifAlign qui prend en paramètre la vaiable board
    #créer une boucle de longueur 3 et qui incremente x de 1 a chaque tour
        #si la liste board  a l'indice x et 0 est égale a "X" et que board a l'indice x et 1 est égale a "X" et que board a l'indice x et 2 est égale a "X"
            #alors retourne 1, 0, True
        #ou sinon la liste board  a l'indice x et 0 est égale a "O" et que board a l'indice x et 1 est égale a "O" et que board a l'indice x et 2 est égale a "O"
            #alors retourne 0, 1, True
        #ou sinon la liste board  a l'indice 0 et x est égale a "X" et que board a l'indice 1 et x est égale a "X" et que board a l'indice 2 et x est égale a "X"
            #alors retourne 1, 0, True
        #ou sinon la liste board  a l'indice 0 et x est égale a "O" et que board a l'indice 1 et x est égale a "O" et que board a l'indice 2 et x est égale a "O"
            #alors retourne 0, 1, True
    #si la liste board  a l'indice 0 et 0 est égale a "X" et que board a l'indice 1 et 1 est égale a "X" et que board a l'indice 2 et 2 est égale a "X"
        #alors retourne 1, 0, True
    #ou sinon la liste board  a l'indice 0 et 0 est égale a "O" et que board a l'indice 1 et 1 est égale a "O" et que board a l'indice 2 et 2 est égale a "O"
        #alors retourne 0, 1, True   
    #si la liste board  a l'indice 0 et 2 est égale a "X" et que board a l'indice 1 et 1 est égale a "X" et que board a l'indice 2 et 0 est égale a "X"
        #alors retourne 1, 0, True
    #ou sinon la liste board  a l'indice 0 et 2 est égale a "O" et que board a l'indice 1 et 1 est égale a "O" et que board a l'indice 2 et 0 est égale a "O"
        #alors retourne 0, 1, True  
    #si le nombre de " " dans la liste board a l'indice 0 est égale a 0 et que le nombre de " " dans board a l'indice 1 est égale a 0 et que le nombre de " " dans board a l'indice 2 est égale a 0
        #alors retourne 0, 0, True
    #retorune 0, 0, False


#Définition de la fonction Display prenant en paramètre board et boardHint
    #Affichage de board et de boardHint


#Définition de la fonction Assign prenant en paramètre choice,board et player
    #si choice est inférieur ou égal à 3 et que choice est strictement supérieur 0 et que board[indice2][choice-1] est égal à vide
        #Alors, board[indice2][choice-1] est égal à player
    #sinon si choice est inférieur ou égal à 6 et que choice est strictement supérieur à 3 et que board[indice1][choice-4] est égal à vide
        #Alors, board[indice1][choice-4] est égal à player
    #sinon si choice est inférieur ou égal à 9 et que choice est strictement supérieur à 6 et que board[indice0][choice-7] est égal à vide
        #Alors, board[indice0][choice-7] est égal à player
    #sinon
        #Retourne False
    #Retourne True

#Définition de la fonction IA prenant en paramètre board
    #Initialisation de la variable IACanPlay à True
    #Initialisation de la liste nbOColumn à [0,0,0]
    #Initialisation de la liste nbXColumn à [0,0,0]
    #Initialisation de la liste nbEmptyColumn à [0,0,0]
    #Initialisation de la liste EmptyIndexColumn à [0,0,0]
    #Initialisation de la variable EmptyIndfexDiagonal0 à 0
    #Initialisation de la variable EmptyIndfexDiagonal1_1 à 0
    #Initialisation de la variable EmptyIndfexDiagonal1_2 à 0
    #Initialisation de la variable nbODiagonal0 à 0
    #Initialisation de la variable nbODiagonal1 à 0
    #Initialisation de la variable nbXDiagonal0 à 0
    #Initialisation de la variable nbXDiagonal0 à 0
    #Initialisation de la variable nbEmptyDiagonal0 à 0
    #Initialisation de la variable nbEmptyDiagonal1 à 0
    #Initialisation de la liste choiceEnnemie à ["",""]
    #Pour i allant de 0 à 2
        #Si board à indice i compte le nombre de "X" est égal 2 et que board indice  i compte le nombre d'endroit vide est égal à 1 et que IACanPlay est strictement égal à True
            #Alors, board[indice i][board[indice i] à l'index vide] est égal "X"
            #Passage de la variable IACanPlay à False
    #Pour i allant de 0 à 2
        #Si board à indice i compte le nombre de "O" est égal 2 et que board indice  i compte le nombre d'endroit vide est égal à 1 et que IACanPlay est strictement égal à True
            #Alors, board[indice i][board[indice i] à l'index vide] est égal "X"
            #Passage de la variable IACanPlay à False
    
    #Pour i allant de 0 à 2
        #Pour j allant de 0 à 2
            #Si board[indice i][indice j] est strictement égal à "O"
                #Alors, Ajoute 1 à nbOColumn[indice j]
            #Si board[indice i][indice j] est strictement égal à "X"
                #Alors, Ajoute 1 à nbXColumn[indice j]
            #Si board[indice i][indice j] est strictement égal à vide
                #Alors, Ajoute 1 à nbEmptyColumn[indice j]
                #EmptyIndexColumn[indice j] est égal à i
    #Pour i allant de 0 à 2
        #Si nbXColumn[indice i] est strictement égal à 2 et que nbEmptyColumn[indice i] est strictement égal à 1 et que IACanPlay est strictement égal à True
            #Alors, board[indice EmptyIndexColumn[indice i]][indice i] est égal à "X"
            #Passage de la variable IACanPlay à False
    #Pour i allant de 0 à 2
        #Si nbOColumn[indice i] est strictement égal à 2 et que nbEmptyColumn[indice i] est strictement égal à 1 et que IACanPlay est strictement égal à True
            #Alors, board[indice EmptyIndexColumn[indice i]][indice i] est égal à "X"
            #Passage de la variable IACanPlay à False
    #Initialisation de la variable diago à 2

    #Pour i allant de 0 à 2
        #Si board[indice i][indice i] est strictement égal à "O"
            #Alors, Ajoute 1 à nbODiagonal0
        #Si board[indice i][indice i] est strictement égal à "X"
            #Alors, Ajoute 1 à nbXDiagonal0
        #Si board[indice i][indice i] est strictement égal à vide
            #Alors, Ajoute 1 à nbEmptyDiagonal0
            #EmptyIndexDiagonal0 est égal à i
        #Si board[indice i][indice diago] est strictement égal à "O"
            #Alors, Ajoute 1 à nbODiagonal1
        #Si board[indice i][indice diago] est strictement égal à "X"
            #Alors, Ajoute 1 à nbXDiagonal1
        #Si board[indice i][indice diago] est strictement égal à vide
            #Alors, Ajoute 1 à nbEmptyDiagonal1
            #EmptyIndexDiagonal1_1 est égal à i
            #EmptyIndexDiagonal1_2 est égal à diago
        #Soustrait 1 à diago
    #Si nbXDiagonal0 est strictement égal à 2 et que nbEmptyDiagonal0 est strictement égal à 1 et que IACanPlay est strictement égal à True
        #Alors, board[indice EmptyIndexDiagonal0][indice EmptyIndexDiagonal0] est égal à "X"
        #Passage de la variable IACanPlay à False
    #Sinon si nbXDiagonal1 est strictement égal à 2 et que nbEmptyDiagonal1 est strictement égal à 1 et que IACanPlay est strictement égal à True
        #Alors, board[indice EmptyIndexDiagonal1_1][indice EmptyIndexDiagonal1_2] est égal à "X"
        #Passage de la variable IACanPlay à False
    #Si nbODiagonal0 est strictement égal à 2 et que nbEmptyDiagonal0 est strictement égal à 1 et que IACanPlay est strictement égal à True
        #Alors, board[indice EmptyIndexDiagonal0][indice EmptyIndexDiagonal0] est égal à "X"
        #Passage de la variable IACanPlay à False
    #Sinon si nbODiagonal1 est strictement égal à 2 et que nbEmptyDiagonal1 est strictement égal à 1 et que IACanPlay est strictement égal à True
        #Alors, board[indice EmptyIndexDiagonal1_1][indice EmptyIndexDiagonal1_2] est égal à "X"
        #Passage de la variable IACanPlay à False
    #Si (board[indice 1][indice 0] est strictement égal à "O" ou que board[indice 0][indice 1] est strictement égal à "O") et que (board[indice 1][indice 0] est strictement égal à vide ou que board[indice 0][indice 1] est égal vide) and board[indice 0][indice 0] est strictement égal à vide et que board[indice 2][indice 2] est strictement égal à vide et que IACanPlay est strictement égal True
        #Alors, board[indice 0][indice 0] est égal à "X"
        #Passage de la variable IACanPlay à False
    #Si (board[indice 1][indice 2] est strictement égal à "O" ou que board[indice 2][indice 1] est strictement égal à "O") et que (board[indice 1][indice 2] est strictement égal à vide ou que board[indice 2][indice 1] est égal vide) and board[indice 0][indice 0] est strictement égal à vide et que board[indice 2][indice 2] est strictement égal à vide et que IACanPlay est strictement égal True
        #Alors, board[indice 2][indice 2] est égal à "X"
        #Passage de la variable IACanPlay à False
    #Si board[indice 1][indice 1] est strictement égal à vide et que IACanPlay est strictement égal True
        #board[indice 1][indice 1] est égal à "X"
        #Passage de la variable IACanPlay à False
    #Sinon si board[indice 1][indice 1] est strictement égal à "O" et que board[indice 0][indice 0] est strictement égal à vide et que IACanPlay est strictement égal à True
        #Alors, board[indice 0][indice 0] est égal à "X"
        #Passage de la variable IACanPlay à False
    #Sinon si board[indice 1][indice 1] est strictement égal à "O" et que board[indice 2][indice 2] est strictement égal à vide et que board[indice 0][indice 0] est strictement égal à vide et que IACanPlay est strictement égal à True
        #Alors, board[indice 0][indice 2] est égal à "X"
        #Passage de la variable IACanPlay à False
    #Si board[indice 0][indice 0] est strictement égal à "O" et que board[indice 2][indice 2] est strictement égal à "O" et que board[indice 1][indice 1] est strictement égal à "X" et que board[indice 1][indice 0] est strictement égal à vide et que IACanPlay est strictement égal à True
        #Alors, board[indice 1][indice 0] est égal à "X"
        #Passage de la variable IACanPlay à False
    #Sinon si board[indice 0][indice 2] est strictement égal à "O" et que board[indice 2][indice 0] est strictement égal à "O" et que board[indice 1][indice 1] est strictement égal à "X" et que board[indice 1][indice 0] est strictement égal à vide et que IACanPlay est strictement égal à True
        #Alors, board[indice 1][indice 0] est égal à "X"
        #Passage de la variable IACanPlay à False
    #Si IACanPlay est strictement égal à True
        #Alors, choiceEnnemie est égal à un nombre aléatoire entre 1 et 9
        #Tant que Assign(choiceEnnemie,board,"X") est strictement égal à False
            #choiceEnnemie est égal à un nombre aléatoire entre 1 et 9
        #Passage de la variable IACanPlay à False

#Définition de la fonction Morpion
    #Initialisation de nbPuntosEnnemie à 0
    #Initialisation de nbPuntosPlayer à 0
    #Initialisation de la liste choicePlayer à 0
    #Initialisation de gameFinish à False
    #Initialisation de la liste (board) pour le morpion à [[" "," "," "],[" "," "," "],[" "," "," "]]
    #Initialisation de la liste (référence) (boardHint) [["7","8","9"],["4","5","6"],["1","2","3"]]
    #Tant que nbPuntosEnnemie est inférieur à 3 et que nbPuntosPlayer est inférieur à 3
        #Alors tant que gameFinish est égal à False
            #Alors afficher Display(board,boardHint)
            #Input la variable choicePlayer (int)
            #Tant que Assign(choicePlayer,board,"O") est strictement égal à False
                #Input la variable choicePlayer (int)
            #Initialisation de la variable "liste" qui vérifie si des mêmes symboles sont alignés avec la fonction VerifAlign
            #Si l'indice 2 de la liste est égal à False
                #IA(board)
            #Initialisation de la variable "liste" qui vérifie si des mêmes symboles sont alignés avec la fonction VerifAlign
            #Ajoute liste[indice 0] à nbPuntosEnnemie
            #Ajoute liste[indice 1] à nbPuntosPlayer
            #gameFinish est égal à liste[indice 2]
            #Alors afficher Display(board,boardHint)
        #si la liste liste a l'indice 0 est égale a 1
            #alors affiche que l'ennemie gagne avec le nombre de point de chaque camp
        #ou sinon la liste liste a l'indice 1 est égale a 1
            #alors affiche que le joueur gagne avec le nombre de point de chaque camp
        #sinon 
            #affiche "égaliter"
        #Passage de la balise board à [[" "," "," "],[" "," "," "],[" "," "," "]]
        #Passage de la variable gameFinish à False
    #si nbPuntosEnnemie est égale à 3
        #alors affiche "L'ennemie gagne"
    #sinon si nbPuntosPlayer est égale a 3
        #alors affiche "Le joueur gagne"


#Appelle la fonction Morpion

#fin