class Moeda:
    def __init__(self, valor):
        self.valor = valor

    def metade(self):
        return f'R$ {(self.valor / 2)}'
    
    def dobro(self):
        return f'R$ {(self.valor * 2)}'
    
    def aumentar(self, aumentar):
        return f'R$ {(self.valor + ((self.valor * aumentar)/100))}'

    def diminuir(self, diminuir):
        return f'R$ {(self.valor - ((self.valor * diminuir)/100))}'
