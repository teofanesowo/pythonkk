#Calculo de dobro, triplo, etc...
numero = int(input("Digite um numero inteiro: "))
if (numero < 0):
    print("Valor precisa ser positivo!")
else:
    dobro = numero*2
    triplo = numero*3
    quadrado = numero**2
    cubo = numero**3
    raiz = numero**(1/2)
    print ('Os valores do dobro, triplo, quadrado, cubo e raiz são {}, {}, {}, {} e {:.2}, respectivamente' .format(dobro, triplo, quadrado, cubo, raiz))
