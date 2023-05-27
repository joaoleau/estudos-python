from discord.ext import commands

class Smarts(commands.Cog):
    """A lot of Smart Commands"""
    def __init__(self, bot):
       self.bot = bot
    
    @commands.command(name="calcular", help="Calcula uma expressao")
    async def calculate_expression(self, ctx, *expression):
        expression = ''.join(expression) #'|'.join coloca os valores da tupla em uma unica str cujo sep='|'
        response = eval(expression)
        await ctx.send("A resposta é: " + str(response))

    # Exercicio 01
    @commands.command(name="cadastrar", help="Cadastra aluno. Ex: SP2000 'Marcia Silva' marcia@gmail.com")
    async def user_register(self, ctx, prontuario, nome, email):
        with open("src/09-estudo-discord-bot/DiscordBot/alunos.txt", "r") as arquivo:
            arquivo_str = arquivo.read()
        if prontuario in arquivo_str:
            await ctx.send("Aluno ja cadastrado")
        elif email in arquivo_str:
            await ctx.send("Aluno ja cadastrado")
        else:
            with open("src/09-estudo-discord-bot/DiscordBot/alunos.txt", "a") as arquivo:
                arquivo.write(f'{str(prontuario)},{str(nome)},{str(email)} \n')
            await ctx.send("Cadastrado com sucesso")

async def setup(bot):
    await bot.add_cog(Smarts(bot))
