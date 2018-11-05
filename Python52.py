gasto = int(input('Digite o gasto do mês: '))
if gasto <= 100:
    custo = 80
else:
    custo = 80 + (gasto - 100)*5
print('O preço de sua mensalidade é R${:.2f}'.format(custo))
