a = int(input('Digite um número: '))
b = int(input('Digite um número: '))
c = int(input('Digite um número: '))
if a > b > c:
    print('O valor do meio é: {}'.format(b))
elif a > c > b:
    print('O valor do meio é: {}'.format(c))
elif b > a > c:
    print('O valor do meio é: {}'.format(a))
elif b > c > a:
    print('O valor do meio é: {}'.format(c))
elif c > a > b:
    print('O valor do meio é: {}'.format(a))
else:
    print('O valor do meio é: {}'.format(b))
