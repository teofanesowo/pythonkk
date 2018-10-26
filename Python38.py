segundo = int(input('Digite seus segundos: '))
hora = segundo//3600
min = (segundo%3600)//60
segundo1 = segundo%60
print('A conversão é: {} horas {} minutos e {} segundos'.format(hora,min,segundo1))
