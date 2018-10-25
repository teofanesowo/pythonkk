#conversão Kb para os outros la
kb = float(input('Valor em kb: '))
bits = 8000*kb
bytes = 1000*kb
mb = kb/1000
gb = kb/8000000
print('Valores em {} bits, {} bytes, {} mb e {} gb'.format(bits,bytes,mb,gb))