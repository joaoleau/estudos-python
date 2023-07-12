notas = []
qtd_notas = 3 #3 notas
contador = 0
while contador < qtd_notas:
    nota = int(input(f"Digite a {contador + 1}º nota"))
    notas.append(nota)
    contador += 1

soma = 0
for n in notas:
    soma += n

media = soma / len(notas)
print('Sua media é:', media)
