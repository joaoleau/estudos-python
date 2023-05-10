"""Aula 01 - Tipos de Dados - Listas"""

# Listas
# Ordenadas
# Mutáveis
# Indexáveis

# Exemplo de lista
nomes = ['Maria', 'Pedro', 'Joao']
print(type(nomes), nomes)

print(nomes[0])
print(nomes[0:2]) #[0,2[

# Modificar elementos
nomes[0] = 'Maria da Silva'
print(nomes)

nomes[1:] = ['Pedro do Santos', 'Joao Leal']
print(nomes)

#Tamanho da lista
# Funcao len
print(len(nomes)) #Numero de elementos da lista

# Adicionar elementos na lista
# Metodo append
nomes.append('Marta Gomes')
print(nomes)

# Inserir numa posicao especifica
# Metodo insert
nomes.insert(0, 'Leo Silva')
print(nomes)

nomes.insert(2, 'Gui Santos')
print(nomes)

# Inserir elementos de outra lista
# Metodo extend
print(len(nomes))
nomes2 = ['Flavio Macedo', 'Carlos Gomes']
nomes.extend(nomes2)
print(nomes)
print(len(nomes))

#Remover elementos da lista
# Metodo remove('Elemento') NAO E O ENDEREÇO
nomes.remove('Maria da Silva')

# Metodo del
del nomes[0] #Deleta o dado do endereço 0
print(nomes)

# REMOVE A LISTA DA MEMORIA
del nomes2

#Limpar a lista
# nomes.clear()
# print(nomes)

# Iteração em lista
for nome in nomes:
    print(nome)

for i in range(len(nomes)):
    print(nomes[i])
