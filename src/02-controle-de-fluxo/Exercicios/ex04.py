codigo_funcionario = 'BR11000X'#input("Digite o identificador do funcionario (Exemplo: BR0000X): ")

codigo_numeros = codigo_funcionario[2:-1]

CODIGO_TAMANHO = len(codigo_funcionario) == 7
QUANTIDADE_NUMEROS = len(codigo_numeros) == 4
CODIGO_FUNCIONARIO = codigo_funcionario[:2] == 'BR'
CARACTER_X = codigo_funcionario[-1:] == 'X'

codigo_numeros = int(codigo_funcionario[2:-1])
TAMANHO_NUMERO = 0<=codigo_numeros<= 9999

erros= []
if not CODIGO_TAMANHO:
    erros.append('Codigo com tamanho incorreto')

if not QUANTIDADE_NUMEROS:
    erros.append('Erro na quantidade de numeros')

if not TAMANHO_NUMERO:
    erros.append('O identificador nao apresenta numeros inteiros entre 0001 e 9999')

if not CODIGO_FUNCIONARIO:
    erros.append('O identificador não inicia com a sequencias "BR"')
    
if not CARACTER_X:
    erros.append('O identificar não finaliza com o caracter X')

if len(erros)!=0:
    print(erros)
else:
    print('Valido')
