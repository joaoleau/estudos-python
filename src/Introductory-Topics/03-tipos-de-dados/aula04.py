"""Aula 04 - Tipos de Dados - Dics"""

# Dic (dicionário)
# coleção de key-value
# key é unica sem copias
# Mutável

# Criar um dic
carro = {
    'marca':'Ford',
    'modelo':'Mustang',
    'ano':1964
    }

print(carro, type(carro))

# Acessar valores por chaves
print(carro['marca']) 
print(carro.get('marca')) #Mesma coisa ^^^^

# Pegar todas as chaves
print(carro.keys()) #'marca', 'modelo', 'ano'

# Pegar todos os valores
print(carro.values()) #'Ford', 'mustang', 1964

# Pares
print(carro.items())

# Verifica se a chave existe
print('ano' in carro)

# Adicionar chaves/valores dinamica
carro['cor'] = 'Azul' #'cor':'Azul'
print(carro)

print('\n')

# Remover items
marca = carro.pop('marca') #marca = 'Ford'
print(carro)
print(marca)#'Ford'

print('\n')

# Loop
for key in carro:
    print(key, carro[key], type(key))

for value in carro.values():
    print(value)

for key in carro.keys():
    print(key)

for key, value in carro.items():
        print(key, value)

aluno1 = {
     'nome':'Joao',
     'email':'joao@email.com',
     'notas': [0, 2.2, 4.5]
}

aluno2 = {
     'nome':'Maria',
     'email':'maria@email.com',
     'notas': [10, 2, 4.5]
}

alunos = [aluno1, aluno2]

for aluno in alunos:
     print(aluno['nome'], aluno['email'])
     for nota in aluno['notas']:
          print(nota)