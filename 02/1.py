file_path = "input.txt"
total = 0
liste_levels = []

# Extraire le contenu du fichier
with open(file_path, "r") as fichier:
	for ligne in fichier:
		levels = ligne.split()

		# Recuperer les chiffres sous forme de integer
		levels = [int(v) for v in levels if v.lstrip('-').isnumeric()]

		liste_levels.extend([levels])

# Verifie si la liste est croissante
def is_croissant(liste):
	if sorted(liste) == liste:
		return True
	return False

# Verifie si la liste est décroissante
def is_decroissant(liste):
	if sorted(liste, reverse=True) == liste:
		return True
	return False

# Verifie si la liste est safe ou pas
def is_level_safe(level):
	difference_safe = {1, 2, 3}
	if is_croissant(level) or is_decroissant(level):
		for i, chiffre in enumerate(level):
			
			if i+1 < len(level):
				nombre_suivant = level[i+1]

				if abs(chiffre - nombre_suivant) not in difference_safe:
					return False
		return True

for level in liste_levels:
	if is_level_safe(level):
		total += 1
		
					
print(total)