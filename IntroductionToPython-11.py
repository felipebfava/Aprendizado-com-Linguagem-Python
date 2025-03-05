# Programação Orientada a Objetos (POO) em Python - Classes, Atributos e Métodos
# além de scripts básicos e funções para determinada solução de algum problema
# A criação do objeto se dá pela Classe dele, o nome de cada classe é padronizado: 'NomeClasse'
# Atributos são as características do objeto, como nome, idade, cor, largura, altura, etc
# Método será a função (opções) que o objeto pode fazer, aumentar volume, acessar netflix, ligar/desligar, etc

# A Classe object é a classe base (classe pai) de todas as classes

# Exemplo do Controle Remoto
# class ControleRemoto:
#     caracteristicas:
#     - cor
#     - altura
#     - largura
#     - profundidade

#     metodos:
#     - passar de canal
#     - mexer no volume
#     - desligar a tv

# uma instãncia é um objeto que usou a classe para ser criado
# controle = ControleRemoto()
# controle2 = ControleRemoto()
# 2 instâncias diferentes da mesma classe, com as mesmas características (atributos) e métodos

# __init__ é um método especial que é chamado quando a classe é instanciada
# init vem de inicialização, é o método construtor da classe
# self é uma referência ao objeto que está sendo criado
# self é uma convenção, pode ser qualquer nome, mas é recomendado usar self

# class ControleRemoto:
#     def __init__(self, cor, altura, largura, profundidade):
#         self.cor = cor
#         self.altura = altura
#         self.largura = largura
#         self.profundidade = profundidade

#     def passar_botao(self, botao):
#         if botao == '+':
#             print('aumentar volume')
#         elif botao == '-':
#             print('diminuir volume')


# # como coloquei de forma obrigatória adicionar qual os atributos da instância, o objeto não será criado (erro)
# controle = ControleRemoto('preto', '10cm', '2cm', '2cm')
# controle2 = ControleRemoto('cinza', '15cm', '3cm', '3cm')
# controle3 = ControleRemoto('', '', '', '') # criou o objeto vazio, não é recomendado

# # chamada de atributos
# print(controle.cor)
# print(controle3.cor)

# # chamada de métodos
# controle.passar_botao('+')
# controle3.passar_botao('-')


class Carros:
    def __init__(self, cor, ano):
        self.ano = ano
        self.cor = cor

        # se eu quiser mudar de cor preciso modificar o lista_cores
        # para não pertencer somente a função __init__
        # modificamos para self.lista_cores

        # lista_cores = ['preto', 'branco', 'prata', 'vermelho', 'azul']
        
        self.lista_cores = ['preto', 'branco', 'prata', 'vermelho', 'azul']

        if self.cor not in self.lista_cores:
            print('Cor inválida')
            print('Cores válidas:', self.lista_cores)
            raise Exception('Cor Inválida')
        
        self.ano_zero = '0'
        self.ano_atual = '2025'
        if self.ano < self.ano_zero:
            raise Exception('Ano Negativo Inválido')
        elif self.ano > self.ano_atual:
            raise Exception('Ano Inválido')
        else:
            self.ano = ano

    def mudar_cor(self, nova_cor):
        if nova_cor in self.lista_cores:
            self.cor = nova_cor

        elif nova_cor not in self.lista_cores:
            print('Cor inválida')
            print('Cores válidas:', self.lista_cores)

# o ano precisa ser como string
# carro1 = Carros('preto', 2020) # erro
# print(carro1.cor)

carro2 = Carros('prata', '2025') # certo
carro3 = Carros('azul', '0') # certo
# carro2 = Carros('prata', '2026') # Exception Ano Inválido
# carro2 = Carros('prata', '-2026') # Exception Ano Negativo Inválido


print(carro2.cor)
print(carro2.ano)

print(carro3.cor)
print(carro3.ano)

# carro1.mudar_cor('azul')
# print(carro1.cor)

# como a cor verde não existe na lista_cores
# a cor do carro1 não poderá ser verde
# carro1.mudar_cor('verde')
# print(carro1.cor)
