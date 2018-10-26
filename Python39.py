mb = (float(input('Digite o tamanho do seu arquivo em mb: ')))*1000
kbs = float(input('Qual a taxa de download em kb/s? '))
temposegundo = mb/kbs
hora = temposegundo//3600
minuto = (temposegundo % 3600)//60
segundo1 = temposegundo % 60
print('O tempo de download é: {} horas {} minutos e {} segundos'.format(hora, minuto, segundo1))
