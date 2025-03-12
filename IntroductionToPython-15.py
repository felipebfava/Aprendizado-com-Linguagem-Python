# usando selenium para automação

# instalando bibliotecas
from selenium import webdriver
import time

# selenium consegue lidar com sites dinâmicos
# recomendado com navegadores Google ou Firefox (previamente instalados)

# abrir navegador
navegador = webdriver.Chrome()
time.sleep(10)

# acessar site
navegador.get("https://www.hashtagtreinamentos.com/")

# colocar o navegador em tela cheia

navegador.maximize_window()

# selecionar um elemento na tela
botao_verde = navegador.find_element("class name", "botao-verde") # seleciona o primeiro elemento com tal característica

# clicar num elemento
botao_verde.click()

# para selecionar não somente o primeiro elemento
# vários elementos
lista_botoes = navegador.find_elements("class name", "header_titulo")
for botao in lista_botoes:
    if "Assinatura" in botao.text:
        botao.click()
        break

# navegar para um site diferente
navegador.get("https://www.hashtagtreinamentos.com/curso-python")

# selecionar uma aba
# abas = navegador.window_handles()
# navegador.switch_to.window(abas[1])
# cria uma lista com as abas > abas[0], abas[1]...

# escrever em um campo/formulário - se o site tiver

# navegador.find_element("id", "firstname").send_keys("Nome")
# navegador.find_element("id", "email").send_keys("algumemail@gmail.com")
# navegador.find_element("id", "phone").send_keys("21999999999")


# botao_clicar = navegador.find_element("id", "_form_2475_submit")

# dar scroll (colocar elemento na tela)
# comando em javascript
# navegador.execute_script("arguments[0].scrollIntoView({block: 'center'})", botao_clicar)
# preciso de um tempo para executar o script
# opção 1
# time.sleep(3)

# opção 2 - espera dinâmica
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# espera = WebDriverWait(navegador, 10) # tempo em segundos
# espera.until(EC.element_to_be_clickable(botao_clicar))
# botao_clicar.click()
# time.sleep(10)