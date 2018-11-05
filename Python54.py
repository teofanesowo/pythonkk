# eita homem pra andar
czh = int(input('Hora de saída: '))
czmin = int(input('Minuto de saída: '))
souzamin = (czmin + 50) % 60
souzah = czh + (czmin + 50) // 60
print('Chegada em Souza: {} horas e {} minutos.'.format(souzah, souzamin))
patosmin = (souzamin + 20) % 60
patosh = souzah + 2 + (souzamin + 20)//60
print('Chegada em Patos: {} horas e {} minutos.'.format(patosh, patosmin))
cgmin = (patosmin + 50) % 60
cgh = patosh + 2 + (patosmin + 50)//60
print('Chegada em Campina Grande: {} horas e {} minutos.'.format(cgh, cgmin))
jpmin = (cgmin + 20) % 60
jph = cgh + 2 + (cgmin + 20)//60
print('Chegada em João Pessoa: {} horas e {} minutos.'.format(jph, jpmin))
