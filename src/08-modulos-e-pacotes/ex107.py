import moeda
# valor = float(input('digite o valor: '))
valor = moeda.Moeda(float(input('digite o valor: ')))
print(f'A metade é: {valor.metade()}')
print(f'O dobro é: {valor.dobro()}')
print(valor.aumentar(200))
print(valor.diminuir(50))
