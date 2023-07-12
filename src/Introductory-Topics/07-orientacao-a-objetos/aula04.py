"""Aula 04 - Propriedades"""
# Forma de controlar o acesso aos atributos duma instancia

class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    # Getter <-- Acessar o Valor get value
    @property
    def base(self): #Sempre passar o Self quando @property (propriedade)
        return self._base # _base = base
    
    # Setter <-- Setar o Valor set value
    @base.setter
    def base(self, value):
        if value<=0:
            raise ValueError("Base deve ser maior que 0")
        self._base = value

    @property
    def altura(self):
        return self._altura
    
    @altura.setter
    def altura(self, value):
        if value<=0:
            raise ValueError("Altura deve ser maior que 0")
        self._altura = value

    @classmethod #Sempre passar cls(Retangulo) quando usar @classmethod
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

retangulo1 = Retangulo(10.00, 0.0)
retangulo1.base = 30.0
retangulo1.altura = 0.0

print(retangulo1.base)