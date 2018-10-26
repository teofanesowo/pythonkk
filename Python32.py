#custo da gasolina e tals
distancia = float(input('Digite a distância a ser percorrida em km: '))
preco = float(input('Qual o preço do litro da gasolina? '))
gastolitro = distancia/14
custoviagem = gastolitro*preco
print('O custo para essa viagem será: R${:.2f}'.format(custoviagem))