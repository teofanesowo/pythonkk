#conversão de Celsius para Farenheit e Kelvin
celsius = int(input('Digite a sua temperatura em Celsius: '))
faren = 1.8*celsius + 32
kelvin = celsius + 273
print('O valor da temperatudo é {:.2f}F e {:.2f}K'.format(faren,kelvin))