from discord.ext import commands
import discord

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
    async def student_register(self, ctx, prontuario, nome, email):
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
    
    # Exercicio 02
    @commands.command(name="listar-alunos", help="Exibi uma lista de alunos cadastrados")
    async def students(self, ctx):
        embed = discord.Embed(
            title = "Lista de Alunos",
            color = 0x0000FF
        )
        embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar)
        with open("src/09-estudo-discord-bot/DiscordBot/alunos.txt", "r") as arquivo:
            i=1
            for linha in arquivo.readlines():
                embed.add_field(name=f"{i}º Aluno(a): ",value=linha, inline=False)
                i+=1
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Smarts(bot))
