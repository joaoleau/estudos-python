"""Aula 03 - 03 Loop For"""
# 1. Iteração em coleçao de elementos
# 2. Repetir instruções

linguagens = ['C', 'Python', 'Java']

# print(linguagens[0])
# print(linguagens[1])
# print(linguagens[2])

# for valor in colecao:
#   instruções

for linguagem in linguagens:
    print(linguagem.upper())


# Comportamento do operador in é
# diferente com base no contexto
print('Java' in linguagens)


nota1 = 10.0
nota2 = 5.5
nota3 = 8.3

media = (nota1 + nota2 + nota3)/3
print(media)

notas = [10.0, 5.6, 3, 3.4]

soma = 0
for nota in notas:
    soma = soma + nota

media = soma / len(notas)
print(media)


# Range
# valores = range(0, 10)
valores = range(10)  # [0, 10[
print(valores)

for valor in valores:
    print(valor)  # 0,1,2,3,4,5,6,7,8,9

# Step: range(0, 11, step)
valores = range(0, 10, 2)
for valor in valores:
    print(valor)

valores = range(10, 0, -1)  # 10,9,8,7,6,5,4,3,2,1
for valor in valores:
    print(valor)

for i in range(3):
    print(linguagens[i])

#Não faz muito sentido fazer isso
for i in range(len(linguagens)):
    print(linguagens[i])

#Pq vc tem isso
for linguagem in linguagens:
    print(linguagem)