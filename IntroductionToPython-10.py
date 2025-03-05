
# use ctrl + ; (no VsCode) para comentar/descomentar várias linhas de uma vez

# Mais sobre o comando continue em loops while e for
# O comando continue é usado para pular o código restante dentro do loop e começar a próxima iteração.
# exemplo pego da internet

# nota = 0
# while nota >= 0 or nota <= 10:
#    try:
#         nota = int(input("Informe a nota entre 0 e 10: "))
#         print("A nota foi:", nota)
#         break
#    except:
#        print("Valor inválido")
#        continue


# serve para definir uma variável e usá-la ao mesmo tempo
# vendas = int(input('Vendas do funcionário:'))
# if vendas > 1000:
#     bonus = 0.05 * vendas
# else:
#     bonus = 0
# print('Bonus:', bonus)

# exemplo do código acima usando ':=' walrus operator
# if(vendas:=int(input('Vendas do funcionário:'))) > 1000:
#     bonus = 0.05 * vendas
# else:
#     bonus = 0

# print('Bonus:', bonus)
# print('Vendas:', vendas)

# # exemplo da nota com o walrus operator
# while not (nota := input(f'Nota entre "0" e "10": ')).isdigit() or (nota := int(nota)) < 0 or nota > 10:
#   print('Valor INVÁLIDO!')
# print(nota)

# comando match case (cópia do switch case)
# alternativa para o uso de muitos if´s

# def fim_semana(dia):
#     match dia:
#         case 'Domingo' | 'Sábado':
#             return "Fim de Semana"
        
#         case 'Sexta-Feira':
#             return 'Sexta-Feira'

#         case _:
#             return 'Dia de Semana'

# print(fim_semana('Domingo'))
# print(fim_semana('Sábado'))
# print(fim_semana('Segunda-Feira'))
# print(fim_semana('Sexta-Feira'))
# # uso da barra vertical para incluir mais de um valor na mesma condição

# outro exemplo
# o input pega o valor como string, então é necessário converter para float
# a = float(input('Digite o número 1: '))
# b = float(input('Digite o número 2: '))
# operador = input('Digite o operador (+, -, *, /, %): ')

# def operacao(a, b, operador):
#     match operador:
#         case '+':
#             return a + b
#         case '-':
#             return a - b
#         case '*':
#             return a * b
#         case '/':
#             return a / b
#         case '%':
#             return a % b
#         case _:
#             return 'Operador inválido'
# print(operacao(a, b, operador))

# def contas(centros):
#     match centros:
#         case [area, centros]: # Apenas 1 centro de custo
#             print(f"A área {area} possui o seguinte custo {centros}")
#             # duas maneiras de imprimir o resultado

#         case [area, *centros]: #2 ou mais centros
#             print('A área {} possui os seguintes custos abaixo:'.format(area))
#             # duas maneiras de imprimir o resultado

#             for centro in centros:
#                 print (centro)
        
#         case _:
#             print('Erro ao processar a informação')

# contas(['Financeira', 'R$ 12.000,00'])
# contas(['Marketing', 'R$ 2.000,00','R$ 1.500,00','R$ 3.000,00'])

# utilizando enums
# importando a biblioteca enum
from enum import Enum

# # exemplo sobre os dias
# class Day(Enum):
#     MONDAY = 1
#     TUESDAY = 2
#     WEDNESDAY = 3
#     THURSDAY = 4
#     FRIDAY = 5
#     SATURDAY = 6
#     SUNDAY = 7

# today = Day.MONDAY
# print(today)
# print(today.name)
# print(today.value)

# # exemplo alerta de seguranca
# class SeverityLevel(Enum):
#     LOW = 1
#     MEDIUM = 2
#     HIGH = 3
#     CRITICAL = 4

# def alert(level):
#     if level == SeverityLevel.HIGH:
#         print('Faça algo imediatamente')

# alert(SeverityLevel.HIGH)

# class ProductCategory(Enum):
#     ELECTRONICS = 1
#     CLOTHING = 2
#     HOME = 3

# produto = {'nome': 'Laptop', 'categoria': ProductCategory.ELECTRONICS}
# print(f'Produto: {produto['nome']}, Categoria: {produto['categoria'].name}')

# print(ProductCategory.__members__) # mostra todos os membros da classe

# # usando for em Enum
# for i in ProductCategory:
#     print(i.name, i.value)

# # Para garantir que todos os membros da enumeração tenham valores exclusivos, use @unique.
# # Isso reforça que nenhum dos dois membros compartilhe o mesmo valor.

# from enum import unique

# @unique
# class UniqueColor(Enum):
#     RED = 1
#     BLUE = 2
#     GREEN = 3

# # pode usar auto() para auto incrementar os valores na chamada
# from enum import auto

# class ErrorCode(Enum):
#     SUCCESS = auto()
#     NOT_FOUND = auto()
#     SERVER_ERROR = auto()

# print(list(ErrorCode)) # imprime em lista com auto incremento