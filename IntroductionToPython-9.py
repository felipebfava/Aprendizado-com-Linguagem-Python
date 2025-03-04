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
# -- Exemplo --
# fila = deque(['João', 'Maria', 'José'])
# fila.appendleft('Pedro') # adiciona na esquerda
# print(fila)
# fila.append('Ana') # adiciona na direita
# print(fila)
# fila.popleft() # remove da esquerda
# print(fila)
# fila.pop() # remove da direita
# print(fila)

# from collections import deque

# # Estacionamento de Carros

# print('#-- Venha estacionar seu carro no estacionamento FIFO --#')

# estacionamento = deque(maxlen=12)

# while True:

#     print('\nEstacionamento atual:', list(estacionamento))

#     if len(estacionamento) == 0:
#         print('\nO estacionamento está vazio.')
#     elif len(estacionamento) == 3:
#         print('\nO estacionamento está cheio.')
#     else:
#         print(f'O estacionamento tem {3 - len(estacionamento)} vagas disponíveis.')

#     atividade = input('\nDeseja adicionar um carro ao estacionamento? (s/n): ').strip().lower()

#     if atividade == 'n':
#         print(f'\nEstacionamento atual: {list(estacionamento)}')
#         break
#     if atividade != 's':
#         print('\nEntrada inválida! Digite "s" para continuar ou "n" para sair.')
#         continue

#     if len(estacionamento) < 3:
#         carro = input('\nDigite o nome do carro que deseja adicionar: ')
#         estacionamento.append(carro)
#         print(f'\nO carro {carro} foi adicionado ao estacionamento.')
#     else:
#         print('O estacionamento está cheio!')


# while True:
    
#     if len(estacionamento) == 0:
#         print('\nO estacionamento está vazio.')
#         break

#     atividade = input('\nDeseja remover um carro do estacionamento? (s/n): ').strip().lower()
   
#     if atividade == 'n':
#         print(f'\nEstacionamento atual: {list(estacionamento)}')
#         break
#     if atividade != 's':
#         print('\nEntrada inválida! Digite "s" para continuar ou "n" para sair.')
#         continue

#     carro = estacionamento.popleft()
#     print(f'\nO carro {carro} foi removido do estacionamento.')
#     print(f'\nEstacionamento atual: {list(estacionamento)}')

# # Comando continue em loops while e for
# # O comando continue é usado para pular o código restante dentro do loop e começar a próxima iteração.