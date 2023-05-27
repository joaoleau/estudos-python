str = "Marcia,Silva,Leal"

# Escrita
with open("src/09-estudo-discord-bot/DiscordBot/dados.txt", "a") as arquivo:
    arquivo.write(f'{str} \n')

# Leitura
with open("src/09-estudo-discord-bot/DiscordBot/dados.txt", "r") as arquivo:
    dados = arquivo.read()
    # for linha in arquivo.readlines():
    #     dados = linha.split(',')
    # print(arquivo.readline())

print(dados)
# print(valor)