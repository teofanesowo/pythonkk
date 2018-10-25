#volume e tals bem top
comprimento = int(input('Digite o comprimeto da sua cisterna em metros: '))
largura = int(input('Digite a largura da cisterna em metros: '))
litro = (int(input('Quantos litros sua cisterna deve suportar? ')))/1000
altura = litro/(comprimento*largura)
print(altura)