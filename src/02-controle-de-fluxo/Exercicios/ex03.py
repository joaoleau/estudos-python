codigo_funcionario = input("Digite o identificador do funcionario (Exemplo: BR0000X): ")

codigo_numeros = codigo_funcionario[2:-1]

VALIDACAO_INICIAL = len(codigo_numeros) == 4 and codigo_funcionario[:2] == 'BR' and codigo_funcionario[-1:] == 'X'

codigo_numeros = int(codigo_funcionario[2:-1])

if VALIDACAO_INICIAL:
    if 0<=codigo_numeros<= 9999:
        print('Valido')
else:
    print('Invalido')

