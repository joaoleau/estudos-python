class Pessoa:
    def __init__(self, n: str, i) -> None:
        self.nome: str = n
        self.idade: int = i
    
    def __str__(self) -> str:
        return (f"{self.nome} {self.idade}")

    def _correr(self):
        

jorge = Pessoa("Jorge", 13)
print(jorge)