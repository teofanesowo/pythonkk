# financiamento safado esse aqui
valor = float(input('Digite o valor a ser financiado: '))
parcela = int(input('Quantas parcelas? '))
parcelavalor = valor/parcela + valor*0.04
valorpago = parcelavalor*parcela
print('Valor da parcela: R${}'.format(parcelavalor))
print('Valor total a ser pago: R${}'.format(valorpago))
