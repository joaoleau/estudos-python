"""Aula 04 01 Introdução a Funções"""

# Função é um bloco que realiza uma tarefa especifica
# Dividir o problema em pequenas partes
# Evita duplicação de codigos

# 1. Standard Library Functions - built-in functions
# ex: print, len

print('Ola', 123, True)

nomes = ['Joao', 'Jorge', 'Joice']
tamanho_lista = len(nomes)
print(nomes, tamanho_lista)

print('\n \n \n \n')

# 2. User Defined Functions
# Definidas pelo desenvovledor
# Fazerem parte da solução do problema

# Declaração
# nome: saudacoes
# parametro: nenhum
# retorno: nenhum
def saudacoes():
    print('Ola')

# Chamada
saudacoes()


# Declaração
# nome: saudacoes
# parametro: nome
# retorno: nenhum
def saudacoes(nome):
    print(f'Ola {nome}')

# Chamada
saudacoes('Joao')
nomezinho = 'Jorge'
saudacoes(nomezinho) #Ou seja, parametro nao precisa ser igual a var

# Declaração
# nome: calcular_media
# parametro: nota1/2/3
# retorno: nenhum
def calcular_media(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3)/3
    print(media)

# Chamada
calcular_media(10.0, 3.0, 6.0) #Argumentos literais
n1 = 9.00
n2 = 3.70
n3 = 5.50
calcular_media(n1, n2, n3) #Argumentos variaveis

# Declaração
# nome: calcular_media
# parametro: nota1/2/3
# retorno: media
def calcular_media (nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3)/3
    return media

media = calcular_media(9.32, 2, 3.32)
print(media)
# Enviar um email
# Salvar no banco de dados
# Salvar no arquivo