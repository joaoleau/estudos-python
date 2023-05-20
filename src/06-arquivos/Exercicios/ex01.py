
def carregar_dados_alunos (arquivo):
    
    dicionarios = []
    for linha in arquivo.readlines():
        conteudo = linha.split(',')
        # dicionario = {'prontuario':conteudo[0],'nome':conteudo[1],'email':conteudo[2]}
        # dicionarios.append(dicionario)
        dicionarios.append({'codigo':conteudo[0],'titulo':conteudo[1],'responsavel':conteudo[2].strip()})

    return tuple(dicionarios)

with open("src/06-arquivos/Exercicios/ex1.txt", "r") as arquivo:
    print(carregar_dados_alunos(arquivo))
arquivo.close()