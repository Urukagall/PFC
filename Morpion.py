import random

def VerifAlign(tableau):
    for x in range (3):
        if tableau[x][0] == "X" and tableau[x][1] == "X" and tableau[x][2] == "X" :
            return 1, 0,True
        elif tableau[x][0] == "O" and tableau[x][1] == "O" and tableau[x][2] == "O" :
            return 0, 1,True
        if tableau[0][x] == "X" and tableau[1][x] == "X" and tableau[2][x] == "X" :
            return 1, 0,True
        elif tableau[0][x] == "O" and tableau[1][x] == "O" and tableau[2][x] == "O" :
            return 0, 1,True
    if tableau[0][0] == "X" and tableau[1][1] == "X" and tableau[2][2] == "X" :
        return 1, 0,True
    elif tableau[0][0] == "O" and tableau[1][1] == "O" and tableau[2][2] == "O" :
        return 0, 1,True
    if tableau[0][2] == "X" and tableau[1][1] == "X" and tableau[2][0] == "X" :
        return 1, 0,True
    elif tableau[0][2] == "O" and tableau[1][1] == "O" and tableau[2][0] == "O" :
        return 0, 1,True
    if tableau[0].count(" ") == 0 and tableau[1].count(" ") == 0 and tableau[2].count(" ") == 0  :
        return 0, 0,True
    return 0,0,False

def Morpion():
    nbPuntosEnnemie = 0
    nbPuntosPlayer = 0
    choicePlayer = ["",""]
    choiceEnnemie = ["",""]
    gameFinish = False
    tableau=[[" "," "," "],[" "," "," "],[" "," "," "]]
    while nbPuntosEnnemie < 3 and nbPuntosPlayer < 3 :
        while not(gameFinish):
            print("",tableau[0],"\n",tableau[1],"\n",tableau[2])
            choicePlayer[0] = input("Met ta coordonées y\n")
            choicePlayer[1] = input("Met ta coordonées x\n")
            while tableau[int(choicePlayer[0])][int(choicePlayer[1])] != " ":
                choicePlayer[0] = input("Met ta coordonées y\n")
                choicePlayer[1] = input("Met ta coordonées x\n")
            tableau[int(choicePlayer[0])][int(choicePlayer[1])] = "O"
            liste = VerifAlign(tableau)
            if liste[2] == False :
                choiceEnnemie[0] = random.randint(0,2)
                choiceEnnemie[1] = random.randint(0,2)
                while tableau[int(choiceEnnemie[0])][int(choiceEnnemie[1])] != " ":
                    choiceEnnemie[0] = random.randint(0,2)
                    choiceEnnemie[1] = random.randint(0,2)
                tableau[int(choiceEnnemie[0])][int(choiceEnnemie[1])] = "X"
            liste = VerifAlign(tableau)
            nbPuntosEnnemie += liste[0]
            nbPuntosPlayer += liste[1]
            gameFinish = liste[2]
        print("",tableau[0],"\n",tableau[1],"\n",tableau[2])
        if liste[0] == 1 :
            print("L'ennemie a gagner avec ", nbPuntosEnnemie , " puntos contre ", nbPuntosPlayer , " puntos pour le joueur")
        elif liste[1] == 1 :
            print("Le joueur a gagner avec ", nbPuntosPlayer , " puntos contre ", nbPuntosEnnemie , " puntos pour l'ennemie")
        else :
            print("égalter")
        tableau=[[" "," "," "],[" "," "," "],[" "," "," "]]
        gameFinish = False
    if nbPuntosEnnemie == 3 :
        print("L'ennemie gane")
    elif nbPuntosPlayer == 3 :
        print("Le joueur gane")




Morpion()

