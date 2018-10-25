#media ponderada de 3 valores
valor1 = float(input('Digite o primeiro valor: '))
peso1 = float(input('Digite o peso do primeiro valor: '))
valor2 = float(input('Digite o segundo valor: '))
peso2 = float(input('Digite o peso do segundo valor: '))
valor3 = float(input('Digite o terceiro valor: '))
peso3 = float(input('Digite o peso do terceiro valor: '))
mediaponderada = (valor1*peso1 + valor2*peso2 + valor3*peso3)/(peso1 + peso2 + peso3)
print(mediaponderada)
