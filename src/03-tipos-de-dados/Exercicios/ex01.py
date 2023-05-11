numeros = input("Digite 3 numeros: ")
lista_numeros = numeros.split(',')

int_numeros = []
for numero in lista_numeros:
    int_numeros.append(int(numero))

maior = int_numeros[0]
menor = int_numeros[0]
for numero in int_numeros:
    if numero < menor:
        menor = numero
    if numero > maior:
        maior = numero

print('Maior:',maior, 'Menor:',menor)
