"""Aula 06 - equal e hash code"""
nome1 = 'Joao'
nome2 = 'Joao'

print(nome1 == nome2) # True

class Pessoa:
    def __init__(self, cpf, nome):
        self.nome = nome
        self.cpf = cpf
    
    def __eq__(self, value):
        if isinstance(value, self.__class__):
            return self.cpf == value.cpf
        return False
    
    def __hash__(self):
        return hash(self.cpf)
    
    def __repr__(self):
        return f'Pessoa({self.cpf},{self.nome})'
    

pessoa1 = Pessoa('100100-10', 'Joao')
pessoa2 = Pessoa('100100-10', 'Joao')
pessoa3 = Pessoa('100100-11', 'Maria')

pessoas = {pessoa1, pessoa2, pessoa3}
print(pessoas)

lista_pessoas = [pessoa1, pessoa2, pessoa3]
print(lista_pessoas.count(pessoa1)) # 2 pq pessoa1 = pessoa2 baseado no __equal__
# Se nao tivesse __eq__ seria 1 ^^

# # Antes do def __eq__
# print(pessoa1 == pessoa2) # False nao ocupam o msm espaco de mem

# Depois do def __eq__
#print(pessoa1 == pessoa2) # True

