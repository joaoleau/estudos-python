"""Aula 02 05 Break & Continue"""

# for i in range(10):
#     if i == 4:
#         break
#     print(i)

# Encontrar a posição dum numero
# numa lista de inteiros
# Caso não encontre posição é igual a -1

busca = 7
numeros = [1, 4, 9, 7, 5, 3, 2, 1, 7]
posicao = 1

print('-=Procurando=-')
contador = 0
for numero in numeros:
    print('Procurando na posicao:', contador)
    if numero == busca:
        posicao = contador
        break

    contador += 1

print(posicao)

# Criando com Range
print('-=Procurando com Range=-')
for i in range(len(numeros)):
    print('Procurando na posicao:', i)
    if numeros[i] == busca:
        posicao = i
        break

print(posicao)

print('--=Continue=-')
# Continue
# Pular a iteração atual
numeros = [1, 2, 3, 4, 5]

for numero in numeros:
    if numero == 3:
        # break --> 1,2
        continue  # -->1,2,4,5
    print(numero)
