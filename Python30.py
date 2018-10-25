#distancia entre pontos
import math
x1 = int(input('Coordenada x do primeiro par ordenado: '))
x2 = int(input('Coordenada x do segundo par ordenado: '))
y1 = int(input('Coordenada y do primeiro par ordenado: '))
y2 = int(input('Coordenada y do segundo par ordenado: '))
distancia = math.sqrt((x1-x2)**2 + (y1-y2)**2)
print('A distancia é: {:.2f} u.a.'.format(distancia))