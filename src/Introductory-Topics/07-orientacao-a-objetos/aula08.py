"""Aula 08 - Herança"""

class Pessoa: #CLASS PAI
    def __init__(self, nome , sobrenome, cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf

    def obtem_nome_completo(self):
        return f'{self.nome} {self.sobrenome}'
    
# class X(heranca)    
class Cliente(Pessoa): #SUBCLASS
    def __init__(self, nome, sobrenome, cpf):
        super().__init__(nome, sobrenome, cpf)
        self.compras = []
    


cliente1 = Cliente("Paulo", "Silva", 123)
print(cliente1.obtem_nome_completo())

class Funcionario(Pessoa):
    def __init__(self, nome, sobrenome, cpf, salario):
        super().__init__(nome, sobrenome, cpf)
        self.salario = salario
    
    def pagamento(self):
        return self.salario - ((10/100)*self.salario)

    def __str__(self):
        return f'Funcionario = [Nome = {self.nome}, Sobrenome = {self.sobrenome}, Cpf = {self.cpf}, Salario = {self.salario}]'

class Programador(Funcionario):
    def __init__(self, nome, sobrenome, cpf, salario, bonus):
        super().__init__(nome, sobrenome, cpf, salario)
        self.bonus = bonus
    
    def pagamento(self):
        pagamento_programador = super().pagamento()
        return pagamento_programador + self.bonus

    def __str__(self):
        return f'Programador = [Nome = {self.nome}, Sobrenome = {self.sobrenome}, Cpf = {self.cpf}, Salario = {self.salario}, Bonus = {self.bonus}]'


funcionario1 = Funcionario("Joao", "Andre", '100100-10', 1200)
print(funcionario1)

print(funcionario1.pagamento())

programador = Programador("Joao", "Andre", '100100-10', 1200, 200)
print(programador)

print('\n Pagamento total programador: ',programador.pagamento())

