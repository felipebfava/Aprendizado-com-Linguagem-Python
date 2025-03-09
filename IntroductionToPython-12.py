# Projeto: Manipulando imagens em python

# importando bibliotecas - pip install pillow
import PIL
from PIL import Image, ImageFilter


imagem = Image.open("imagens/flor_rosa.jpg")

# exibir
# imagem.show() # 1 imagem de cada vez

# salvar imagem como outro arquivo
# imagem.save("imagens/flor_rosa.png")

# .jpg para .png funciona
# .png para .jpg pode não funcionar
# precisa converter a imagem para padrão rgb
# imagem_rgb = imagem.convert("RGB")
# imagem_rgb.save("imagens/flor_rosa.jpg") # .png para .jpg

# mudar tamanho de imagem
# o tamanho tem que ser menor
# tamanho = (300, 300) # largura x altura em tupla
# imagem.thumbnail(tamanho)
# imagem.save("imagens/flor_rosa 300.jpg") # redimensionada para altura = 300 - garantindo proporção

# editar as imagens
# mudar cor, filtro ou orientação
# rotacionar
# imagem.rotate(90).save("imagens/flor_rosa rotacionada.jpg")
# # em graus

# coverter cores
# imagem.convert("L").save("imagens/flor_rosa preto e branco.jpg") # escala de cinza

# filtros
# imagem.filter(ImageFilter.GaussianBlur(15)).save("imagens/flor_rosa borrada.jpg")
