#Exercicio 2
contador = 0
numeros = []
print("Digite 3 valores\n")
breakpoint()
while contador<3:
    numeros.append(float(input(f"Digite o {contador + 1} numero: ")))
    contador += 1

def soma (n1, n2, n3):
    return (n1 + n2 + n3)

soma = soma(numeros[0], numeros[1], numeros[2])
print('O valor da soma e:', soma)
# print('O valor da soma e:', soma(numeros[0], numeros[1], numeros[2]))

#Ou usar literais
#print('O valor da soma e: ', soma(4.00, 32, 19.2))

