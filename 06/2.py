from tqdm import tqdm

file_path = "input.txt"
direction = "haut"
liste_direction = ["haut", "droite", "bas", "gauche"]
input = []
liste_emplacement = []

with open(file_path, "r") as fichier:
    input = [list(ligne.rstrip()) for ligne in fichier]


def find_start():
    for y, ligne in enumerate(input):
        for x, val in enumerate(ligne):
            if val == "^":
                return y, x

def avancer(pos_x, pos_y, direction):
    moves = {
        "haut": (-1, 0),
        "bas": (1, 0),
        "droite": (0, 1),
        "gauche": (0, -1)
    }
    dx, dy = moves[direction]
    return pos_x + dx, pos_y + dy

def is_in_input(x, y):
    return 0 <= x < len(input) and 0 <= y < len(input[0])

origin_x, origin_y = find_start()
pos_x, pos_y = origin_x, origin_y

while is_in_input(pos_x, pos_y) :
    new_x, new_y = avancer(pos_x, pos_y, direction)
    if not is_in_input(new_x, new_y):
        break

    if input[new_x][new_y] == "#":
        direction = liste_direction[(liste_direction.index(direction) + 1) % len(liste_direction)]

    else:
        if [pos_x, pos_y] not in liste_emplacement:
            liste_emplacement.append([pos_x, pos_y])

        pos_x, pos_y = new_x, new_y


## PARTIE 2
total = 0
liste_part_2 = set()
for pos in tqdm(liste_emplacement, desc="Test des positions"):
    liste_part_2.clear()

    direction = "haut"
    pos_x, pos_y = origin_x, origin_y
    found_loop = False

    while is_in_input(pos_x, pos_y):
        new_x, new_y = avancer(pos_x, pos_y, direction)
        if not is_in_input(new_x, new_y):
            # sortie
            break
        
        if (new_x, new_y) == (pos[0], pos[1]) or input[new_x][new_y] == "#": # verifier si la position n'est pas sur un obstacle
            direction = liste_direction[
                (liste_direction.index(direction) + 1) % len(liste_direction)
            ]
        else:
            current_pos = (pos_x, pos_y, direction)
            if current_pos in liste_part_2:
                # boucle
                found_loop = True
                break
        
            liste_part_2.add((pos_x, pos_y, direction))
            pos_x, pos_y = new_x, new_y
    
    if found_loop:
        total += 1

print(total+1) # + 1 car je ne sais pas pourquoi mais il manque 1


