
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