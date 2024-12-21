from time import perf_counter
from tqdm import tqdm
import re

pattern = r"'\.']\s*,\s*\['\.'"
file_path = "input.txt"

with open(file_path, "r") as fichier:
    contenu_fichier = list(fichier.read())

def etape_1():
    index = 0
    result = []
    for i, chiffre in enumerate(contenu_fichier):
        if i % 2 == 0:
            for j in range(int(chiffre)):
                result.extend([str(index)])
            index += 1
        else:
            result.extend(["."] * int(chiffre))

    return result

def lier(liste):
    result = []
    index = 0
    while index < len(liste):
        petit_result = []
        i = 0

        while index+i  < len(liste) and liste[index] == liste[index+i]:
            petit_result.append(liste[index+i])
            i += 1
        
        result.append(petit_result)
        index += i
    return result
        
def point(nombres):
    result = []
    for item in nombres:
        if "." in item and item not in result:
            result.append(item)
    return result

def etape_2():
    nombres = lier(etape_1())

    liste_nombre = [item for item in reversed(nombres) if "." not in item]
    nombres_final = nombres.copy()

    for nombre in tqdm(liste_nombre, desc="Traitement en cours"):
        longeur_nombre = len(nombre)
        for points in point(nombres_final):
            longeur_points = len(points)
            if longeur_nombre > longeur_points or nombres_final.index(nombre) <= nombres_final.index(points):
                continue
            
            nombres_final[nombres_final.index(nombre)] = ["."] * longeur_nombre
            
            nombres_final[nombres_final.index(points)] = nombre
            
            if longeur_nombre-longeur_points:
                nombres_final.insert(nombres_final.index(nombre)+1, ["."] * (longeur_points-longeur_nombre))
            
            nombres_final = eval(re.sub(pattern, "'.', '.'", str(nombres_final)))
            break

    return nombres_final
    
def etape_3():
    nombres = etape_2()
    final = []
    for i in nombres:
        final.extend(i)

    nombres = final

    total = 0
    index = 0
    for chiffre in nombres:
        if chiffre != ".":
            total += index*int(chiffre)
        index += 1

    return total

if __name__ == "__main__":
    start_time = perf_counter()
    print(etape_3())
    print(f"Temps d'exécution : {perf_counter() - start_time}")