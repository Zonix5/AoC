from time import perf_counter

file_path = "input.txt"
input_liste = []

positions = [
    (1, 0),
    (-1, 0),
    (0, 1),
    (0, -1)
]

with open(file_path, "r") as fichier:
    for ligne in fichier:
        input_liste.append(list(ligne.rstrip()))

def trouver_zero(input_liste=input_liste):
    position_zero = []
    for position, row in enumerate(input_liste):
            for index, nombre in enumerate(row):
                if nombre == "0":
                    position_zero.append((position, index))

    return position_zero

def verifier_prochains(start, queue=[]):
    result = []
    for position in positions:
            x_pro, y_pro = start[0] + position[0], start[1] + position[1]
            if x_pro < 0 or x_pro >= len(input_liste) or y_pro < 0 or y_pro >= len(input_liste[0]):
                continue
                
            if int(input_liste[x_pro][y_pro]) != int(input_liste[start[0]][start[1]])+1:
                continue
            if (x_pro, y_pro) not in result:
                result.append((x_pro, y_pro))
    
    return result

def main():
    total = 0
    for depart in trouver_zero():
        petit_total = []
        queue = verifier_prochains(depart)
        while queue:
            for item in queue:
                queue.remove(item)
                if input_liste[item[0]][item[1]] == "9":
                    petit_total.append(item)
                else:
                    queue.extend(verifier_prochains(item, queue))
        total += len(petit_total)
    return total

if __name__ == "__main__":
    start_time = perf_counter()
    print(main())
    print(f"Temps d'exécution : {perf_counter() - start_time}")