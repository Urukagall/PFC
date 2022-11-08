import random
"""
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

print(salaires(10,8,300))

def salairenet(net):
    return(net*1.25)
"""



alphabet="azertyuiopqsdfghjklmwxcvbn"
gagner=False


def hasard():
    y = alphabet[random.randint(0,25)]
    return y


while gagner == False:
    y=hasard()
    x=input()
    if x == y:
        gagner = True
        print("ganer")


def concatrucBarbitruc(str1, str2):
    return (str1 + "," + str2)




liste=[0,1,1,1,0,1,1,0,1]

def itere(tableau, nb):
    stringue="" #initialise la variable string
    for i in range (len(tableau)): #incrémente i jusqu'a la longueur de la liste
        if tableau[i] == nb and stringue == "": #si la valeur du tableau a l'index i est = à la valeur chercher et que le string est vide
            stringue = str(i) #prend la valeur en string de la valeur i 
        elif tableau[i] == nb: #si la valeur du tableau a l'index i est = à la valeur chercher
            stringue = stringue + ", " + str(i) #rajoute ", " et la valeur en string de i
    return stringue #returne stringue



