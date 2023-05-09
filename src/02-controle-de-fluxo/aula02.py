"""Aula 02 02 Instrucao if"""

#Python
#if condicao(bool):
#   codigos

#C, Java, C#, outras
#if(){
#   instrucao
#instrucao
# }

codigo_cliente = 32
desconto = 30.0
DESCONTO_ESPECIAL = desconto >= 20.0

#Tem qeu manter a indentação
#O ideal é um TAB
#Mas pode fazer com 1 espaço ou 2 ou 3 desde que se mantem para toda estrutura
if DESCONTO_ESPECIAL:
    print('Desconto Especial')
    print(codigo_cliente)
 #print(2+2)Da erro de identacao
else:
    print('Sem Desconto Especial')


nome = 'Leo'
print(len(nome))#3
# Nome tem que ter pelo menos 3 caracteres
if len(nome) < 3:
    print('Nome deve ter pelo menos 3 caracteres')
else:
    print('Nome válido')

NOME_INVALIDO = len(nome) < 3
if NOME_INVALIDO:
    print('Nome deve ter pelo menos 3 caracteres')
else:
    print('Nome válido')

NOME_VALIDO = len(nome) >= 3
if NOME_VALIDO:
    print('Nome válido')
else:
    print('Nome deve ter pelo menos 3 caracteres')

#Somente um exemplo ideal é evitar o uso de negacao
if not NOME_INVALIDO:
    print('Nome válido')
else:
    print('Nome deve ter pelo menos 3 caracteres')

# Nome tem que ter pelo menos 3 caracteres
# Idade tem que ser maior ou igual a 18
# exibir todos os erros no final apenas
nome = 'Le'
idade = 17
erros = []

NOME_INVALIDO= len(nome) < 3
if NOME_INVALIDO:
    erros.append('Nome tem que ter pelo menos 3 caracteres')

IDADE_INVALIDA = idade < 18
if IDADE_INVALIDA:
    erros.append('Idade tem que ser maior ou igual a 18')

if len(erros) != 0:
    print(erros)
else:
    print('Dados validos')

#False: False, None, 0, 0.0, string vazia '', lista, tupla, set vazia
#True: todo resto
if erros:
    print(erros)
else:
    print('Dados validos')

# if elif else

# Verifica se um numero é positivo ou negativo ou zero
numero = 3
if numero > 0:
    print('Maior que zero')
elif numero == 0:
    print('Zero')
else:
    print('Menor que zero')

# Calcule a media e verifique se as duas notas
# sao validas antes do calculo
n1 = 5.6
n2 = 10.0

NOTA1_VALIDA = 0<=n1<=10
NOTA2_VALIDA = 0<=n2<=10

# Cuidado com Ifs aninhados
if NOTA1_VALIDA and NOTA2_VALIDA:
        media = (n1 + n2)/2

        if media >=6:
            print('Aprovado')
        elif media >= 4:
            print('Recuperação')
        else:
            print('Reprovado')
else:
    print('Notas inválidas')