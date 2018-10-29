# Índice de massa corporal
peso = float(input('Digite seu peso em kg: '))
altura = float(input('Digite sua altura em metros: '))
imc = peso/altura**2
print('Seu índice de massa corporal é {:.2f}kg/m²'.format(imc))
