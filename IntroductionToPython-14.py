# Web scraping em python usando beautiful soup

# instalando bibliotecas
# pip install beautifulsoup4
# pip install requests

import requests
from bs4 import BeautifulSoup

# beautifulsoup funciona melhor em sites estáticos, como o google e sites de notícia
# para youtube não
# usando google

link = "https://www.google.com/search?q=cota%C3%A7%C3%A3o+d%C3%B3lar" # do google
# headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36"}

# para obter o headers (no Google)
# inspecionar > Network > Headers > General (minimiza) > Response Headers (minimiza) > Request Headers

# a requisição pode ser rastreada pelo navegador
# requisicao = requests.get(link, headers=headers)
requisicao = requests.get(link)
print(requisicao)

# print(requisicao.text) # código html
site = BeautifulSoup(requisicao.text, "html.parser") # le o html
# print(site.prettify()) # código printado mais bonito/organizado

# titulo = site.find("title") # passar o nome da tag html
# print(titulo)

# acha somente um input (qualquer)
# pesquisa = site.find("span")
# print(pesquisa)
# print(pesquisa[0]) # como é uma lista de input, posso fazer isso quando existir mais


# acha todas as correspondências de input, formato de lista
# pesquisa = site.find_all("div")
# print(pesquisa[0])

# pesquisa2 = site.find("input", name="q") # para nomes
# pesquisa2 = site.find("input", class_="gLFyf") # para classes
# print(pesquisa2)
# print(pesquisa2["value"]) # valor da tag

# cotacao_dolar = site.find("textarea", class_="gLFyf")
# cotacao_dolar = site.find(class_="SwHCTb")
# print(cotacao_dolar)
# print(cotacao_dolar["data-value"])
# print(cotacao_dolar.get_text()) # pega o texto da tag
