import re

total = 0
file_path = "input.txt"

with open(file_path, "r") as fichier:
    matches = re.findall(r"do\(\)|don\'t\(\)|mul\(\d+,\d+\)", fichier.read())

def mul(x, y):
    return x*y

do = True
for match in matches:
    do = match == "do()" if match in {"do()", "don't()"} else do

    total += eval(match) if do and match not in {"don't()", "do()"} else 0

print(total)