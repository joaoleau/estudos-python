from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, Image

# Definir estilos
styles = getSampleStyleSheet()
titulo_style = styles['Heading1']
titulo_style.fontSize = 16

paragrafo_style = styles['BodyText']
paragrafo_style.fontSize = 12

# Criar conteúdo do PDF
conteudo = []

# Exercicio 02
#Imagem
caminho = "https://th.bing.com/th/id/R.dbd9636c8ed97aa4a5b7b83b96827778?rik=tBmOK2ohOPpBZw&riu=http%3a%2f%2fwww.reportlab.com%2fstatic%2fcms%2fimg%2flogo_bg.gif&ehk=KAaAWSOSG2Zqd4NwMQ4%2bPZSYErXwRmPc6phsZ%2bqvTho%3d&risl=&pid=ImgRaw&r=0"
imagem = Image(caminho,  height=100, width=300, hAlign = 'CENTER')
conteudo.append(imagem)

# Título
titulo = Paragraph('Título do Documento', titulo_style)
conteudo.append(titulo)

# Espaço após o título
espaco_titulo = Spacer(1, 20)  # 20pt de espaço
conteudo.append(espaco_titulo)

# Parágrafo
paragrafo = Paragraph('Este é um parágrafo de exemplo.', paragrafo_style)
conteudo.append(paragrafo)

# Espaço após o parágrafo
espaco_paragrafo = Spacer(1, 15)  # 15pt de espaço
conteudo.append(espaco_paragrafo)

# Tabela
dados = [['Coluna 1', 'Coluna 2', 'Coluna 3', 'Coluna 4'],
         ['Dado 1', 'Dado 2', 'Dado 3', 'Dado 4']]
tabela = Table(dados)
conteudo.append(tabela)

# Criar documento PDF
pdf_filename = 'exemplo.pdf'
doc = SimpleDocTemplate(f"D:/Faculdade/VisLab/estudos_python/src/10-estudo-reportlab/{pdf_filename}", pagesize=letter)

# Adicionar conteúdo ao documento
doc.build(conteudo)
