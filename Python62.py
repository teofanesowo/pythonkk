# múltiplo
n = int(input('Digite um número: '))
m = int(input('Digite outro número: '))
if m % n == 0 :
    print('O valor {} é múltiplo de {}.'.format(m, n))
elif n % m == 0:
    print('O valor {} é múltiplo de {}.'.format(n, m))
else:
    print('Não são múltiplos.')
