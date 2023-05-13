
#Funcao Volume
def volume (comprimento, altura, largura):
    volume = (comprimento*altura*largura)/1000
    return volume

#Funcao Termostato
def potencia_termostato (volume, temperatura_desejada, temperatura_ambiente):
    potencia = volume * 0.05 * (temperatura_desejada - temperatura_ambiente)
    return potencia

#Funcao Filtragem
def qtd_filtragem (volume):
    min_filtragem = volume*2.5
    return min_filtragem

#Valores de entrada
#Aquario
comprimento = float(input("Digite o comprimento do aquario (cm): "))
altura = float(input("Digite a altura do aquario (cm): "))
largura = float(input("Digite a largura do aquario (cm): "))
#Entrada Termostato
temperatura_desejada = float(input("Digite a temperatura desejada para o aquario: "))
temperatura_ambiente = float(input("Digite a temperatura ambiente: "))

volume_aquario = volume(comprimento, altura, largura)
potencia = potencia_termostato(volume_aquario, temperatura_desejada, temperatura_ambiente)
filtragem = qtd_filtragem(volume_aquario)

#Saida
print('Volume do aquario em litros: ',volume_aquario)
print(f'Potencia necessaria para o Termostato: {potencia}W')
print(f'Quantidade minima de filtragem por hora é {filtragem} vezes')