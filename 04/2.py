input_xmas = []
file_path = "input.txt"
total = 0

with open(file_path, "r") as fichier:
    for ligne in fichier:
        input_xmas.append(list(ligne.rstrip()))

def is_X_mas(ligne, index):
    mot = ""
    ligne_index = input_xmas.index(ligne)

    if ligne[index] == "M":
        resultat = ["MSAMS", "MMASS"]
    elif ligne[index] == "S":
        resultat = ["SMASM", "SSAMM"]
    else :
        return False

    for i in (0, 2):
        if 0 <= index+2 < len(ligne) and ligne_index + 2 < len(ligne):
            
            mot += input_xmas[ligne_index + i][index] + input_xmas[ligne_index + i][index + 2]
            
            if i == 0:
                mot +=  input_xmas[ligne_index + 1][index + 1]

    return mot in resultat


for ligne in input_xmas:
    for i in range(len(ligne)):
        if is_X_mas(ligne, i):
            total += 1
        
print(total)