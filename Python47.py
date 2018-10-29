# financiamento
valorfin = float(input('Digite o valor a ser emprestado: '))
prestacao1 = valorfin*0.2
prestacao25 = prestacao1*1.07
jurostotal = prestacao1*0.07*4
print('Valor da primeira prestação: R${:.2f}'.format(prestacao1))
print('Valor das próximas prestações: R${:.2f}'.format(prestacao25))
print('O juros total foi: R${:.2f}'.format(jurostotal))
