# Os dois funcionam
# Python é case sensitive, isso é, diferencia maiúsculas de minúsculas
print('Olá, Mundo')
print("Olá, Mundo!")

# imprimindo mensagens com variáveis
x = 4
print("7 +", 7 + x, "=", 7 + 7 + x)

# nesse caso o '+' serve para unir strings
print("Olá, " + "Mundo")

x = 2.5
y = -4

# declaração if com uma linha
if(y > 0) :
    print('y é positivo')
elif(y == 0) : print(y)
else : print('y é negativo')

# declaração if com mais linhas
if(x > 0) :
    print('x é positivo')
    print(x)
elif(x == 2) : print(x)
else:
    # equivalente do else if
    print('x é negativo')
    print(x)

# declaração dentro de uma função
y = 4
print(y if (y > 0) else 'y é negativo')

# função for
# função range cria uma lista de números, nesse caso de 0 a 4
for i in range(5) : print(i)

# função foreach
i = foreach = [1, 2, 3, 4, 5]
print(i)

# função while
x = 4
while (x > 0):
    x -= 1
    print(x)
# x = x - 1 é igual a x -= 1


