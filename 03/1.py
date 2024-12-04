import re

pattern = r"mul\(\d+,\d+\)"
total = 0

file_path = "input.txt"
with open(file_path, "r") as fichier:
    content = fichier.read()

matches = re.findall(pattern, content)

def mul(x, y):
    return x*y

for mult in matches:
    total += eval(mult)

print(total)