"""Aula 01 - 06 Arquivos"""

# Open --> Funçao p abrir arquivo

# open("caminho", "modulo")
#Tipos de modulos:
# r - Read / Leitura
# a - Append / Incrementar
# w - Write / Escrita  
# x - Create -> Criar arquivo
# r+ - Leitura + Escrita

# arquivo = open("src/06-arquivos/test3.txt", "w")

# print(arquivo.readable()) # Verificar se o arq pode ser lido
# print(arquivo.read()) # Retorna o Arquivo em Str
# x = arquivo.read() # Type X é str

# print(arquivo.readline()) # Faz a leitura linha a linha
# print(arquivo.readline()) # 2 linha....
# print(arquivo.readline()) # 3 linha
# print(arquivo.readline()) # 4 linha

# lista = arquivo.readlines() # Retorna uma lista com conteudo das linhas
# print(lista)
# print(lista[2])

# arquivo.write("C\n")
# arquivo.write("COBOL\n")
# arquivo.write("C++\n")

# arquivo.write("Python\n")

# lista = ['joao', 'ze', 'minhoca']
# arquivo.writelines(lista)



# arquivo.close() #SEMPRE

# Importando Biblioteca do SO
import os

# Removendo arquivo
# if os.path.exists("src/06-arquivos/test3.txt"):
#     os.remove("src/06-arquivos/test3.txt")
# else:
#     print("Nao existe")

# Removendo pasta sem conteudo
# os.rmdir("src/06-arquivos/novapasta")

#ABRINDO COM WITH
with open("src/06-arquivos/test3.txt", "w") as arquivo:
    arquivo.write('Teste')

print('Fim')


