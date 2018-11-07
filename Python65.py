idade = int(input('Digite a idade: '))
if 0 <= idade <= 12:
    print('É uma criança.')
elif 13 <= idade <= 17:
    print('É um adolescente.')
elif 18 <= idade <= 59:
    print('É um adulto.')
elif idade >= 60:
    print('É um idoso.')
else:
    print('Não existe idade negativa.')
