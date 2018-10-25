total = int(input('Número total de questões: '))
acerto = int(input('Número de acertos: '))
porcacerto = (acerto/total)*100
porcerro = 100 - porcacerto
print('Porcentagem de acertos: {}% //// Porcentagem de erros : {}%'.format(porcacerto,porcerro))