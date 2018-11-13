a = int(input('Digite um número: '))
b = int(input('Digite um número: '))
c = int(input('Digite um número: '))
if a > b > c:
    print('O maior valor é {} e o menor valor é {}'.format(a, c))
elif a > c > b:
    print('O maior valor é {} e o menor valor é {}'.format(a, b))
elif b > a > c:
    print('O maior valor é {} e o menor valor é {}'.format(b, c))
elif b > c > a:
    print('O maior valor é {} e o menor valor é {}'.format(b, a))
elif c > a > b:
    print('O maior valor é {} e o menor valor é {}'.format(c, b))
else:
    print('O maior valor é {} e o menor valor é {}'.format(c, a))
