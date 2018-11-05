print('~~~~~Ano e mês do início da pena~~~~~')
anoini = int(input('Digite o ano: '))
mesini = int(input('Digite o mes: '))
anopen = int(input('Digite o numero de anos preso: '))
mespen = int(input('Digite o numero de meses presos: '))
mesfin = (mesini + mespen) % 12
anofin = anoini + anopen + (mesini + mespen)//12
print('Data de soltura: ano {} e mês {}.'.format(anofin, mesfin))
