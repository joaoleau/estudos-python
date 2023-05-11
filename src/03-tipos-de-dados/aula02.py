"""Aula 02 - Tipos de Dados - Tuplas"""

# Tuplas
# Ordenadas
# Imutáveis
# Indexáveis iguais as listas

# Criação da tuplas
nomes = ('Maria', 'Joao', 'Pedro')
print(nomes, type(nomes))

# Acessar os elementos
print(nomes[0])
print(nomes[0:2])

# Modificar elementos (Nao e possivel pois é imutavel)
# nomes[1] = 'Carlos'

# Iteração
for nome in nomes:
    print(nome)

for i in range(len(nomes)):
    print(nomes[i])

nomes2 = 'Ana', 'Amelia', 'Marcos'  # Tambem é tupla omitindo ()
print(nomes2, type(nomes2))

# Unpack
# nome1 = nomes2[0]
# nome2 = nomes2[1]
# nome3 = nomes2[2]

nome1, nome2, nome3 = nomes2  # Tem q ter o msm num de var e elementos
print(nome1, nome2, nome3)

# Juntas duas tuplas
todos_nomes = nomes + nomes2  # Cria uma nova tupla com os valores
print(todos_nomes, type(todos_nomes))
