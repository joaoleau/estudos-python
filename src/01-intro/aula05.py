# Tipos de dados
# Int e Float
num = 18
num_float = 12.3

# String
nome = 'Joao'
sobrenome = 'Silva'
print(nome + sobrenome)
print(f'O {nome} {sobrenome} eh bom')

print(nome[0])  # J ->> 1 Caracter

print(nome.lower())  # Metodo lower
print(nome.upper())

print(1, 2, 3, 'kasd', sep='.')  # 1.2.3.kasd


# Listas
frutas = ['Banana', 'Maca']
print(frutas[1])

frutas.append('Abacaxi')  # Add 'Abacaxi' na lista
print(frutas)

for fruta in frutas:
    print(fruta.upper())

print(len(frutas))

# Conjuntos
resultado_sorteio = {10, 2, 4, 23}
print(resultado_sorteio)

resultado_sorteio.add(20)
print(resultado_sorteio)

# Dicionario
funcionario = {'nome': 'Kau',
               'idade': 18,
               'sobrenome': 'Silva'}

print(funcionario['sobrenome'])  # Chama pela chave

print(funcionario.keys())
print(funcionario.values())
