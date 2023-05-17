dados_individuo = {
    'altura':0,
    'peso':0
}

dados_individuo['altura'] = float(input("Digite sua altura em metros: "))
dados_individuo['peso'] = float(input("Digite seu peso em kg: "))

def imc (altura, peso):
    return (peso / (altura * altura))

def classificacao (imc):
    if imc<18.5:
        return ('Baixo peso')
    elif 18.5<imc<24.9:
        return ('Peso normal')
    elif 25.0<imc<29.9:
        return ('Excesso de peso')
    elif 30.0<imc<34.9:
        return ('Obesidade de Classe 1')
    elif 35<imc<39.9:
        return ('Obesidade de Classe 2')
    else:
        return ('Obesidade de Classe 3')
    
def situacao_individuo (imc):
    if imc<18.5:
        return ('Ganhar peso')
    elif imc<24.9:
        return ('Peso normal')
    else:
        return ('Perder peso')
    
valor_imc = imc(dados_individuo['altura'], dados_individuo['peso'])

print('Seu IMC é de:', valor_imc)
breakpoint()
print('Classificacao: ',classificacao(valor_imc))
print('Situacao do individuo: ',situacao_individuo(valor_imc))