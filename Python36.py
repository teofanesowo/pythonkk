#manipulação de variáveis
a = int(input('Digite a varíavel a: '))
b = int(input('Digite a variável b: '))
print('Valor de a = {} e b = {}' .format(a, b))
t = a
a = b
b = t
print('Valor de a = {} e b = {}'.format(a, b))