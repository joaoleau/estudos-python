from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Spacer, Table, TableStyle, Paragraph

def create_pdf():
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

# create_pdf()

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
