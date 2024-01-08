

pessoa = {
    'nome':'Aline',
    'sobrenome':'Silva'
}

dados_pessoa = {
    'idade':12,
    'altura':1.8
}

def parametros(*args, **kwargs):
    print(*args, **kwargs)
    return

parametros('Jorge', 'Bruno', 'Maria', 'Osmar', 'Paulo')