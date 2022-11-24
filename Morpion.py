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
