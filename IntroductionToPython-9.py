# baseado em https://docs.python.org/pt-br/3.13/tutorial/datastructures.html
# use 'ctrl + ;' para comentar e descomentar o código com as linhas selecionadas

# Usando listas como pilhas
# política o último a entrar é o primeiro a sair - LIFO

# pilha = []
# print('Pilha:')
# while True:

#     try:
#         inserir = int(input('Insira um valor numérico na pilha: '))
#         pilha.append(inserir)
#         print(f'O número é {inserir}.')


#         while True:
#             atividade = input('Deseja continuar? (s/n): ').strip().lower()
#             if atividade in ('s', 'n'):
#                 break
#             print('Inválido! Digite apenas "s" para continuar ou "n" para sair.')
        
#         if atividade == 'n':
#             break

#     except ValueError:
#         print('Digite um valor numérico válido.')   
# print(f'pilha atual: {pilha}')

# while pilha:
        
#     while True:
#         atividade = input('Você quer remover o último item da pilha? (s/n): ').strip().lower()
                
#         if atividade in ('s', 'n'):
#             break
#         print('Inválido! Digite apenas "s" para continuar ou "n" para sair.')

#     if atividade == 'n':
#         break
    
#     removido = pilha.pop()
#     print(f'O número {removido} foi removido da pilha. Pilha atual: {pilha}')
# print(f'pilha atual: {pilha}')



# Usando listas como filas
# política o primeiro a entrar é o primeiro a sair - FIFO
# appends e pops ao final da lista são rápidos
# porém inserts ou pop no início da lista são lentos por precisar de deslocamento
# utilize a classe collections.deque que foi projetada para ter inserções e remoções rápidas em ambos os lados

# from collections import deque


# fila = deque(['João', 'Maria', 'José'])
# fila.appendleft('Pedro') # adiciona na esquerda
# print(fila)
# fila.append('Ana') # adiciona na direita
# print(fila)
# fila.popleft() # remove da esquerda
# print(fila)
# fila.pop() # remove da direita
# print(fila)