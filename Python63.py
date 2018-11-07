time1 = int(input('Número de gols do time 1: '))
time2 = int(input('Número de gols do time 2: '))
if time1 > time2:
    print('Time 1 Venceu!')
elif time1 < time2:
    print('Time 2 Venceu!')
else:
    print('Empate.')
