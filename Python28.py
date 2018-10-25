#Modos de pagamento
compra = int(input('Digite o valor de compra: '))
compravista = compra*0.9
compra3parc = compra/3
compra10parc = (compra + compra*0.2)/10
print('O valor da compra vista é: R${}'.format(compravista))
print('ou 3 parcelas de R${:.2f}'.format(compra3parc))
print('ou 10 parcelas de R${:.2f}'.format(compra10parc))
