# Projeto Tratamento de imagens

# importando bibliotecas
import cv2 # pip install opencv-python
import os

# o open cv executa numa janela a parte
imagem = cv2.imread("imagens/Pessoas_caminhando.jpg")

imagem_pb = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

imagem_invertida = cv2.bitwise_not(imagem_pb) #cores negativas

# 3 parâmetros
qtde_filtro = 95 # positivo e ímpar
imagem_blur = cv2.GaussianBlur(imagem_invertida, (qtde_filtro, qtde_filtro), 0)

imagem_blur_invertida = cv2.bitwise_not(imagem_blur)

imagem_desenho = cv2.divide(imagem_pb, imagem_blur_invertida, scale=256.0)


cv2.imshow("Pessoas_caminhando", imagem_desenho) # visualizar
cv2.waitKey(0) # quando fechar imagem para código tecla 0 = esc
cv2.destroyAllWindows()

# colocando em função para fazer com diversas imagens
def transformar_desenho(arquivo, qtde_filtro):
    imagem = cv2.imread(f"imagens/{arquivo}")

    imagem_pb = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

    imagem_invertida = cv2.bitwise_not(imagem_pb)

    imagem_blur = cv2.GaussianBlur(imagem_invertida, (qtde_filtro, qtde_filtro), 0)

    imagem_blur_invertida = cv2.bitwise_not(imagem_blur)

    imagem_desenho = cv2.divide(imagem_pb, imagem_blur_invertida, scale=256.0)

    cv2.imwrite(f"imagens_tratadas/{arquivo}", imagem_desenho) # salvando dentro de pasta específica

lista_arquivos = os.listdir("imagens") # lê todos os arquivos na pasta imagens

# transformar_desenho(arquivo, 45) # para um único arquivo

# para todos na lista
for arquivo in lista_arquivos:
    transformar_desenho(arquivo, 45)