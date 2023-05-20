
def linha_para_dict(arquivo, chaves):
    for linha in arquivo.readlines():
        valores = linha.split(',')

    #dados = [chaves, valores]
    dicionario = {}
    i = 0
    while i<len(valores):
        # dados[0][0] : dados[1][0]
        # dados[0][1] : dados[1][1]
        """dados[0][i] : dados[1][i]"""
        #chaves[0] : valores[0]
        #chaves[1] : valores[1]
        """chaves[i] : valores[i]"""
        dicionario[chaves[i]] = valores[i].strip()
        i+=1

    return dicionario

chaves = ['prontuario', 'nome', 'email']

with open("src/06-arquivos/Exercicios/ex3.txt", "r") as arquivo:
    print(linha_para_dict(arquivo, chaves))
arquivo.close()