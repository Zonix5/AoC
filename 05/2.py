file_path = "input.txt"
total = 0
regles = []
liste_nombre = []
dict_regle = {}

with open(file_path , "r") as fichier:
    for ligne in fichier:
        if len(ligne.rstrip()) > 5:
            liste_nombre.append(ligne.rstrip().split(","))
        else :
            regles.append(ligne.rstrip().split("|"))

del(regles[-1])
liste = []

for regle in regles:
    if regle[0] not in liste:
        liste.append(regle[0])
    if regle[1] not in liste:
        liste.append(regle[1])

for chiffre in liste:
    liste1 = []
    liste2 = []
    for regle in regles:
        if regle[0] == chiffre:
            liste1.append(regle[1])
        elif regle[1] == chiffre:
            liste2.append(regle[0])

    dict_regle[chiffre] = liste1, liste2

def verifier_sequence(liste_nombres, dict_regle):
    for i in range(len(liste_nombres)):
        nombre_actuel = liste_nombres[i]
        nombres_suivants = liste_nombres[i+1:]
        
        for nombre_suivant in nombres_suivants:
            if nombre_suivant not in dict_regle[nombre_actuel][0]:
                return False
    
    return True

liste_invalide = []
for liste in liste_nombre:
    if verifier_sequence(liste, dict_regle) == False:
        liste_invalide.append(liste)

for liste in liste_invalide:
    regle_copie = dict_regle.copy()
    vraie_regle = {}
   
    for i, nombre in enumerate(liste):
       
        if nombre in regle_copie and nombre in liste:

            vraie_regle[nombre] = (
                [x for x in regle_copie[nombre][0] if x in liste],
                [x for x in regle_copie[nombre][1] if x in liste]
            )
       
        if i in regle_copie and i in liste:
            vraie_regle[i] = regle_copie[i]

    liste_final = [None] * len(vraie_regle)
    for i, clé in enumerate(vraie_regle):
        liste_final[len(vraie_regle[clé][1])] = clé

    total += int(liste_final[len(liste)//2])

print(total)