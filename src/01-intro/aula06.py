"""Aula 06 Conversao de tipos"""
# Conversao de tipo implicita e explicita

leitura = 25.53
peso = 3
total = leitura * peso
print(total, type(total))

# Conversao explicita (type casting)
soma = 13.4 + float('3.4')
print(soma, type(soma))

idade = int('34')
print(idade, type(idade))

# mensagem = nome + 'tem a altuda de' + str(altura)
nome = 'Jorge'
altura = 21
mensagem = f'{nome} tem a altuda de {altura}'

print(mensagem, type(mensagem))  # str
