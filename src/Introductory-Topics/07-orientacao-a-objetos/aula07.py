"""Aula 07 Relacionamento entre classes"""
class Endereço:
    def __init__(self, cep, numero):
        self.cep = cep
        self.numero = numero

    def __str__(self):
        return f'Endereço[cep={self.cep}, numero={self.numero}]'
        
        


class Telefone:
    def __init__(self, ddd, numero):
        self.ddd = ddd
        self.numero = numero
    
    def __str__(self):
        return f'Telefone[ddd={self.ddd}, numero={self.numero}]'
        

class Pessoa:
    def __init__(self, cpf, nome, telefone, endereco):
        self.cpf = cpf
        self.nome = nome
        self.telefone = telefone
        self.enderecos = [endereco]
    
    def add_endereco(self, endereco):
        self.enderecos.append(endereco)

    def print_enderecos(self):
        print(self.nome)
        for endereco in self.enderecos:
            print(endereco)
    
    def __str__(self):
        return f'Pessoa[cpf={self.cpf}, nome={self.nome}, telefone={self.telefone}]'
    
# pessoa = Pessoa('100100-10', 'Joao', Telefone('11', '99999-9999'))
telefone = Telefone('11', '99999-9999')

pessoa1 = Pessoa('100100-10', 'Joao', telefone, Endereço('022264-505', '034'))
pessoa1.add_endereco(Endereço('05864-505', '034'))
pessoa1.add_endereco(Endereço('05444-565', '14'))

pessoa2 = Pessoa('100100-11', 'Joice', telefone, Endereço('93334-565', '134'))
pessoa2.add_endereco(Endereço('00444-565', '134'))

# print(pessoa1)

# print(pessoa1.cpf, pessoa1.nome, pessoa1.telefone)
# print(pessoa1.telefone.ddd, pessoa1.telefone.numero)

pessoa1.print_enderecos()
# pessoa2.print_enderecos()
        