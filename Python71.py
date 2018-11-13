a = int(input('Digite um número: '))
b = int(input('Digite um número: '))
c = int(input('Digite um número: '))
if a > b and a > c:
    print('O maior valor é {}'.format(a))
elif b > a and b > c:
    print('O maior valor é {}'.format(b))
else:
    print('O maior valor é {}'.format(c))
