# regra de tres basica
reais = int(input('Valor de uma passagem em reais: '))
milha = int(input('Valor de uma passagem em milhas: '))
reais2 = int(input('Valor da passagem que deseja comprar: '))
milha2 = (reais2 * milha) / reais
print('Você deve ter {} milhas para comprar essa passagem.'.format(milha2))
