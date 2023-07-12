
def carregar_dados_projetos(arquivo):
    dicionarios = []
    for linha in arquivo.readlines():
        conteudo = linha.split(',')
        dicionarios.append({'codigo':int(conteudo[0]),'titulo':conteudo[1],'responsavel':conteudo[2].strip()})
    return tuple(dicionarios)

with open("src/06-arquivos/Exercicios/ex2.txt", "r") as arquivo:
    print(carregar_dados_projetos(arquivo))
arquivo.close()