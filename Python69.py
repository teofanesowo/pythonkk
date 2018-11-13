x = int(input('Digite sua coordenada x: '))
y = int(input('Digite sua coordenada y: '))
if x > 0 and y > 0:
    print('Está no primeiro quadrante.')
elif x > 0 and y < 0:
    print('Está no quarto quadrante.')
elif x < 0 and y > 0:
    print('Está no segundo quadrante.')
elif x < 0 and y < 0:
    print('Está no terceiro quadrante.')
else:
    print('O ponto informado é o centro.')
