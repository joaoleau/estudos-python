import re

# baralho = str(input)
baralho = "11P01C02C01U02U03U04U"
baralho_pattern = "[0-9]{2}[A-Z]"
cartas = re.findall(baralho_pattern, baralho)
print(cartas)

def verificar(cartas):
    for carta in carta:
        