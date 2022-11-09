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
def itere(tableau, nb): #définir une fonction qui prend en caractère une liste tableau et une variable nb
    stringue="" #initialise la variable stringue
    for i in range (len(tableau)): #incrémente i jusqu'a la longueur de la liste
        if tableau[i] == nb and stringue == "": #si la valeur du tableau a l'index i est = à la variable nb et que la variable stringue est vide
            stringue = str(i) #alors prend la valeur en string de la variable i 
        elif tableau[i] == nb: #si la valeur du tableau a l'index i est = à la valeur chercher
            stringue = stringue + ", " + str(i) #alors rajoute ", " et la valeur en string de la variable i
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
    for i in range (lenmax): #incrémente i 
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



#definir une fonction truc qui prend une liste tableau et une variables x quelconques
def truc(tableau,x):
    #initialise i à 0
    i=0
    #definir resultat en tant que string vide
    resultat=""
    #alors on determine firstTurn a True
    firstTrun = True
    #tant que i est inférieur a la longueur de tableau
    while i < len(tableau):
        #alors si l'element d'index i de tableau est égale à x
        if tableau[i] == x:
            #si je suis au premier tour (si firstTurn est True)
            if firstTrun:
                #alors j'assigne str(i) a resutat
                resultat = str(i)
                #on passe firstTurn a False
                firstTrun = False
            #alors on assigne a resultat le retour de concater(resultat, str(i))
            resultat = concate(resultat, str(i))
        #on incrément i de 1
        i = i + 1



#on admet une fonction random qui renvoie un nombre aléatoire entre un nombres x et un autre y
#on admet une fonction input qui renvoie ce que le joueur rentre

#définir la fonction PFC
    #initialise playerWin en booléen et sur False
    #initialise iaWin en booléen et sur False
    #initialise la variable ia avec la valeur retourner par l'éxecution de la fonction random qui prendra en argument x=0 et y=2
    #initialise la variable joueur avec le retour de l'éxecution de la fonction input
    #si la variable joueur est égale à 0,1 ou 2 qui correspond dans l'ordre a pierre, feuille et ciseaux
        #alors la variable joueur est convertit en integer
        #si la variable ennemie est égale a la variable
            #alors retourne "egalter"
        #ou sinon la variable ennemie est égale a la variable joueur plus 1 (l'ennemie gagne avec un pierre ou une feuille)
            #alors retourne "l'ennemie gane"
        #ou sinon la variable joueur est égale a la variable ennemie plus 1 (le joueur gagne avec un pierre ou une feuille)
            #alors retourne "le joueur gane"
        #ou sinon la variable ennemie est égale à 0 et la variable joueur est égale à 2 (l'ennemie gagne avec une pierre)
            #alors retourne "l'ennemie gane"
        #ou sinon la variable joueur est égale à 0 et la variable ennemie est égale à 2 (le joueur gagne avec une pierre)
            #alors retourne "le joueur gane"