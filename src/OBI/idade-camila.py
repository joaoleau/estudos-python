idades = []

# Entradas
i = 0
while (i < 3):
    idade = int(input())
    if 5 <= idade <= 100:
        idades.append(idade)
        i += 1
    else:
        print("Idade incorreta")

def idade_camila(idades:list[int]):
    idades.sort()
    return idades[1]

print(idade_camila(idades))