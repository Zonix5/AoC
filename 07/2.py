from itertools import product
from tqdm import tqdm

file_path = "input.txt"
input = []
total = 0

def math_sans_priorite(liste_operation):
    resultat = 0
    operations = list(liste_operation)

    i = 0
    while i < len(operations):
        if operations[i] in ["+", "*", "||"]:
            operator = operations[i]
            if i+1 < len(operations):
                if operator == "||":
                    resultat = eval(f"{resultat}{operations[i+1]}")
                elif operator == "+":
                    resultat += int(operations[i+1])
                elif operator == "*":
                    resultat *= int(operations[i+1])
            i += 2
        else:
            if i == 0:
                resultat = int(operations[i])
            i += 1
    
    return resultat

with open(file_path, "r") as fichier:
    for ligne in fichier:
        final = []
        nombre = ""
        for i in ligne:
            if i.isnumeric():
                nombre += i
            else:
                if nombre != "":
                    final.append(nombre)
                    nombre = ""
                
        
        if nombre != "":
                final.append(nombre)

        input.append(final)

def trouver_factor(ligne):
    resultat = int(ligne[0])
    autre_nombre = ligne[1:]
    
    interval = len(autre_nombre)-1


    for i in product(["*","+", "||"], repeat=interval):
        factors = i

        result = []
            
        for j in range(len(autre_nombre)):
                
            if j < len(autre_nombre):
                result.append(autre_nombre[j])
            if j < len(factors):
                result.append(factors[j])

        if math_sans_priorite(result) == resultat:
            return resultat
                
    return 0
        


for ligne in tqdm(input, desc="Traitement de l'input"):
    total += trouver_factor(ligne)

print(total)