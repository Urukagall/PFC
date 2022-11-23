import random

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
