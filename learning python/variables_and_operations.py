A = 1 # variáveis
B = 2

print('Soma:')
print(A+B)

print('Subtração:')
print(A-B)

print('Multiplicação:')
print(A*B)

print('Divisão:')
print(A/B) # RETORNA SEMPRE UM FLOAT (5.0, 2.1 etc)

# uma maneira de definir o tipo de uma variável é usando casting

X = str(0) # '0'
Y = int(0) # 0
Z = float(0) # 0.0

# é possivel declarar várias de uma vez

X, Y, Z = str(0), int(0), float(0)

# é possivel declarar um valor a todas elas

X = Y = Z = 'abobora'

# é possivel designar cada variavel para um elemento de um vetor

FRUTAS = ['maçã', 'banana', 'cereja']

X, Y, Z = FRUTAS

# print em múltiplas variaveis

print(X, Y, Z)

# concatenar ou somar

print(X + Y + Z)
