#usei biblioteca aqui pra fazer a área de um círculo(top)
import math
raio = int(input('digite o valor de seu raio: '))
area = math.pi*raio**2
comprimento = 2*math.pi*raio
print("A área é {:.2f} e o comprimento é {:.2f}".format(area,comprimento))
