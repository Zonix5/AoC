liste_1 = []
liste_2 = []
nombre_final = 0

# Separer les 2 nombres de la ligne
def separe_nombre(nombres):
    nombres = nombres.split()
    liste_1.append(nombres[0])
    liste_2.append(nombres[1])


# Extraire les nombres du fichier
with open("input.txt", "r") as fichier:
	for ligne in fichier:
	    separe_nombre(ligne)

# Classer les nombres du plus petit au plus grand
liste_1 = sorted(liste_1)
liste_2 = sorted(liste_2)

# Faire la difference entre le plus grand nombre et le plus petit pour chaque couple de nombre 
for i in range(len(liste_1)):
    chiffre_1 = int(liste_1[i])
    chiffre_2 = int(liste_2[i])
	
    nombre_final += abs(chiffre_1-chiffre_2)

# Resultat
print(nombre_final)


