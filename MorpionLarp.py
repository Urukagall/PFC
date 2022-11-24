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