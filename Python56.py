# usando tabela ascii topissima
letra = input('Digite a letra a ser codificada: ')
code = input('Digite a letra que será a codificação da letra anterior: ')
letra2 = input('Digite a letra que você quer encontrar a correspondente: ')
distancia = abs(ord(letra) - ord(code))
letracode = chr(ord(letra2) + distancia)
print("A letra correspondente a '{}' é '{}'".format(letra2, letracode))
