# Estruturas de dados em python

# Listas
palavras = ['comer', 'jantar', 'almoçar', 'beber']
print(palavras) # printa toda a lista com quebra de linha
print('a primeira palavra da lista é', palavras[0]) # printa o primeiro elemento da lista


# posso usar um for para printar
print('\nusando for para printar a lista')
for i in palavras:
    print(i) # i eh o indice da lista, comecando em 0
print('-'*30)

# para saber o tipo de dado da variável
print(type(palavras))

# Lista é uma coleção ordenada e mutável. Permite membros duplicados
lista = ['carro', True, 2, 3.5]
print(type(lista)) # tipo lista como um todo
print(type(lista[0])) # tipo string do primeiro elemento
print(type(lista[1])) # tipo boolean do segundo elemento
print(type(lista[2])) # tipo int do terceiro elemento
print(type(lista[3])) # tipo float do quarto elemento

print('-'*30)

# Tuplas
# Tupla é uma coleção ordenada e imutável. Permite membros duplicados
tupla = ('carro', True, 2, 3.5)
print(tupla) # printa a lista sem quebra de linha
print(type(tupla)) # tipo tuple -> tupla

print('-'*30)
# Dicionários
# O dicionário é uma coleção ordenada e mutável. Nenhum membro duplicado é permitido
# nos dicionários trabalhos com chave e valor
dictionary = { "chave": "valor" }
print(dictionary)

dicionario = {
    'nome': 'João',
    'idade': 25,
    'masculino': True,
    'peso': 70,
    'altura': 1.75
}

print(dicionario) # printa a lista sem quebra de linha
print(type(dicionario)) # tipo dict -> dictionary/dicionário
print(dicionario['altura']) # printa o valor da chave 'altura'

print('-'*30)

# Conjuntos
# Set é uma coleção não ordenada e não indexada. Não há membros duplicados
# coleção / sets -> conjuntos
conjunto = {'carro', True, 2, 3.5}
print(conjunto)
print(type(conjunto)) # tipo set -> conjunto