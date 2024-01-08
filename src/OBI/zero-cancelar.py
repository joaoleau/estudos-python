def somar(valores:list[int]):
    soma = 0
    for valor in valores:
        soma += valor
    return soma

valores_int = []

for num in range(10):
    valor_entrada = int(input())
    if valor_entrada == 0:
        valores_int.pop()
    else:
        valores_int.append(valor_entrada)

print(somar(valores_int))
    