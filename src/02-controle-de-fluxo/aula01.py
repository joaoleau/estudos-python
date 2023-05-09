"""Aula 01 - Operadores """
# Operadores aritmeticos

n1 = 10.2
n2 = 3.5
resultado = n1 + n2 + 8.5

print('1+1', 1+1, type(1+1))
print('1.2+1.3', 1.2+1.3, type(1.2+1.3))
print('resultado: ', resultado, type(resultado))

# Subtração
print(3-1)

# Multiplicação
print(3*2, type(3*2))

# Divisão
print(3/2, type(3/2))

# Modula->Resto divisão
print(3 % 2)

# Divisao sem resto, Floor Division
print(10 // 3)

# Potenciação
print(10**2)  # 100=10^2

# Operador de atribuição
x = 10.0  # = --> Atribuição
print(type(x))  # Float

# Operador de comparação
resultado = x > 10  # False
print(type(resultado))  # Bool

print('10==10', 10 == 10, type(10 == 10))  # 10==10 True ...
print('10!=10', 10 != 10, type(10 != 10))
print('10>10', 10 > 10, type(10 > 10))  # False
print('10<10', 10 < 10, type(10 < 10))  # False
print('10<=10', 10 <= 10, type(10 <= 10))  # True
print('10>=10', 10 >= 10, type(10 >= 10))  # True

# if x > 10.0 and resultado < 3.0 and x Simplificar
# condicao = x > 10.0 and resultado < 3.0 and x
# if condicao:

# Operadores Lógicos
print('True and True', True and True, type(True and True))  # Bool
print('True and False', True and False, type(True and False))
print('False and True', False and True, type(False and True))
print('False and False', False and False, type(False and False))

print('True or True', True or True, type(True or True))  # Bool
print('True or False', True or False, type(True or False))
print('False or True', False or True, type(False or True))
print('False or False', False or False, type(False or False))

condicao = True
print('not condicao', not condicao, type(not condicao))  # False

condicao = False
print('not condicao', not condicao, type(not condicao))  # True

# Operadores Especiais

# Is
# == comparar se dois valores são iguais
# is verificar se as variaveis apontam para o msm objeto em memoria
a = 10
b = 10.0
c = b
print(a == b, a == c, b == c)
print(a is b, a is c, b is c)

# In
# str, list, tuple, set, dic(chave)
frase = 'Você é um palavrao!'
print('palavrao' in frase, type('palavrao' in frase))

numeros = [1, 5, 2, 6]
print(10 in numeros)  # False
print(1 in numeros)  # True
# Mesmo comportamento com tuples, listas etc...

pessoa = {
    'nome': 'Maria',
    'idade': 22,
    'altura': 1.75
}

print('Maria' in pessoa)  # False
print('nome' in pessoa)  # True


"""TESTE"""
a = 18/7
print(a, int(a))  # Arredonda pra baixo
