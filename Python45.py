# vish
salario = float(input('Digite seu salário: '))
objetivo = float(input('Quanto de dinheiro você quer juntar? '))
tempo = objetivo/(salario*0.25)
anos = int(tempo//12)
meses = int(tempo - anos*12)
print('O tempo para juntar o dinheiro completo será {} anos e {} meses.'.format(anos, meses))
