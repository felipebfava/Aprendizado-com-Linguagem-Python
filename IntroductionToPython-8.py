# o índice de lista começa com 0, 1, 2...
# de forma negativa começa no sentido inverso -3, -2, -1...
lista_compras = ['banana', 'laranja', 'maçã']
print(lista_compras[-2])

print('-'*30)

# append(x)
# adiciona somnete um único item no final da lista
lista_compras.append('pera')
print(lista_compras)

print('-'*30)

# insert(i, x)
# a.insert(0, x) insere um elemento na frente da lista
lista_compras.insert(1, 'morango') # adiciona um item na posição 1
print(lista_compras)

print('-'*30)

# remove(x) - remove um item da lista
# lista_compras.remove('carro') # erro, pois não existe o item 'carro' na lista_compras
lista_compras.remove('laranja')
print(lista_compras)

print('-'*30)

# pop(i) - remove um item da lista na posição i
lista_compras.pop(0) # remove o item na posição 0
print(lista_compras)
print('-'*30)

# remove todos os itens da lista
# lista_compras.clear()
print('-'*30)

# index(x) - retorna o índice do item x
# lista.index(item, inicio, fim)
# inicio e fim para casos de repetição do item
lista_compras = ['banana', 'laranja', 'maçã']
lista_compras.append('abacaxi')
lista_compras.append('banana')


# índice do segundo item banana
lista_compras.index('banana') # retorna o índice do item 'banana' na posição 0
# lista_compras.index('banana', 1, 4) # retorna o índice do item 'banana' entre as posições 1 e 4
print(lista_compras)
print('-'*30)

# count(x) - conta quantas vezes o item x aparece na lista
lista_compras.count('banana') # conta quantas vezes o item 'banana' aparece na lista
print('-'*30)

# reverse() - inverte a ordem dos itens da lista
lista_compras.reverse()
print(lista_compras)
print('-'*30)

# sort() - ordena os itens da lista

lista_compras.sort() # ordena os itens da lista de forma crescente
lista_compras.sort( reverse=False ) # o mesmo que o anterior
lista_compras.sort( reverse=True ) # ordena os itens da lista de forma decrescente
print(lista_compras)
print('-'*30)

tarefas = []

# testando o input
atividade = input('Informe qual atividade iremos fazer (enter para cancelar): ')
tarefas.append(atividade)
print(tarefas)
print('-'*30)

# inserir vários itens na lista
while atividade:
    atividade = input('Informe qual atividade iremos fazer (enter para cancelar): ')
    tarefas.append(atividade)
print(tarefas[:-1]) # pega os itens da posição [0] até o último item da lista [-1]
print('-'*30)

# for para printar as tarefas
for tarefa in tarefas:
    print(tarefas)
print('-'*30)

lojas = ['mercado', 'farmácia', 'padaria']
vendas = [100, 200, 300]
print(lojas+vendas) # concatena as duas listas
print('-'*30)

# unindo listas com tupla
resultados = []

for i in range(3):
    tupla = (lojas[i], vendas[i])
    resultados.append(tupla)
print(resultados)
print(resultados[1][1]) # acessa o item 1 da tupla 1
print('-'*30)

print(lojas*2) # repete/replica a lista lojas 2 vezes
print('-'*30)


# operador in - verifica se um item está na lista True/False
bool = 'padaria' in lojas # verifica se o item 'padaria' está na lista lojas
print(bool)
print('-'*30)

numeros = [1, 2, 3, 4, 5]
print('o valor máx da lista é:', max(numeros)) # retorna o maior número da lista
print('o valor min da lista é:',min(numeros)) # retorna o menor número da lista
print('a soma dos valores da lista é:',sum(numeros)) # retorna a soma dos números da lista
print('-'*30)

# copy() - copia a lista
print(numeros.copy())
print(lista_compras.copy())