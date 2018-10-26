#amo camiula
datacompra = int(input('Data da realização da compra: '))
prazo = int(input('Prazo de pagamento da primeira parcela: '))
pagamentomes = (prazo + datacompra)//30
pagamentodia = prazo + datacompra - pagamentomes*30
print('O pagamento será realizado daqui a {} meses, no dia {}'.format(pagamentomes, pagamentodia))
