import random

def add(x , y):
    #addition de deux nombres
    return (x + y)

def sub(x , y):
    #soustrzaction de deux nombres
    return(x - y)

def multiply(x , y):
    #multiplication de deux nombres
    return(x * y)

def divide(x , y):
    #condition de division par 0 pas très possible (sauf si t'as pris math expert)
    if y != 0:
        #division de deux nombres
        return(x / y)
    else:
        #message d'erreur
        print("dommage la division par 0 ne marche pas")
        return

def modulo(x , y):
    #condition de division par 0 pas très possible (sauf si t'as pris math expert)
    if y != 0:
        #modulo de deux nombres
        return(x % y)

def salaires(salaireh , hjo , joan):
    return((salaireh*hjo*joan)/(365*24*60*60))

def salairenet(net):
    return(net*1.25)


liste=[0,1,1,1,0,1,1,0,1]
def itere(tableau, nb):
    stringue="" #initialise la variable string
    for i in range (len(tableau)): #incrémente i jusqu'a la longueur de la liste
        if tableau[i] == nb and stringue == "": #si la valeur du tableau a l'index i est = à la valeur chercher et que le string est vide
            stringue = str(i) #prend la valeur en string de la valeur i 
        elif tableau[i] == nb: #si la valeur du tableau a l'index i est = à la valeur chercher
            stringue = stringue + ", " + str(i) #rajoute ", " et la valeur en string de i
    return stringue #returne stringue

def concate(texte1,texte2):
    return str(texte1) + ", " + str(texte2) #concatene les deux chaine de caractère

def affiche(aff):
    print(aff) #affiche la variable aff

listUtilisateur = {
    "Alexandre" : "motdepasse",
    "Michel" : "Password",
    "Toto" : "12345",
    "JhonDoe" : "azerty"
}

def login(user,password,utilisateurs):
    if utilisateurs.get(user) == password: #si le password lier a l'user est le bon
        return"ganer" #retorune "ganer"


def fibonachi (xdebut,lenmax):
    texte="0, " + str(xdebut) #initialise le texte avec le 0 et le x debut en str
    suiteNb=[0,xdebut] #initialise la suite avec le 0 et le x debut en int dans une liste
    for i in range (lenmax): #boucle de la longueur de la longuer max
        suiteNb.append(suiteNb[-1]+suiteNb[-2]) #ajoute a la fin de la liste de int la valeur qui est l'addition des deux dernière valeur
        texte += ", " + str(suiteNb[-1]+suiteNb[-2]) #ajoute ", " et la valeur calculer grâce à la liste
    return texte #retourne le texte complète

def tableau(lenx,leny,liste):
    for x in range (lenx):
        for y in range (leny):
            if x == 0 and y == 0:
                if liste[0][0] == liste[0][1] or liste[0][0] == liste[1][0]:
                    return "pedu1"
            elif x != 0 and x != lenx-1 and y == 0:
                if liste[x][0] == liste[x][1] or liste[x][0] == liste[x-1][0] or liste[x][0] == liste[x+1][0]:
                    return "pedu2"
            elif x == 0 and y != 0 and y != leny-1:
                if liste[0][y] == liste[1][y] or liste[0][y] == liste[0][y-1] or liste[0][y] == liste[0][y+1]:
                    return "pedu3"
            elif x == lenx-1 and y == leny-1:
                if liste[lenx-1][leny-1] == liste[lenx-1][leny-2] or liste[lenx-1][leny-1] == liste[lenx-2][leny-1]:
                    return "pedu4"
            elif x != 0 and x != lenx-1 and y == leny-1:
                if liste[x][leny-1] == liste[x][leny-2] or liste[x][leny-1] == liste[x-1][leny-1] or liste[x][leny-1] == liste[x+1][leny-1]:
                    return "pedu5"
            elif x == lenx-1 and y != 0 and y != leny-1:
                if liste[lenx-1][y] == liste[lenx-2][y] or liste[lenx-1][y] == liste[lenx-1][y-1] or liste[lenx-1][y] == liste[lenx-1][y+1]:
                    return "pedu6"
            elif y != 0 and y != leny-1 and x != 0 and x != lenx-1:
                if liste[x][y] == liste[x][y+1] or liste[x][y] == liste[x-1][y] or liste[x][y] == liste[x+1][y] or liste[x][y] == liste[x][y-1] or liste[x][y] == liste[x][y+1]:
                    return "pedu7"



print(tableau(4,4,[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]))