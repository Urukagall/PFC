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