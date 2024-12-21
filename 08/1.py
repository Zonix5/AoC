file_path = "input.txt"
antenne_pos = {}
total = 0
noeud_set = set()

with open(file_path, "r") as fichier:
    contenu_fichier = [list(ligne.rstrip()) for ligne in fichier]

for x, row in enumerate(contenu_fichier):
    for y, item in enumerate(row):
        if item not in [".", "#"]:
            if item in antenne_pos:
                antenne_pos[item] += [(x, y)]
            else:
                antenne_pos[item] = [(x, y)]

def is_in_board(x, y):
    return 0 <= x < len(contenu_fichier) and 0 <= y < len(contenu_fichier[0])

for key in antenne_pos:
    for pos_base_index, pos_base in enumerate(antenne_pos[key]):
        dict_copy = antenne_pos[key][::]
        dict_copy.remove(pos_base)

        for other_pos in dict_copy:

            noeud_x = 2 * pos_base[0] - other_pos[0]
            noeud_y = 2 * pos_base[1] - other_pos[1]
            
            if is_in_board(noeud_x, noeud_y):
                noeud_set.add((noeud_x, noeud_y))

print(len(noeud_set))
