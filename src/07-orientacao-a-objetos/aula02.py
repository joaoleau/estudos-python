"""Aula 02 - Atributos de Classes e Instancias"""

# Classe Pessoa possui
# Atributos de instancia: nome e email
# Todos na class terao esse atributo
class Pessoa:
    especie = 'Humano' #<--- Atributo de calsse
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
    
pessoa1 = Pessoa('Maria da Silva', 'maria@email.com')
pessoa2 = Pessoa('Joao Santos', 'joao@email.com')

# Alterar um atributo de class na instancia
# So altera para aquela instancia
pessoa1.especie = 'Alien'

# Reatribuindo um novo valor para instancia de class
Pessoa.especie = 'Alien v2'

print(pessoa1.nome, pessoa1.email, pessoa1.especie)
print(pessoa2.nome, pessoa2.email, pessoa2.especie)

print(Pessoa.especie)