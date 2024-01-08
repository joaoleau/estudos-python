x: int = '2'
print(type(x))

lista:[int] = [2,3]
print(type(lista))

class Car:
    def __init__(self, nome:str) -> None:
        self.nome = nome
    def __str__(self) -> str:
        return self.nome
    def listar(self, lista:[int]) -> [int]:
        return lista

car1 = Car('Gol')
print(type(car1))

print(type(car1.listar([1,2,3])))

