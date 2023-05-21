   
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