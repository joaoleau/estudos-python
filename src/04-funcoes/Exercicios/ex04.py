# Argumento especial *args  é útil quando não se sabe quantos argumentos serão passados para uma função
# Exercicio 4

def soma(*args):
    soma = 0
    for arg in args:
        soma += arg
    return soma


print(soma(1, 2, 6, 7))
