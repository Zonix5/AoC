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

pos_x, pos_y = find_start()
while 0 <= pos_x < len(input) and 0 <= pos_y < len(input[0]):
    if input[pos_x][pos_y] == "#":
        direction = liste_direction[(liste_direction.index(direction) + 1) % len(liste_direction)]

    pos_x, pos_y = avancer(pos_x, pos_y, direction)

    if [pos_x, pos_y] not in liste_emplacement:
        liste_emplacement.append([pos_x, pos_y])

print(len(liste_emplacement))