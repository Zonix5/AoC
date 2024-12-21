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
    print(result)
    return result

def compter_point_fin(nombres):
    return len("".join(nombres)) - len("".join(nombres).rstrip("."))

def dernier_chiffre(nombres):
    index = len(nombres)
    for chiffre in reversed(nombres):
        index -= 1
        if chiffre.isdigit() :
            return chiffre, index

def etape_2():
    nombres = etape_1()
    i = compter_point_fin(nombres)
    while i != nombres.count(".") :
        chiffre, chiffre_index = dernier_chiffre(nombres)
        punt_index = nombres.index(".")
        del nombres[chiffre_index]
        nombres[punt_index] = chiffre
        i = compter_point_fin(nombres)

    return nombres

def etape_3():
    nombres = etape_2()
    
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
    #print(f"Temps d'exécution : {perf_counter() - start_time}")