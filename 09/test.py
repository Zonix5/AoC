from time import perf_counter

file_path = "input09.txt"

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

def dernier_nombre(nombres):
    return (item for item in reversed(nombres) if item and isinstance(item, str) and item.isdigit())

def lier_point(nombres):
    nombres_final = []
    for item in nombres:
        nombres_final.append(item.rstrip("."))
        nombres_final.append("."*item.count("."))

    nombres_final = [item for item in nombres_final if "" != item]
    # print(nombres_final)
    nombres = nombres_final

    for index in range(len(nombres)):
        suivant = True
        while suivant:
            if index +1 > len(nombres)-1:
                suivant = False
                continue
            if any(c in nombres[index+1] for c in nombres[index]):
                item = nombres[index+1]
                nombres.pop(index+1)
                nombres[index] += item
                
            if index +1 <= len(nombres)-1:
                suivant = any(c in nombres[index+1] for c in nombres[index])
            else :
                suivant = False

    return nombres

def premier_point(nombres):
    return (item for item in nombres if "." in item)

def etape_2():
    nombres = lier_point(etape_1())
    liste_nombre = [item for item in reversed(nombres) if "." not in item]
    nombres_final = nombres.copy()

    for nombre in liste_nombre:
        for point in premier_point(lier_point(nombres_final)):
            nombres_final = lier_point(nombres_final)
            if len(nombre) <= len(point) and nombres_final.index(nombre) > nombres_final.index(point):
                nombres_none = [None]*len(nombres_final)
                nombres_none[nombres_final.index(point)] = nombre + "."*(len(nombres_final[nombres_final.index(point)])-len(nombre))
                nombres_none[nombres_final.index(nombre)] = "."*len(nombre)
                for i in nombres_none:
                    if i != None:
                        nombres_final[nombres_none.index(i)]=i
                break

    return nombres_final


def etape_3():
    nombres = "".join(etape_2()) 
    print(nombres)  
    total = 0
    index = 0
    for chiffre in nombres:
        if chiffre != ".":
            total += index*int(chiffre)
            index += 1

    return total

if __name__ == "__main__":
    start_time = perf_counter()
    etape_3()
    print(f"Temps d'exécution : {perf_counter() - start_time}")