liste_1 = []
liste_2 = []
nombre_final = 0

# Separer les 2 nombres de la ligne
def separe_nombre(nombres):
    global liste_1, liste_2
    nombres = nombres.split()
    liste_1.append(nombres[0])
    liste_2.append(nombres[1])

# Extraire les nombres du fichier
with open("input.txt", "r") as fichier:
	for ligne in fichier:
	    separe_nombre(ligne)

# Compter le score de similarité (nombre * nombre de fois dans l'autre liste)
for nombre in liste_1:
	occurence = liste_2.count(nombre)
	nombre_final += int(nombre)*occurence

# Resultat
print(nombre_final)