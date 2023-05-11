"""Version 2"""
print("Digite 3 valores inteiros")

lista_numeros = []
contador = 0
while contador<3:
    numeros = int(input(f"Digite o {contador + 1}º valor: "))
    lista_numeros.append(int(numeros))
    contador += 1

maior = lista_numeros[0]
menor = lista_numeros[0]
for numero in lista_numeros:
    if numero < menor:
        menor = numero
    if numero > maior:
        maior = numero

print('Maior:',maior, 'Menor:',menor)