"""Aula 4 - 02 Arguments: positional, keyword, default value"""

# Declarar funcao que soma dois numeros
def somar (n1, n2):
    return n1 + n2

# Argumentos posicionais
print(somar(10, 3.5))

# Argumentos nomeados (keyword)
print(somar(n1=3.0, n2=6.5))
print(somar(n2=5.0, n1=9.5))

print('---------------')

def dividir (dividendo, divisor):
    return dividendo/divisor

print(dividir(10.0,2.0))
print(dividir(divisor=3.0,dividendo=12.0))

print('---------------')

# Unpack list e tuplas OBS: Sem sets
numeros = [10, 5.5]
print(somar(numeros[0], numeros[1]))
print(somar(*numeros)) #Porem nº de elementos de numeros deve ser igual ao de parametros

# Unpack dict
numeros = {
    'n1':10.2,
    'n2':5.4
}
print(somar(**numeros))#Porem as str das keys deve ser igual ao parametro

# Declaração
# nome: saudacoes
# parametros: nome, saudacao
# retunr: string
def saudacoes(nome, saudacao='Oi'): #saudacao com default value
    return(f'{saudacao} {nome}')

print(saudacoes('Joao', 'Ola'))
print(saudacoes('Maria', 'Bom dia'))
print(saudacoes('Pedro')) #Oi Pedro --> saudacao default = Oi
print(saudacoes(nome='Karina'))
