# inversão
numero = int(input('Digite um numero de 0 a 999: '))
centena = str(numero//100)
dezena = str((numero%100)//10)
unidade = str(numero%10)
valorreverso = unidade + dezena + centena
print('Valor inverso: {}'.format(valorreverso))