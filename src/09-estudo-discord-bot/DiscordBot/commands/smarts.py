from discord.ext import commands
from discord import app_commands, ui
import discord
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Spacer, Table, TableStyle, Paragraph
MY_GUILD = discord.Object(id=1110650990320963664)

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

async def create_pdf():
    doc = SimpleDocTemplate("D:/Faculdade/VisLab/estudos_python/src/10-estudo-reportlab/alunos.pdf", pagesize=letter)

    # Estilos
    styles = getSampleStyleSheet()
    # Estilo Titulo
    titulo_style = styles['Heading1']
    titulo_style.fontSize = 20

    # Estilo Tabela
    # Criar estilo para a tabela
    estilo_tabela = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.black),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 16),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),

        ('BACKGROUND', (0, 1), (-1, -1), colors.white),
        ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 12),
        ('ALIGN', (0, 1), (-1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('BOTTOMPADDING', (0, 1), (-1, -1), 6),
        ('TOPPADDING', (0, 1), (-1, -1), 6),

        ('LINEABOVE', (0, 0), (-1, -1), 1, colors.black),
        ('LINEBELOW', (0, 0), (-1, -1), 1, colors.black),
        ('LINEBEFORE', (0, 0), (-1, -1), 1, colors.black),
        ('LINEAFTER', (0, 0), (-1, -1), 1, colors.black)
    ])

    # Conteudo
    conteudo = []

    # -============== PDF ==================-
    # Titulo
    titulo = Paragraph('Alunos Cadastrados', titulo_style)
    conteudo.append(titulo)

    conteudo.append(Spacer(1, 15))

    # Tabela
    dados = [['Prontuario', 'Nome', 'Email']]
    qtd_cadastro = 0
    with open("src/09-estudo-discord-bot/DiscordBot/alunos.txt", "r") as arquivo:
        for linha in arquivo.readlines():
            linhas = linha.split(',')
            dados.append(linhas)
            qtd_cadastro += 1

    tabela = Table(dados)
    tabela.setStyle(estilo_tabela)
    conteudo.append(tabela)

    conteudo.append(Spacer(1, 15))

    num_cadastro = Paragraph(f'Quantidade de cadastros: {qtd_cadastro}')
    conteudo.append(num_cadastro)
    
    # Construido
    doc.build(conteudo)


#Exercicio 04
class Cadastro(ui.Modal, title='Cadastro'):
    
    def __init__(self):
        super().__init__()
        self.prontuario = ui.TextInput(label="Prontuario", style=discord.TextStyle.short)
        self.nome = ui.TextInput(label="Nome", style=discord.TextStyle.short)
        self.email = ui.TextInput(label="Email", style=discord.TextStyle.short)

        # Visualização do Modal
        self.add_item(self.prontuario)
        self.add_item(self.nome)
        self.add_item(self.email)

    async def cadastro(self, interaction: discord.Interaction):
        prontuario = self.prontuario.value
        nome = self.nome.value
        email = self.email.value
        
        with open("src/09-estudo-discord-bot/DiscordBot/alunos.txt", "r", encoding="utf-8") as arquivo:
            arquivo_str = arquivo.read()
        
        if prontuario in arquivo_str or email in arquivo_str:
            await interaction.response.send_message("Aluno ja cadastrado")

        else:
            with open("D:/Faculdade/VisLab/estudos_pythonsrc/09-estudo-discord-bot/DiscordBot/alunos.txt", "a", encoding="utf-8") as arquivo:
                arquivo.write(f'{prontuario},{nome},{email} \n')
            await interaction.response.send_message("Cadastrado com sucesso")


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

    # Exercicio 01 e 04
    @app_commands.command(name="cadastrar", description="Cadastra aluno")
    async def student_register(self, interaction: discord.Interaction):
        await interaction.response.send_modal(Cadastro())
        # with open("src/09-estudo-discord-bot/DiscordBot/alunos.txt", "r") as arquivo:
        #     arquivo_str = arquivo.read()
        # if prontuario in arquivo_str or email in arquivo_str:
        #     await interaction.response.send_message("Aluno ja cadastrado")
        #     # async def on_submit(self, interaction: discord.Interaction):
        #     #     await interaction.response.send_message(f'Aluno ja cadastrado')
        # else:
        #     with open("src/09-estudo-discord-bot/DiscordBot/alunos.txt", "a") as arquivo:
        #         arquivo.write(f'{str(prontuario)},{str(nome)},{str(email)} \n')
        #     await interaction.response.send_message("Cadastrado com sucesso")
    
    # Exercicio 02
    # Exercicio ReportLab
    @app_commands.command(name="listar-alunos", description="Exibi uma lista de alunos cadastrados")
    @app_commands.describe(option="Modo de listagem")
    @app_commands.choices(option=[
        discord.app_commands.Choice(name='Embed', value=1),
        discord.app_commands.Choice(name='Pdf', value=2)
    ])
    async def students(self, interaction: discord.Interaction, option:discord.app_commands.Choice[int]):
        
        if option.name == 'Embed':
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
        else:
            await create_pdf()
            with open("D:/Faculdade/VisLab/estudos_python/src/09-estudo-discord-bot/DiscordBot/alunos.pdf", "rb") as file:
                await interaction.response.send_message(file=discord.File(file, filename="alunos.pdf"))


            
            # Deu certo porra
            # async with aiohttp.ClientSession() as session:
            #     await create_pdf()

            #     # Abrir o arquivo PDF gerado
            #     with open("src/09-estudo-discord-bot/DiscordBot/alunos.pdf", "rb") as file:
            #         # Enviar o arquivo usando a webhook
            #         await session.post(webhook_url, data={"file": file})

async def setup(bot):
    await bot.add_cog(Smarts(bot), guilds=[MY_GUILD])