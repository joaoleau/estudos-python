"""Aula 03 - Metodos de Classes """
# Executar metodos sem instancias

class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    @classmethod
    def from_list(cls, lista):
        return cls(lista[0], lista[1])
    
    @classmethod
    def from_string(cls, rep_retangulo):
        base, altura = rep_retangulo.split(',')
        return cls(float(base), float(altura))
    
    def calcular_area(self):
        return self.base*self.altura
    
    def calcular_perimetro(self):
        return 2*(self.base + self.altura)

retangulo1 = Retangulo(10.0 , 5.0)
retangulo2 = Retangulo(6.0 , 3.0)
retangulo3 = Retangulo.from_list([20.0, 3.5])
retangulo4 = Retangulo.from_string('55.3,2')

# print(retangulo1.calcular_area())
# print(retangulo2.calcular_area())

# print(retangulo3.base, retangulo3.altura, retangulo3.calcular_area())
print(retangulo4.base, retangulo4.altura, retangulo4.calcular_area())