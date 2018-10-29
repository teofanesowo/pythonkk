#maneira feia de transformar binário em decimal
print('Convertendo um valor na base binária genérico de 4 dígitos')
a = int(input('Digite o primeiro valor da esquerda para direita: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
d = int(input('Quarto valor: '))
decimal = (2**3)*a + (2**2)*b + (2**1)*c + (2**0)*d
print('O valor em base 10 é: {}'.format(decimal))