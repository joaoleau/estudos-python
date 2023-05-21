class Aluno:
    def __init__(self, prontuario,nome,email):
        self.prontuario = prontuario
        self.nome = nome
        self.email = email

    @classmethod
    def aluno_string(cls, string):
        prontuario, nome, email = string.split(',')
        return cls(prontuario, nome, email)
    
    # Getter Prontuario
    @property
    def prontuario(self):
        return self._prontuario

    # Setter Prontuario
    @prontuario.setter
    def prontuario(self, value):
        if len(value)==0:
            raise ValueError("Prontuario incorreto")
        self._prontuario = value
    
    # Getter Nome
    @property
    def nome(self):
        return self._nome

    # Setter Nome
    @nome.setter
    def nome(self, value):
        if len(value)==0:
            raise ValueError("Nome incorreto")
        self._nome = value
    
    # Getter Email
    @property
    def email(self):
        return self._email

    # Setter Email
    @email.setter
    def email(self, value):
        if len(value)==0:
            raise ValueError("Email incorreto")
        self._email = value

    def __eq__(self, value):
        if isinstance(value, self.__class__):
            return self.prontuario == value.prontuario
        return False
    
    def __hash__(self):
        return hash(self.prontuario)

    def __str__(self):
        return f'Aluno[Prontuario = {self.prontuario}, Nome = {self.nome}, Email = {self.email}]'


pessoa1 = Aluno.aluno_string("SP0101,João da Silva,joao@email.com")
print(pessoa1)

# # pessoa1 = Aluno.aluno_string("SP0101,João,joao@email.com")
# pessoa2 = Aluno.aluno_string("SP0101,João da Silva,joaosilva@email.com") 

# pessoa3 = Aluno.aluno_string("SP2221,Pedro,pedro@email.com") 

# # print(pessoa1)

# lista_pessoas = [pessoa1, pessoa2, pessoa3]
# print(lista_pessoas.count(pessoa1)) #--> 2