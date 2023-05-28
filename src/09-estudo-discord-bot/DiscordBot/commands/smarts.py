from discord.ext import commands
from discord import app_commands
import discord
MY_GUILD = discord.Object(id=1110650990320963664)

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

class Smarts(commands.Cog):
    """A lot of Smart Commands"""
    def __init__(self, bot):
       self.bot = bot
    
    # @commands.command()
    # async def sync(self, ctx) -> None:
    #     fmt = await ctx.bot.tree.sync(guild=ctx.guild)
    #     await ctx.send(f"Synced {len(fmt)} commands")
    
    @app_commands.command(name="calcular", description="Calcula uma expressao")
    async def calculate_expression(self, interaction: discord.Interaction, expression:str):
        expression = ''.join(expression) #'|'.join coloca os valores da tupla em uma unica str cujo sep='|'
        response = eval(expression)
        await interaction.response.send_message("A resposta é: " + str(response))

    # Exercicio 01
    @app_commands.command(name="cadastrar", description="Cadastra aluno. Ex: SP2000 'Marcia Silva' marcia@gmail.com")
    async def student_register(self, interaction: discord.Interaction, prontuario:str, nome:str, email:str):
        with open("src/09-estudo-discord-bot/DiscordBot/alunos.txt", "r") as arquivo:
            arquivo_str = arquivo.read()
        if prontuario in arquivo_str or email in arquivo_str:
            await interaction.response.send_message("Aluno ja cadastrado")
        else:
            with open("src/09-estudo-discord-bot/DiscordBot/alunos.txt", "a") as arquivo:
                arquivo.write(f'{str(prontuario)},{str(nome)},{str(email)} \n')
            await interaction.response.send_message("Cadastrado com sucesso")
    
    # Exercicio 02
    @app_commands.command(name="listar-alunos", description="Exibi uma lista de alunos cadastrados")
    async def students(self, interaction: discord.Interaction):
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
        await interaction.response.send_message(embed=embed)

async def setup(bot):
    await bot.add_cog(Smarts(bot), guilds=[MY_GUILD])
