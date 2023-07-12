"""Aula 03 - Tipos de Dados - Sets"""

# set(conjuntos)
# Nao ordenaveis
# Mutaveis
# Não indexaveis
# Não aceitam elementos duplicados

# Criar um Set
numeros = {1, 12, 5, 7, 4, 3, 3, 1}
print(numeros, type(numeros))

for numero in numeros:
    print(numero)

print(3 in numeros)
print(30 in numeros)

# Adicionar itens no Set
numeros.add(2)
print(numeros)

# Adicionar elemtos de um set em outro
numeros2 = {1, 5, 4, 3, 9, 22, 28}

todos_numeros = numeros.update(numeros2)  # Atualiza não cria um novo set
print(todos_numeros, type(todos_numeros))  # None

# Portanto utiliza:
numeros.update(numeros2)
print(numeros)
