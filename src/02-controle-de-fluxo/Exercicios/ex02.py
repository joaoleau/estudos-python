notas = []

entrada_notas = input("Digite as notas: ")
notas_str = entrada_notas.split()

for nota in notas_str:
    notas.append(int(nota))

soma = 0
for nota in notas:
    soma += nota

media = soma / len(notas)
print(media)
