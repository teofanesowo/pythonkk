#nesse exemplo n considero que ele fez menos de 160 horas
horas = int(input('Quantas horas de trabalho você realizou esse mês? '))
preçohora = float(input('Quando você recebe por hora de trabalho? '))
pagamento = 160*preçohora + (horas - 160)*preçohora*1.5
print('Você deve receber R${:.2f}.'.format(pagamento))