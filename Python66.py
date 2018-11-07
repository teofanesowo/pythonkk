pessoa = int(input('Digite o número de pessoas: '))
quilo = pessoa*0.250
if pessoa % 4 == 0:
    print('A quantidade de carne necessária é {} kg'.format(int(quilo)))
else:
    print('A quantidade de carne necessária é {} kg'.format(int(quilo + 1)))
