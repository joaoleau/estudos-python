tupla_numeros = (1, 2, 3, 4, 5, 6)


def soma(tupla_numeros):
    soma = 0
    contador = 0
    while contador < len(tupla_numeros):
        soma += tupla_numeros[contador]
        contador += 1
    return soma


print(soma(tupla_numeros))
