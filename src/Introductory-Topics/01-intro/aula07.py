"""Aula 07 Input & Output"""
# print('hello', 'maria', 12, False, sep='&', end='!!!\n')

# sep='' --> separador
# end='' --> final

# arquivo = open('nomes.txt', 'w', encoding='utf-8')
# print('joao@gmail,com',
#       'maria@gmail.com',
#       file=arquivo,
#       sep=';'
#       )

# Entrada

# nome = input('Digite seu nome: ')
# idade = int(input('Digite sua idade: '))

# if idade >= 18:
#     print(f'{nome}, voce e maior de idade')
#     print('adsjdasdsj', nome, 'asdnadskjfkçla')
# else:
#     print(f'{nome}, voce e menor de idade')


# File
arquivo_notas = open('notas.txt', 'r', encoding='utf-8')
conteudo = arquivo_notas.read()
notas = conteudo.split(sep=';')

notas = [float(nota) for nota in notas]

print(notas)

media = (notas[0] + notas[1] + notas[2]) / len(notas)
print(media)

# #################
