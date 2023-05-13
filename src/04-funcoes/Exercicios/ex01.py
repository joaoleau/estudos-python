#Exercicio 01
contador = 0
numero = []
print("Digite 3 valores\n")
while contador<3:
    numero.append(float(input(f"Digite o {contador + 1} valor: ")))
    contador += 1

def somar (n1, n2 , n3):
    print('Resultado é: ',n1 + n2 + n3)

somar(numero[0], numero[1], numero[2])