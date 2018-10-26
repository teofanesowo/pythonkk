#conseguir os valores de um numero
numero = int(input('Digite um numero positivo entre 1 e 9999: '))
milha = numero//1000
centena = (numero%1000)//100
dezena = (numero%100)//10
unidade = numero%10
print('Valor da milha: {} \n Valor da centena: {} \n Valor da dezena: {} \n Valor da unidade: {}'.format(milha, centena, dezena, unidade))