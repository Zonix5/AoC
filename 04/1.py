input_xmas = []
file_path = "input.txt"
total = 0

with open(file_path, "r") as fichier:
    for ligne in fichier:
        input_xmas.append(list(ligne.rstrip()))

def is_xmas_droite(ligne, index):
    if ligne[index] == "X":
        resultat = "XMAS"
    elif ligne[index] == "S":
        resultat = "SAMX"
    else :
        return False

    if index + 3 < len(ligne):
        return ''.join(ligne[index:index+4]) == resultat
    return False

def is_xmas_bas(ligne, index, direction):
    mot = ""
    ligne_index = input_xmas.index(ligne)

    if ligne[index] == "X":
        resultat = "MAS"
    elif ligne[index] == "S":
        resultat = "AMX"
    else :
        return False

    for i in range(1, 4):
        if ligne_index + i < len(input_xmas):
            if direction == "bas":
                new_index = index
            elif direction == "dia_gauche":
                new_index = index - i
            elif direction == "dia_droite":
                new_index = index + i

            if 0 <= new_index < len(input_xmas[ligne_index + i]):
                mot += input_xmas[ligne_index + i][new_index]
    
    return mot == resultat



for ligne in input_xmas:
    for i in range(len(ligne)):
        if is_xmas_droite(ligne, i):
            total += 1
        for direction in {"bas", "dia_gauche", "dia_droite"}:
            if is_xmas_bas(ligne, i, direction):
                total +=1
print(total)