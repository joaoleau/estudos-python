class Projeto:
    def __init__(self, codigo,titulo,responsavel):
        self.codigo = codigo
        self.titulo = titulo
        self.responsavel = responsavel
        self.participacao = []

    def add_participacao(self, value):
        self.participacao.append(value)
    
    def print_participacao(self):
        for participacao in self.participacao:
            print(participacao)

    @classmethod
    def from_string(cls, string):
        codigo, titulo, responsavel = string.split(',')
        return cls(codigo, titulo, responsavel)
    
    # Getter Codigo
    @property
    def codigo(self):
        return self._codigo

    # Setter Codigo
    @codigo.setter
    def codigo(self, value):
        if len(value)==0:
            raise ValueError("Codigo invalido")
        self._codigo = value
    
    # Getter Titulo
    @property
    def titulo(self):
        return self._titulo

    # Setter Titulo
    @titulo.setter
    def titulo(self, value):
        if len(value)==0:
            raise ValueError("Titulo invalido")
        self._titulo = value
    
    # Getter Responsavel
    @property
    def responsavel(self):
        return self._responsavel

    # Setter Responsavel
    @responsavel.setter
    def responsavel(self, value):
        if len(value)==0:
            raise ValueError("Responsavel incorreto")
        self._responsavel = value

    def __eq__(self, value):
        if isinstance(value, self.__class__):
            return self.codigo == value.codigo
        return False
    
    def __hash__(self):
        return hash(self.codigo)

    def __str__(self):
        return f'Projeto[codigo = {self.codigo}, titulo = {self.titulo}, responsavel = {self.responsavel}]'

##################################################

class Participacao:
    def __init__(self, codigo, data_inicio, data_fim, aluno, projeto):
        self.codigo = codigo
        self.data_inicio = data_inicio
        self.data_fim = data_fim
        self.aluno = aluno
        self.projeto = projeto
    
    @classmethod
    def from_string(cls, string):
        codigo, data_inicio, data_fim, aluno, projeto = string.split(',')
        return cls(codigo, data_inicio, data_fim, aluno, projeto)
    
    def __str__(self):
        return f'Participacao[Codigo = {self.codigo}, Data Inicio = {self.data_inicio}, Data Fim = {self.data_fim}, Aluno = {self.aluno}, Projeto = {self.projeto}]'

#########################################################################

projeto1 = Projeto("9999","Laboratório de Sistema","Ana")
projeto2 = Projeto("9900","Tecnologia no ensino","Bruno")


participacao1 = Participacao('21','05/05','17/10','Jorge','SI')
participacao3 = Participacao('23','05/05','17/10','Cerol','SI')
participacao2 = Participacao('22','05/06','1/11','Carlos','TI')

projeto1.add_participacao(participacao1)
projeto1.add_participacao(participacao3)
projeto2.add_participacao(participacao2)

print(projeto1)
for part in projeto1.participacao:
    print(part)




