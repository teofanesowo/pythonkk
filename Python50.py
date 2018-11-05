# Um atendimento rápido
senha = int(input('Digite a senha que você pegou: '))
tempo = (senha-1)*25  #está em minutos aqui
horaini = int(input('Hora de chegada: '))
minini = int(input('Minuto de chegada: '))
hora = horaini + tempo//60
min = minini + tempo%60
print('Você será atendido às {}:{}.'.format(hora, min))