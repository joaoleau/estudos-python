from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.styles import ParagraphStyle

def create_pdf():
    doc = SimpleDocTemplate("D:/Faculdade/VisLab/estudos_python/src/10-estudo-reportlab/meu_documento.pdf")
    styles = getSampleStyleSheet()

    # Conteúdo do documento
    content = []

    # Estilos
    title_style = styles['Title']
    paragraph_style = styles['BodyText']

    # Título
    title_text = "Título do Documento"
    title = Paragraph(title_text, title_style)
    content.append(title)

    # Espaço após o título
    content.append(Spacer(1, 20))

    # Parágrafo 1
    paragraph1_text = "Este é o primeiro parágrafo."
    paragraph1 = Paragraph(paragraph1_text, paragraph_style)
    content.append(paragraph1)

    # Espaço entre parágrafos
    content.append(Spacer(1, 15))

    # Parágrafo 2
    paragraph2_text = "Este é o segundo parágrafo."
    paragraph2 = Paragraph(paragraph2_text, paragraph_style)
    content.append(paragraph2)

    content.append(Spacer(1, 15))

    # Exercicio 01
    paragrafo_style = ParagraphStyle(
    name='MeuParagrafo',
    fontSize=12,
    leading=16,
    )

    paragrafo1_text = "Paragrafo do Exercicio 01"
    paragrafo1 = Paragraph(paragrafo1_text, paragrafo_style)
    content.append(paragrafo1)


    paragrafo_style.fontSize = 30
    paragrafo_style.fontName = 'Helvetica'
    paragrafo2_text = "Paragrafo 2 do Exercicio 01"
    paragrafo1 = Paragraph(paragrafo2_text, paragrafo_style)
    content.append(paragrafo1)

    # Adicionar o conteúdo ao documento
    doc.build(content)

# Chamar a função para criar o PDF
create_pdf()
