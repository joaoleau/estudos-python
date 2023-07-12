from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
# 'colors' é usado para definir as cores
from reportlab.lib.colors import blue, green, red

# Definimos uma função create_pdf() que cria um objeto Canvas chamado 'c'
def create_pdf():
    # Criar o objeto Canvas
    # O 'canvas' é usado para criar e manipular o PDF
    # 'letter' é um tamanho de página pré-definido
    c = canvas.Canvas("D:/Faculdade/VisLab/estudos_python/src/10-estudo-reportlab/hello_world.pdf", pagesize=letter)

    # Desenhar o texto "Hello World"
    # setFont() para definir a fonte e o tamanho do texto
    c.setFont("Helvetica", 14)

    # drawString() para desenhar a string "Hello World" nas COORDENADAS (100, 700) da página.
    c.drawString(100, 700, "Hello World")

    # Desenhar formas geométricas
    # setFillColor() para definir a cor de preenchimento
    c.setFillColor(blue)
    
    # rect(), circle() e line() para desenhar as formas geométricas retângulo, círculo e linha, respectivamente:
    c.rect(100, 600, 100, 50, fill=True, stroke=False)
    c.setFillColor(green)
    c.circle(300, 625, 25, fill=True, stroke=False)
    c.setFillColor(red)
    c.line(100, 500, 300, 500)

    # Fechar o objeto Canvas
    c.save()

# Chamar a função para criar o PDF
create_pdf()
