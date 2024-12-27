from functools import lru_cache
from time import perf_counter


file_path = "input.txt"

with open(file_path, "r") as fichier:
    content = [int(x) for x in fichier.read().split()]

@lru_cache(maxsize=None)
def process_item(item, n):
    if n == 0:
        return 1
    n -= 1

    if item == 0:
        return process_item(1, n)
    
    item_str = str(item)
    if len(item_str) % 2 == 0:
        mid = len(item_str)//2
        return process_item(int(item_str[:mid]), n) + process_item(int(item_str[mid:]), n)

    return process_item(item*2024, n)

if __name__ == "__main__":
    start_time = perf_counter()
    resultat1 = resultat2 = 0
    for i in content:
        resultat1 += process_item(i, 25)
        resultat2 += process_item(i, 75)
    print(resultat1)
    print(resultat2)
    print(f"Temps d'exécution : {perf_counter() - start_time}")