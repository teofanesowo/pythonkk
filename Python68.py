salariobruto = float(input('Digite o valor do seu salário bruto: '))
if  salariobruto <= 1903.98:
    salarioliquido = salariobruto - salariobruto * 0.11
elif 1903.99 <= salariobruto <= 2826.65:
    salarioliquido = salariobruto - salariobruto * 0.11 - salariobruto * 0.075
elif 2826.66 <= salariobruto <= 3751.05:
    salarioliquido = salariobruto - salariobruto * 0.11 - salariobruto * 0.15
elif 3751.06 <= salariobruto <= 4664.68:
    salarioliquido = salariobruto - salariobruto * 0.11 - salariobruto * 0.225
elif salariobruto >= 4664.69:
    salarioliquido = salariobruto - salariobruto * 0.11 - salariobruto * 0.275
print('O valor do seu salário líquido é {:.2f}'.format(salarioliquido))
