ab = int(input('Digite o tamanho de um lado: '))
bc = int(input('Digite o tamanho de outro lado: '))
ac = int(input('Digite o tamanho do terceito lado: '))
if ab == bc == ac:
    print('O triangulo é equilátero.')
elif ab == bc != ac or ab == ac != bc or bc == ac != ab:
    print('O triangulo é isóceles.')
else:
    print('O triangulo é escaleno.')
